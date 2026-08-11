# GapBridge

Offline cybersecurity policy gap analysis and improvement tool.

GapBridge takes an organizational policy document, compares it against the CIS MS-ISAC NIST Cybersecurity Framework Policy Template Guide (2024), identifies gaps, scores the policy's maturity, generates a prioritized improvement roadmap, and drafts a revised version of the policy that addresses the missing controls, grounded in the actual NIST guide text via retrieval-augmented generation. Everything runs on a local LLM (Mistral 7B, via Ollama) with no external API calls or internet dependency after initial setup.

## Table of Contents

- [How to Run](#how-to-run)
- [Dependencies and Installation](#dependencies-and-installation)
- [Logic and Workflow](#logic-and-workflow)
- [Project Structure](#project-structure)
- [Known Issues Found and Fixed During Testing](#known-issues-found-and-fixed-during-testing)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)

## How to Run

### Prerequisites

- Python 3.11+
- [Ollama](https://ollama.com) installed and running locally
- The `mistral` model pulled in Ollama

### Setup

```bash
git clone https://github.com/shashwat2806/GapBridge.git
cd GapBridge

python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux

pip install -r requirements.txt

ollama pull mistral
```

### Running the pipeline (CLI)

```bash
python main.py data/sample_policies/isms_policy.txt
```

Runs the full pipeline against a single policy file and writes results to `output/`, prefixed with the policy's filename. A full run makes 15-20+ sequential calls to the local LLM and typically takes 5-10 minutes on CPU-only hardware.

Any of the four sample policies work the same way:

```bash
python main.py data/sample_policies/data_privacy_policy.txt
python main.py data/sample_policies/patch_management_policy.txt
python main.py data/sample_policies/risk_management_policy.txt
```

### Running the web UI

```bash
streamlit run ui/app.py
```

Opens a browser interface with three pages, navigable from the sidebar:

- **Home**: what the tool does, why it's offline, and what you get, with a shortcut into the analysis flow.
- **Upload & Analyze**: select a sample policy or upload your own (`.txt`, `.pdf`, `.docx`), review the settings panel (framework, control count, model), and run the analysis. A live progress indicator tracks each pipeline stage.
- **Results**: maturity metrics, a per-function breakdown with status badges, and four tabs (Breakdown, Roadmap, Report, Policy) with download buttons for the generated files.

A logo image at `assets/logo.png` is used in the header if present; the app falls back to a plain text header if it's missing.

### One-time knowledge base build (for RAG grounding)

Only needs to run once, or whenever the reference PDF changes:

```bash
python build_knowledge_base.py
```

Chunks and embeds `data/sample_policies/nist_2024.pdf` so generated policy clauses can be grounded in the actual guide text rather than relying only on the model's own training knowledge.

## Dependencies and Installation

All dependencies are listed in `requirements.txt`:

| Package | Purpose |
|---|---|
| `pdfplumber` | Extracts text from PDF policy files and the NIST reference guide |
| `python-docx` | Extracts text from DOCX policy files |
| `sentence-transformers` | Generates embeddings for semantic gap detection and RAG retrieval (`all-MiniLM-L6-v2`) |
| `numpy` | Vector math for cosine similarity and embedding storage |
| `requests` | Sends prompts to the local Ollama API |
| `rich` | Color-coded terminal output |
| `fpdf2` | Generates PDF summary reports |
| `streamlit` | Web UI |

Ollama and the `mistral` model are installed separately (not via pip). No cloud APIs, API keys, or internet access are required once the model is pulled locally.

`config.py` sets `HF_HUB_OFFLINE=1` and `TRANSFORMERS_OFFLINE=1` at import time, so `sentence-transformers` never attempts a network check against Hugging Face once the embedding model is cached. This was added after a real startup hang (see below).

## Logic and Workflow

GapBridge runs as a sequential pipeline, where each stage consumes the previous stage's output:

```
1. Load policy       (engine/policy_loader.py)
2. Load framework     (engine/framework_loader.py)
3. Detect gaps         (engine/gap_detector.py)
4. Calculate scorecard  (engine/scorecard.py)
5. Generate roadmap      (engine/roadmap_generator.py)
6. Generate report         (engine/report_generator.py)
7. Revise policy             (engine/policy_reviser.py)
8. Export (terminal/PDF/files/UI)
```

**1-2. Loading.** The policy file (TXT, PDF, or DOCX) and the 106-control NIST CSF framework (structured JSON) are loaded into memory.

**3. Gap detection.** The policy text is split into overlapping word chunks. Both the chunks and each of the 106 control descriptions are embedded using `all-MiniLM-L6-v2`. For each control, GapBridge computes cosine similarity against every policy chunk and keeps the highest score. If that score falls below 0.45, the control is flagged as a gap.

**4. Scorecard.** Gaps are aggregated per NIST function (GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER) into a percentage-coverage score, an overall maturity percentage, a weighted score (GOVERN and IDENTIFY weighted higher, since governance gaps tend to be foundational), and a maturity label (Initial / Basic / Developing / Managed / Mature).

**5. Roadmap.** The six NIST functions are ranked by weakness and split into thirds (short/mid/long term), rather than fixed percentage cutoffs. This keeps the roadmap balanced regardless of how a given policy's scores happen to cluster.

**6. Report.** For each function scoring below 50%, Mistral is prompted to write a specific, actionable recommendation referencing the actual missing control IDs.

**7. Policy revision.** For every NIST function with at least one gap, GapBridge retrieves the most relevant passages from the NIST guide text and prompts Mistral to draft new formal policy language addressing those gaps, grounded in the retrieved guidance rather than the model's own general knowledge.

**RAG grounding (`rag/`).** The NIST guide PDF is chunked and embedded once (`build_knowledge_base.py`), cached to `data/knowledge_base/`. At generation time, `rag/retriever.py` retrieves the top-3 most similar guide passages for the relevant gap descriptions, which are injected into the prompt as grounding context before Mistral drafts each policy clause.

**8. Export.** Results are written as Markdown, JSON, CSV, a one-page PDF executive summary, color-coded terminal tables (`rich`), and shown live in the Streamlit UI.

## Project Structure

```
GapBridge/
├── assets/
│   └── logo.png                            # optional UI header branding
├── data/
│   ├── frameworks/cis_ms_isac_2024.json    # 106 NIST controls, structured
│   ├── knowledge_base/                      # cached NIST guide chunks + embeddings
│   └── sample_policies/                     # 4 test policies + reference PDF
├── engine/
│   ├── policy_loader.py
│   ├── framework_loader.py
│   ├── gap_detector.py
│   ├── scorecard.py
│   ├── roadmap_generator.py
│   ├── report_generator.py
│   ├── policy_reviser.py
│   └── llm_client.py
├── rag/
│   ├── document_chunker.py
│   ├── embedding_store.py
│   └── retriever.py
├── ui/app.py                 # Streamlit interface (Home / Upload & Analyze / Results)
├── terminal_display.py       # Rich terminal output
├── pdf_exporter.py           # PDF summary export
├── main.py                   # CLI entry point
├── config.py                 # Central constants, offline-mode flags
├── build_knowledge_base.py   # One-time RAG setup
└── output/                   # Generated results per policy
```

## Known Issues Found and Fixed During Testing

These were caught by actually running the tool against real policies, not by inspection. Kept here as an honest record of the debugging process:

- **Roadmap bucketing collapsed to zero in the middle band.** The original `roadmap_generator.py` used fixed percentage cutoffs (< 20% short term, < 50% mid term). On a policy where 5 of 6 functions scored under 13%, everything piled into short term, nothing landed in mid term. Fixed by ranking functions by weakness and splitting into thirds instead, which stays balanced regardless of how a policy's scores cluster.
- **RAG retrieval pulled in source-document boilerplate.** The knowledge base was built from the full extracted PDF text, including the cover page and a closing marketing paragraph from the source guide. That text once got retrieved and woven into a generated RECOVER policy clause. Fixed by trimming the source text to the actual technical content before chunking.
- **Generated clauses cited control IDs that weren't actual gaps.** Because retrieval is similarity-based, a GOVERN clause once cited two controls that the policy actually already satisfied, since they were topically adjacent to real gaps in the retrieved text. Fixed with an explicit prompt constraint restricting Mistral to only cite the control IDs listed as actual gaps.
- **Streamlit sidebar navigation didn't respond to programmatic redirects.** The page-selector radio had no `index=` bound to `st.session_state.current_page`, so calling `st.rerun()` after setting the page in code (e.g. auto-redirecting to Results after analysis) was silently overwritten by the radio's own last-rendered state. Fixed by explicitly binding the radio's `index` to the current session state value.
- **Roadmap items rendered as raw Python dicts in the UI.** An early version of the Results page did `st.markdown(f"- {item}")` where `item` was a dict, printing literal dict text on screen. Fixed by formatting each field explicitly.

## Limitations

- **Speed.** Running entirely on local CPU (no GPU), a full pipeline run makes 15-20+ sequential Mistral calls and takes roughly 5-10 minutes. Deliberate tradeoff for full offline operation.
- **Semantic gap detection isn't perfect.** Cosine similarity against control descriptions can occasionally miss context-dependent phrasing, or flag an adequately-worded clause as a gap. The 0.45 threshold was chosen empirically.
- **RAG retrieval can still occasionally surface tangentially related content**, since it's similarity-based rather than exact matching. The prompt-level constraint mitigates the worst case but isn't a hard guarantee against topical drift more broadly.
- **No automated test suite.** Testing was done via manual per-module test scripts rather than pytest.
- **Tested only on Windows.** Path handling and the Ollama connection have not been verified on macOS or Linux.
- **Streamlit UI has no persistence.** Results exist only in the browser session; closing the tab loses them unless downloaded first.

## Future Improvements

- Add a pytest suite for automated regression testing across all modules.
- Support additional frameworks beyond NIST CSF (e.g., ISO 27001, SOC 2) via the same architecture.
- Allow user-adjustable similarity thresholds and function weights from the UI, rather than fixed values in `config.py`.
- Persist Streamlit session results so analyses survive a page refresh.
- Batch mode: run all sample policies in one command and generate a comparison report.

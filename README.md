# GapBridge

Offline cybersecurity policy gap analysis engine that checks policy documents against the NIST CSF 2.0 framework. No cloud APIs, no internet required.

## Overview

GapBridge takes an organization's cybersecurity policy document and analyzes it against the 106 controls in the NIST CSF 2.0 framework, via the CIS MS-ISAC 2024 mapping. It flags gaps, scores coverage, and generates a prioritized remediation roadmap, entirely offline, using a local LLM (Ollama with Mistral 7B) instead of a cloud API.

Originally built as the primary deliverable of an AI/ML internship at C3iHub, IIT Kanpur.

## Features

* Parses policy documents (.docx / PDF) and maps their content against 106 NIST CSF 2.0 controls
* Detects gaps using semantic similarity (sentence-transformers, all-MiniLM-L6-v2) rather than naive keyword matching
* Generates a compliance scorecard (JSON/CSV) and a prioritized roadmap covering 3, 6, and 12 month windows
* Uses a local RAG pipeline (chunking, embeddings, and retrieval) to ground an offline LLM when drafting revised policy language and gap reports
* Exports Markdown reports and PDF summaries
* Ships a CLI (argparse) and a Streamlit UI, both driving the same underlying pipeline
* Runs fully offline. No data leaves the machine, no API keys, no cloud dependency

## Tech stack

Python, pdfplumber, python-docx, sentence-transformers, numpy, Ollama (Mistral 7B), Rich, fpdf2, Streamlit

## Project structure

```
GapBridge/
├── engine/              core pipeline: policy loading, gap detection, scoring, roadmap and report generation
├── rag/                 chunking, embedding store, retriever for the offline RAG pipeline
├── data/
│   ├── frameworks/      NIST CSF 2.0 / CIS MS-ISAC 2024 control set
│   ├── sample_policies/ example policy documents to try the tool on
│   └── knowledge_base/  prebuilt chunks and embeddings for RAG
├── ui/app.py            Streamlit interface
├── main.py              CLI entry point
├── config.py             thresholds, model names, paths
└── output/               generated scorecards, roadmaps, reports, PDFs
```

## Getting started

### Prerequisites

* Python 3.10 or newer
* Ollama installed locally, with the Mistral model pulled:

```bash
ollama pull mistral
```

### Installation

```bash
git clone https://github.com/shashwat2806/GapBridge.git
cd GapBridge
pip install -r requirements.txt
```

### Usage

Run the CLI on a policy document:

```bash
python main.py data/sample_policies/isms_policy.txt
```

This prints a scorecard to the terminal and writes a scorecard, gap breakdown, roadmap, report, PDF summary, and revised policy draft to output/.

Or launch the Streamlit UI:

```bash
streamlit run ui/app.py
```

## How it works

1. Load. The policy document and the NIST CSF 2.0 control set are parsed
2. Detect gaps. Each control is compared against the policy text using semantic similarity between sentence embeddings
3. Score. A coverage scorecard is calculated across the CSF functions
4. Generate roadmap. Gaps are prioritized into short term, mid term, and long term remediation items
5. Report and revise. A local LLM (Mistral 7B via Ollama), grounded with a RAG pipeline over the NIST framework, drafts a gap report and revised policy language

## Roadmap

* Hosted web version (FastAPI and React) on free tier infrastructure (Render, Vercel, Neon Postgres), with Groq as a swappable hosted LLM provider alongside the offline CLI and Streamlit path

## License

MIT. See LICENSE

## Acknowledgments

Built during an AI/ML internship at C3iHub, IIT Kanpur.

from engine.llm_client import query_mistral
from rag.retriever import retrieve_context

def generate_policy_clause(function_name, missing_controls):
    control_list = "\n".join(f"- {c['id']}: {c['description']}" for c in missing_controls[:8])
    query_text = " ".join(c["description"] for c in missing_controls[:8])
    nist_context = retrieve_context(query_text, top_k=3)
    context_block = "\n".join(f"- {chunk}" for chunk in nist_context)

    prompt = f"""You are drafting formal policy language for an organizational cybersecurity policy document. Write a new policy section addressing the {function_name} function of the NIST Cybersecurity Framework. The section must cover these specific requirements:

{control_list}

Here is relevant guidance from the official NIST Cybersecurity Framework Policy Template Guide to inform your wording and terminology:

{context_block}

Important: only cite the control IDs listed above under "specific requirements." Do not reference any other control ID that appears in the guidance text above, even if it seems related.

Write this as formal policy text, not advice - use "shall" and "must" statements as found in an actual corporate policy. Include a short section heading. Keep it to one paragraph, 4-6 sentences."""
    return query_mistral(prompt)

def generate_revised_policy(original_policy_text, gaps):
    by_function = {}
    for g in gaps:
        if g["gap_found"]:
            by_function.setdefault(g["function"], []).append(g) 

    sections = ["# Revised Policy Document\n"]
    sections.append("## Original Policy Text\n")
    sections.append(original_policy_text)
    sections.append("\n\n## Added Provisions (Gap Remediation)\n")
    sections.append("_The following sections address gaps identified against the NIST Cybersecurity Framework, grounded in retrieved guidance from the CIS MS-ISAC NIST CSF 2024 Policy Template Guide._\n")

    for fn, missing in by_function.items():
        print(f"drafting policy clause for {fn} ({len(missing)} gaps)")
        clause = generate_policy_clause(fn, missing)
        sections.append(f"### {fn}\n")
        sections.append(f"{clause}\n")

    return "\n".join(sections)

def save_revised_policy(text, filepath="output/revised_policy.md"):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
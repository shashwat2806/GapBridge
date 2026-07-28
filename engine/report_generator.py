from engine.llm_client import query_mistral
from config import WEAK_FUNCTION_THRESHOLD

def generate_recommendation(function_name, missing_controls):
    control_list = "\n".join(f"- {c['id']}: {c['description']}" for c in missing_controls[:8])

    prompt = f"""You are a cybersecurity policy analyst. The organization's policy is weak in the {function_name} function of the NIST Cybersecurity Framework. The following controls are not adequately addressed:

{control_list}

Write exactly 3 separate sentences (not one long sentence with commas) giving a practical recommendation for closing this gap. Reference at least 2 of the specific control IDs listed above by name. No preamble, no headers, just the recommendation text."""

    return query_mistral(prompt)

def generate_report(gaps, scorecard, weak_threshold=WEAK_FUNCTION_THRESHOLD):
    lines = ["# GapBridge Policy Gap Analysis Report\n"]
    lines.append(f"**Overall Maturity Score:** {scorecard['overall_pct']}% ({scorecard['maturity_label']})")
    lines.append(f"**Weighted Score:** {scorecard['weighted_pct']}%\n")
    lines.append("## Scorecard by NIST Function\n")

    for fn, d in scorecard["by_function"].items():
        lines.append(f"- **{fn}:** {d['met']}/{d['total']} controls met ({d['pct']}%)")

    lines.append("\n## Recommendations\n")

    for fn, d in scorecard["by_function"].items():
        if d["pct"] >= weak_threshold:
            continue

        missing = [g for g in gaps if g["function"] == fn and g["gap_found"]]
        if not missing:
            continue

        print(f"generating recommendation for {fn} ({len(missing)} gaps)")
        rec = generate_recommendation(fn, missing)
        lines.append(f"### {fn} ({d['pct']}% - needs attention)\n")
        lines.append(f"{rec}\n")

    lines.append("\n## Appendix: Full Gap Details\n")
    for g in gaps:
        status = "Met" if not g["gap_found"] else "Gap"
        lines.append(f"- **{g['id']}** [{g['function']}] {status} (score: {g['score']}) - {g['description']}")

    return "\n".join(lines)

def save_report(report_text, filepath="output/report.md"):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(report_text)
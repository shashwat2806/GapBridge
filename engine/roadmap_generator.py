# engine/roadmap_generator.py

def generate_roadmap(gaps, scorecard):
    by_pct = sorted(scorecard["by_function"].items(), key=lambda x: x[1]["pct"])
    names = [fn for fn, _ in by_pct]

    third = max(1, len(names) // 3)
    short_fns = set(names[:third])
    mid_fns = set(names[third:2 * third])
    long_fns = set(names[2 * third:])

    short_term, mid_term, long_term = [], [], []

    for gap in gaps:
        if not gap["gap_found"]:
            continue

        pct = scorecard["by_function"][gap["function"]]["pct"]
        item = {
            "id": gap["id"],
            "function": gap["function"],
            "description": gap["description"],
            "related_policies": gap.get("related_policies", []),
            "function_coverage_pct": pct,
        }

        if gap["function"] in short_fns:
            short_term.append(item)
        elif gap["function"] in mid_fns:
            mid_term.append(item)
        else:
            long_term.append(item)

    
    for bucket in (short_term, mid_term, long_term):
        bucket.sort(key=lambda i: i["function_coverage_pct"])

    return {
        "short_term_0_3_months": short_term,
        "mid_term_3_6_months": mid_term,
        "long_term_6_12_months": long_term,
    }


def save_roadmap(roadmap, filepath="output/roadmap.md"):
    lines = ["# GapBridge Improvement Roadmap\n"]

    sections = [
        ("Short Term (0-3 months)", "short_term_0_3_months"),
        ("Mid Term (3-6 months)", "mid_term_3_6_months"),
        ("Long Term (6-12 months)", "long_term_6_12_months"),
    ]

    for title, key in sections:
        items = roadmap[key]
        lines.append(f"## {title}\n")
        if not items:
            lines.append("_No gaps in this priority band._\n")
            continue
        for item in items:
            lines.append(
                f"- **{item['id']}** [{item['function']}, function at "
                f"{item['function_coverage_pct']}% coverage] {item['description']}"
            )
        lines.append("")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
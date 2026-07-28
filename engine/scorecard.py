import json
import csv

MATURITY_LABELS = [
    (80, "Mature"),
    (60, "Managed"),
    (40, "Developing"),
    (20, "Basic"),
    (0, "Initial"),
]

FUNCTION_WEIGHTS = {
    "GOVERN": 1.5,
    "IDENTIFY": 1.2,
    "PROTECT": 1.0,
    "DETECT": 1.0,
    "RESPOND": 1.0,
    "RECOVER": 0.8,
}


def get_maturity_label(pct):
    for threshold, label in MATURITY_LABELS:
        if pct >= threshold:
            return label
    return "Initial"


def calculate_scorecard(gaps, controls_by_id=None):
    by_function = {}

    for g in gaps:
        fn = g.get("function")
        if not fn and controls_by_id:
            fn = controls_by_id.get(g["id"], "UNKNOWN")
        if not fn:
            fn = "UNKNOWN"

        if fn not in by_function:
            by_function[fn] = {"met": 0, "total": 0}

        by_function[fn]["total"] += 1
        if not g["gap_found"]:
            by_function[fn]["met"] += 1

    for fn in by_function:
        d = by_function[fn]
        d["pct"] = round(100 * d["met"] / d["total"], 1) if d["total"] else 0.0

    total_met = sum(d["met"] for d in by_function.values())
    total_controls = sum(d["total"] for d in by_function.values())
    overall_pct = round(100 * total_met / total_controls, 1) if total_controls else 0.0

    weighted_sum = 0
    weight_total = 0
    for fn, d in by_function.items():
        w = FUNCTION_WEIGHTS.get(fn, 1.0)
        weighted_sum += d["pct"] * w
        weight_total += w
    weighted_pct = round(weighted_sum / weight_total, 1) if weight_total else 0.0

    return {
        "overall_pct": overall_pct,
        "weighted_pct": weighted_pct,
        "maturity_label": get_maturity_label(overall_pct),
        "by_function": by_function,
    }


def get_control_breakdown(gaps, controls_by_id=None):
    breakdown = []
    for g in gaps:
        fn = g.get("function") or (controls_by_id.get(g["id"], "UNKNOWN") if controls_by_id else "UNKNOWN")
        breakdown.append({
            "control_id": g["id"],
            "function": fn,
            "met": not g["gap_found"],
        })
    return breakdown


def export_json(scorecard, filepath):
    with open(filepath, "w") as f:
        json.dump(scorecard, f, indent=2)


def export_csv(breakdown, filepath):
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["control_id", "function", "met"])
        writer.writeheader()
        writer.writerows(breakdown)

def print_scorecard(scorecard):
    print(f"Overall: {scorecard['overall_pct']}% - {scorecard['maturity_label']}")
    print(f"Weighted: {scorecard['weighted_pct']}%\n")
    for fn, d in scorecard["by_function"].items():
        print(f"{fn}: {d['met']}/{d['total']} ({d['pct']}%)")
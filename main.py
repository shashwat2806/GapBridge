from terminal_display import show_scorecard, show_roadmap_summary
from pdf_exporter import export_pdf
import argparse
import os
os.environ["HF_HUB_OFFLINE"] = "1"

from engine.policy_loader import load_policy
from engine.framework_loader import load_framework
from engine.gap_detector import detect_gaps
from engine.scorecard import calculate_scorecard, print_scorecard, get_control_breakdown, export_json, export_csv
from engine.roadmap_generator import generate_roadmap, save_roadmap
from engine.report_generator import generate_report, save_report
from engine.policy_reviser import generate_revised_policy, save_revised_policy
from config import FRAMEWORK_PATH, OUTPUT_DIR

def run_pipeline(policy_path):
    name = os.path.splitext(os.path.basename(policy_path))[0]
    print(f"\n=== Running GapBridge on {name} ===\n")

    policy_text = load_policy(policy_path)
    controls = load_framework(FRAMEWORK_PATH)
    gaps = detect_gaps(policy_text, controls)

    scorecard = calculate_scorecard(gaps)
    print_scorecard(scorecard)

    breakdown = get_control_breakdown(gaps)
    export_json(scorecard, f"{OUTPUT_DIR}/{name}_scorecard.json")
    export_csv(breakdown, f"{OUTPUT_DIR}/{name}_breakdown.csv")

    print("\ngenerating roadmap")
    roadmap = generate_roadmap(gaps, scorecard)
    show_scorecard(name, scorecard)
    show_roadmap_summary(roadmap)
    export_pdf(name, scorecard, roadmap, f"{OUTPUT_DIR}/{name}_summary.pdf")
    save_roadmap(roadmap, f"{OUTPUT_DIR}/{name}_roadmap.md")
    print(
        f"  short term: {len(roadmap['short_term_0_3_months'])} items, "
        f"mid term: {len(roadmap['mid_term_3_6_months'])} items, "
        f"long term: {len(roadmap['long_term_6_12_months'])} items"
    )

    print("\ngenerating report")
    report = generate_report(gaps, scorecard)
    save_report(report, f"{OUTPUT_DIR}/{name}_report.md")

    print("generating revised policy")
    revised = generate_revised_policy(policy_text, gaps)
    save_revised_policy(revised, f"{OUTPUT_DIR}/{name}_revised_policy.md")

    print(f"\nDone. Outputs saved with prefix '{name}_' in {OUTPUT_DIR}/")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GapBridge - offline cybersecurity policy gap analysis")
    parser.add_argument("policy", help="path to the policy file to analyze")
    args = parser.parse_args()
    run_pipeline(args.policy)
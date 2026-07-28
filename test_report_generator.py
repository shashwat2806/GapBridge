from engine.policy_loader import load_policy
from engine.framework_loader import load_framework
from engine.gap_detector import detect_gaps
from engine.scorecard import calculate_scorecard
from engine.report_generator import generate_report, save_report

policy_text = load_policy('data/sample_policies/isms_policy.txt')
controls = load_framework('data/frameworks/cis_ms_isac_2024.json')

gaps = detect_gaps(policy_text, controls)
scorecard = calculate_scorecard(gaps)

print("Generating report (this calls Mistral for each weak function, may take a few minutes)...")
report = generate_report(gaps, scorecard)
save_report(report, "output/report.md")

print("\nReport saved to output/report.md")
print(f"Report length: {len(report)} characters")
from engine.policy_loader import load_policy
from engine.framework_loader import load_framework
from engine.gap_detector import detect_gaps
from engine.scorecard import calculate_scorecard, print_scorecard, get_control_breakdown, export_json, export_csv

policy_text = load_policy('data/sample_policies/isms_policy.txt')
controls = load_framework('data/frameworks/cis_ms_isac_2024.json')

gaps = detect_gaps(policy_text, controls)

scorecard = calculate_scorecard(gaps)
print_scorecard(scorecard)

breakdown = get_control_breakdown(gaps)
export_json(scorecard, "output/scorecard.json")
export_csv(breakdown, "output/breakdown.csv")
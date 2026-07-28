from engine.policy_loader import load_policy
from engine.framework_loader import load_framework
from engine.gap_detector import detect_gaps
from engine.scorecard import calculate_scorecard
from engine.roadmap_generator import generate_roadmap

policy_text = load_policy('data/sample_policies/isms_policy.txt')
controls = load_framework('data/frameworks/cis_ms_isac_2024.json')
gaps = detect_gaps(policy_text, controls)
scorecard = calculate_scorecard(gaps)
roadmap = generate_roadmap(gaps, scorecard)

print(f"Short term: {len(roadmap['short_term_0_3_months'])} items")
print(f"Mid term: {len(roadmap['mid_term_3_6_months'])} items")
print(f"Long term: {len(roadmap['long_term_6_12_months'])} items")
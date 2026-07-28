from engine.policy_loader import load_policy
from engine.framework_loader import load_framework
from engine.gap_detector import detect_gaps

policy_text = load_policy('data/sample_policies/isms_policy.txt')
controls = load_framework('data/frameworks/cis_ms_isac_2024.json')

print(f"Total controls loaded: {len(controls)}")

gaps = detect_gaps(policy_text, controls)

total_gaps = sum(1 for g in gaps if g["gap_found"])
print(f"Total controls checked: {len(gaps)}")
print(f"Gaps found: {total_gaps}")
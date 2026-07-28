from engine.policy_loader import load_policy
from engine.framework_loader import load_framework
from engine.gap_detector import detect_gaps
from engine.policy_reviser import generate_revised_policy, save_revised_policy

policy_text = load_policy('data/sample_policies/isms_policy.txt')
controls = load_framework('data/frameworks/cis_ms_isac_2024.json')
gaps = detect_gaps(policy_text, controls)

print("Generating revised policy (calls Mistral per function, may take a few minutes)...")
revised = generate_revised_policy(policy_text, gaps)
save_revised_policy(revised)
print("Saved to output/revised_policy.md")
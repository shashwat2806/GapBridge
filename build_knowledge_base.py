from engine.policy_loader import load_policy
from rag.embedding_store import build_store

nist_text = load_policy('data/sample_policies/nist_2024.pdf')
start_marker = "GV.OC-01"
end_marker = "The Center for Internet Security, Inc. (CIS"

start_idx = nist_text.find(start_marker)
end_idx = nist_text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    nist_text = nist_text[start_idx:end_idx]
    print(f"Trimmed to {len(nist_text)} chars of technical content")
else:
    print("Warning: trim markers not found, using full extracted text")

build_store(nist_text)
print("Knowledge base built.")
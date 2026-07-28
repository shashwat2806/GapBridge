import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from engine.policy_loader import load_policy
from engine.framework_loader import load_framework
from engine.gap_detector import detect_gaps
from engine.scorecard import calculate_scorecard, get_control_breakdown
from engine.roadmap_generator import generate_roadmap
from engine.report_generator import generate_report
from engine.policy_reviser import generate_revised_policy
from config import FRAMEWORK_PATH, POLICY_DIR

st.set_page_config(page_title="GapBridge", layout="wide")

st.title("GapBridge")
st.caption("Offline cybersecurity policy gap analysis - NIST CSF 2024, local LLM, RAG-grounded")

SAMPLE_POLICIES = {
    "ISMS Policy": "isms_policy.txt",
    "Data Privacy Policy": "data_privacy_policy.txt",
    "Patch Management Policy": "patch_management_policy.txt",
    "Risk Management Policy": "risk_management_policy.txt",
}

with st.sidebar:
    st.header("Select Policy")
    source = st.radio("Source", ["Sample policy", "Upload your own"])

    policy_path = None
    policy_name = None
    uploaded = None

    if source == "Sample policy":
        choice = st.selectbox("Choose a sample", list(SAMPLE_POLICIES.keys()))
        policy_path = os.path.join(POLICY_DIR, SAMPLE_POLICIES[choice])
        policy_name = SAMPLE_POLICIES[choice].replace(".txt", "")
    else:
        uploaded = st.file_uploader("Upload a policy file", type=["txt", "pdf", "docx"])
        if uploaded:
            policy_path = os.path.join("output", f"_uploaded_{uploaded.name}")
            with open(policy_path, "wb") as f:
                f.write(uploaded.getbuffer())
            policy_name = os.path.splitext(uploaded.name)[0]

    run_button = st.button(
        "Run Analysis", type="primary",
        disabled=(source == "Upload your own" and not uploaded)
    )
    st.caption("Full run takes 5-10 minutes (multiple local Mistral calls).")

if run_button:
    status = st.status("Running GapBridge pipeline...", expanded=True)

    status.write("Loading policy and NIST framework...")
    policy_text = load_policy(policy_path)
    controls = load_framework(FRAMEWORK_PATH)

    status.write("Detecting gaps against NIST CSF 2024...")
    gaps = detect_gaps(policy_text, controls)

    status.write("Calculating scorecard...")
    scorecard = calculate_scorecard(gaps)

    status.write("Building improvement roadmap...")
    roadmap = generate_roadmap(gaps, scorecard)

    status.write("Generating recommendations (Mistral, per weak function)...")
    report = generate_report(gaps, scorecard)

    status.write("Drafting RAG-grounded revised policy clauses...")
    revised_policy = generate_revised_policy(policy_text, gaps)

    status.update(label="Analysis complete", state="complete", expanded=False)

    st.session_state["result"] = {
        "policy_name": policy_name,
        "scorecard": scorecard,
        "roadmap": roadmap,
        "report": report,
        "revised_policy": revised_policy,
        "breakdown": get_control_breakdown(gaps),
    }

if "result" in st.session_state:
    result = st.session_state["result"]
    scorecard = result["scorecard"]

    st.subheader(f"Results: {result['policy_name']}")

    col1, col2, col3 = st.columns(3)
    col1.metric("Overall Maturity", f"{scorecard['overall_pct']}%", scorecard["maturity_label"])
    col2.metric("Weighted Score", f"{scorecard['weighted_pct']}%")
    total_gaps = sum(1 for item in result["breakdown"] if not item["met"])
    col3.metric("Total Gaps Found", total_gaps)

    tab1, tab2, tab3, tab4 = st.tabs(["Scorecard", "Roadmap", "Report", "Revised Policy"])

    with tab1:
        st.write("#### Coverage by NIST Function")
        for fn, data in scorecard["by_function"].items():
            st.progress(data["pct"] / 100, text=f"{fn}: {data['pct']}% ({data['met']}/{data['total']} controls)")

    with tab2:
        roadmap = result["roadmap"]
        st.write(f"**Short term (0-3 months):** {len(roadmap['short_term_0_3_months'])} items")
        st.write(f"**Mid term (3-6 months):** {len(roadmap['mid_term_3_6_months'])} items")
        st.write(f"**Long term (6-12 months):** {len(roadmap['long_term_6_12_months'])} items")

    with tab3:
        st.markdown(result["report"])
        st.download_button(
            "Download Report (.md)", result["report"],
            file_name=f"{result['policy_name']}_report.md"
        )

    with tab4:
        st.markdown(result["revised_policy"])
        st.download_button(
            "Download Revised Policy (.md)", result["revised_policy"],
            file_name=f"{result['policy_name']}_revised_policy.md"
        )
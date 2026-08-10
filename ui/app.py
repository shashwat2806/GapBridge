"""
GapBridge
NIST CSF 2024 Policy Gap Analysis
 Streamlit Application
"""

import sys
import os
from datetime import datetime
import json

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

# PAGE CONFIG

st.set_page_config(
    page_title="GapBridge - NIST CSF 2024",
    layout="wide",
    page_icon="▨",
    initial_sidebar_state="expanded"
)


# DARK MODE


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

:root {
    --primary: #3b82f6;
    --primary-light: #60a5fa;
    --primary-dark: #1e40af;
    --success: #10b981;
    --success-dark: #059669;
    --warning: #f59e0b;
    --warning-dark: #d97706;
    --danger: #ef4444;
    --danger-dark: #dc2626;
    --bg-dark: #0f172a;
    --bg-darker: #0a0e27;
    --surface: #1e293b;
    --surface-light: #334155;
    --border: #475569;
    --text: #f1f5f9;
    --text-secondary: #cbd5e1;
    --text-tertiary: #94a3b8;
}

* {
    font-family: 'Inter', sans-serif;
}

html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    background-color: var(--bg-dark) !important;
    color: var(--text);
}

[data-testid="stSidebar"] {
    background-color: var(--bg-darker) !important;
    border-right: 1px solid var(--border);
}

h1, h2, h3, h4, h5, h6 {
    color: var(--text) !important;
    font-weight: 600;
    letter-spacing: -0.01em;
}

p, span, label {
    color: var(--text-secondary);
    line-height: 1.6;
}

a {
    color: var(--primary-light);
    text-decoration: none;
}

a:hover {
    color: var(--primary);
}

.main {
    background: var(--bg-dark);
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 10px 20px !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary) 100%) !important;
    box-shadow: 0 8px 20px rgba(59, 130, 246, 0.4) !important;
    transform: translateY(-2px) !important;
}

/* Metrics */
[data-testid="stMetric"] {
    background: linear-gradient(135deg, var(--surface) 0%, var(--surface-light) 100%);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 18px;
}

[data-testid="stMetricValue"] {
    color: var(--primary-light) !important;
    font-size: 32px !important;
    font-weight: 700 !important;
}

[data-testid="stMetricLabel"] {
    color: var(--text-tertiary) !important;
    font-size: 12px !important;
    font-weight: 500 !important;
}

/* Tabs */
[data-testid="stTabs"] button {
    color: var(--text-tertiary) !important;
    font-weight: 500 !important;
}

[data-testid="stTabs"] button[aria-selected="true"] {
    color: var(--primary-light) !important;
    border-bottom-color: var(--primary) !important;
}

/* Input fields */
.stTextInput > div > div > input,
.stSelectbox > div > div > select,
.stFileUploader {
    background-color: var(--surface) !important;
    color: var(--text) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    padding: 10px 12px !important;
}

.stTextInput > div > div > input:focus,
.stSelectbox > div > div > select:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2) !important;
    outline: none !important;
}

/* Expander */
.streamlit-expanderHeader {
    background: linear-gradient(90deg, rgba(59, 130, 246, 0.05) 0%, transparent 100%);
    border-radius: 8px;
    color: var(--text);
    font-weight: 500;
}

.stExpander {
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    background: var(--surface) !important;
}

/* Radio buttons */
.stRadio > div > label {
    color: var(--text) !important;
    font-weight: 500;
}

.stRadio input[type="radio"] {
    accent-color: var(--primary) !important;
}

/* Checkbox */
.stCheckbox > div > label {
    color: var(--text) !important;
    font-weight: 500;
}

.stCheckbox input[type="checkbox"] {
    accent-color: var(--primary) !important;
}

/* Progress bar */
.stProgress > div > div > div {
    background: linear-gradient(90deg, var(--primary) 0%, var(--primary-light) 100%) !important;
}

/* Divider */
hr {
    border: none !important;
    height: 1px !important;
    background: linear-gradient(90deg, transparent, var(--border), transparent) !important;
    margin: 24px 0 !important;
}

/* Download button */
.stDownloadButton > button {
    background: linear-gradient(135deg, var(--success) 0%, var(--success-dark) 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
}

.stDownloadButton > button:hover {
    box-shadow: 0 8px 20px rgba(16, 185, 129, 0.4) !important;
}

/* Alerts */
.stAlert {
    border-radius: 8px !important;
    padding: 12px 16px !important;
}

.stSuccess {
    background: rgba(16, 185, 129, 0.15) !important;
    border-left: 4px solid var(--success) !important;
}

.stError {
    background: rgba(239, 68, 68, 0.15) !important;
    border-left: 4px solid var(--danger) !important;
}

.stInfo {
    background: rgba(59, 130, 246, 0.15) !important;
    border-left: 4px solid var(--primary) !important;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: var(--bg-dark);
}

::-webkit-scrollbar-thumb {
    background: var(--surface);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--border);
}

.badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 600;
    margin: 4px 0;
}

.badge-success {
    background: rgba(16, 185, 129, 0.2);
    color: var(--success);
}

.badge-warning {
    background: rgba(245, 158, 11, 0.2);
    color: var(--warning);
}

.badge-danger {
    background: rgba(239, 68, 68, 0.2);
    color: var(--danger);
}
</style>
""", unsafe_allow_html=True)


# SESSION STATE


if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

if "policy_path" not in st.session_state:
    st.session_state.policy_path = None

if "policy_name" not in st.session_state:
    st.session_state.policy_name = None


# SIDEBAR

with st.sidebar:
    st.markdown("## GapBridge")
    st.markdown("NIST CSF 2024")
    
    st.divider()
    
    # Bind radio index to session_state.current_page
    PAGES = ["Home", "Upload & Analyze", "Results"]
    current_page_index = PAGES.index(st.session_state.current_page) if st.session_state.current_page in PAGES else 0
    
    page_selection = st.radio(
        "Navigate",
        PAGES,
        index=current_page_index,
        label_visibility="collapsed"
    )
    
    st.session_state.current_page = page_selection
    
    st.divider()
    
    with st.expander("NIST CSF Functions"):
        st.markdown("""
        **GOVERN** — Policy & governance  
        **PROTECT** — Safeguarding  
        **DETECT** — Detection  
        **RESPOND** — Response  
        **RECOVER** — Recovery
        """)
    
    with st.expander("How It Works"):
        st.markdown("""
        1. Upload policy document
        2. Analyze against 106 controls
        3. Get scoring & roadmap
        4. Download revised policy
        """)
    
    st.divider()
    
    st.markdown("**Privacy** All local  ")
    st.markdown("**Model** Mistral offline  ")
    st.markdown("**Time** 5-10 minutes  ")


# HOME PAGE


if st.session_state.current_page == "Home":
    st.markdown("# GapBridge")
    st.markdown("Professional NIST CSF 2024 Gap Analysis Platform")
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### What It Does
        
        Analyzes cybersecurity policies against 106 NIST CSF 2024 controls and identifies specific gaps.
        """)
    
    with col2:
        st.markdown("""
        ### Why Offline
        
        Your sensitive policies stay on your machine. No cloud uploads or external APIs.
        """)
    
    with col3:
        st.markdown("""
        ### What You Get
        
        Maturity scorecard, gap analysis, roadmap, and revised policy.
        """)
    
    st.divider()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Getting Started")
        st.markdown("""
        Upload a policy document to begin analysis:
        
        - Scan against all 106 NIST controls
        - Calculate maturity by function
        - Identify specific gaps
        - Create improvement roadmap
        - Generate compliant policy
        """)
    
    with col2:
        st.markdown("### Next Steps")
        if st.button("Start Analysis", use_container_width=True, type="primary", key="btn_home_start"):
            st.session_state.current_page = "Upload & Analyze"
            st.rerun()


# UPLOAD PAGE


elif st.session_state.current_page == "Upload & Analyze":
    st.markdown("# Upload & Analyze")
    
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.markdown("## Select Policy")
        
        policy_source = st.radio(
            "Choose source",
            ["Upload File", "Sample Policy"],
            label_visibility="collapsed"
        )
        
        if policy_source == "Upload File":
            uploaded_file = st.file_uploader(
                "Choose file",
                type=["txt", "pdf", "docx"],
                label_visibility="collapsed"
            )
            
            if uploaded_file:
                output_dir = os.path.join(os.path.dirname(__file__), "..", "output")
                os.makedirs(output_dir, exist_ok=True)
                st.session_state.policy_path = os.path.join(output_dir, f"_uploaded_{uploaded_file.name}")
                with open(st.session_state.policy_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.session_state.policy_name = os.path.splitext(uploaded_file.name)[0]
        
        else:
            samples = {
                "ISMS Policy": "isms_policy.txt",
                "Data Privacy": "data_privacy_policy.txt",
                "Patch Management": "patch_management_policy.txt",
                "Risk Management": "risk_management_policy.txt",
            }
            
            choice = st.selectbox(
                "Select sample",
                list(samples.keys()),
                label_visibility="collapsed"
            )
            
            st.session_state.policy_path = os.path.join(POLICY_DIR, samples[choice])
            st.session_state.policy_name = choice
    
    with col2:
        st.markdown("## Settings")
        st.markdown("""
        **Framework** NIST CSF 2024  
        **Controls** 106 total  
        **Processing** Local  
        **Model** Mistral  
        
        **Output**
        - Scorecard
        - Gap analysis
        - Roadmap
        - Revised policy
        """)
    
    st.divider()
    
    if st.session_state.policy_path:
        st.success(f"Selected: {st.session_state.policy_name}")
        
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col3:
            run_button = st.button(
                "Run Analysis",
                type="primary",
                use_container_width=True,
                key="btn_run_analysis"
            )
    else:
        st.info("Select a policy to begin")
        run_button = False
    
   
    # RUN ANALYSIS

    
    if run_button:
        progress_placeholder = st.empty()
        status_placeholder = st.empty()
        
        try:
            steps = [
                ("Loading policy and framework", 10),
                ("Detecting gaps", 30),
                ("Calculating scores", 50),
                ("Building roadmap", 65),
                ("Generating report", 80),
                ("Creating revised policy", 95),
            ]
            
            policy_text = None
            controls = None
            gaps = None
            scorecard = None
            roadmap = None
            report = None
            revised_policy = None
            
            for step_name, progress_value in steps:
                status_placeholder.markdown(f"**{step_name}...**")
                progress_placeholder.progress(progress_value / 100)
                
                if step_name == "Loading policy and framework":
                    policy_text = load_policy(st.session_state.policy_path)
                    controls = load_framework(FRAMEWORK_PATH)
                elif step_name == "Detecting gaps":
                    gaps = detect_gaps(policy_text, controls)
                elif step_name == "Calculating scores":
                    scorecard = calculate_scorecard(gaps)
                elif step_name == "Building roadmap":
                    roadmap = generate_roadmap(gaps, scorecard)
                elif step_name == "Generating report":
                    report = generate_report(gaps, scorecard)
                elif step_name == "Creating revised policy":
                    revised_policy = generate_revised_policy(policy_text, gaps)
            
            progress_placeholder.progress(100)
            status_placeholder.markdown("**Analysis Complete**")
            
            st.session_state.analysis_result = {
                "policy_name": st.session_state.policy_name,
                "scorecard": scorecard,
                "roadmap": roadmap,
                "report": report,
                "revised_policy": revised_policy,
                "breakdown": get_control_breakdown(gaps),
            }
            
            st.success("Analysis finished! Redirecting to results...")
            st.session_state.current_page = "Results"
            
            # Small delay 
            import time
            time.sleep(2)
            st.rerun()
        
        except Exception as e:
            st.error(f"Error during analysis: {str(e)}")
            import traceback
            st.error(traceback.format_exc())


# RESULTS PAGE

elif st.session_state.current_page == "Results":
    if st.session_state.analysis_result:
        result = st.session_state.analysis_result
        scorecard = result["scorecard"]
        
        st.markdown(f"# Results: {result['policy_name']}")
        
        
        # METRICS
       
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Overall Score", f"{scorecard['overall_pct']}%")
        
        with col2:
            st.metric("Weighted Score", f"{scorecard['weighted_pct']}%")
        
        with col3:
            gaps_count = sum(1 for c in result["breakdown"] if not c["met"])
            st.metric("Gaps Found", gaps_count)
        
        with col4:
            st.metric("Controls", len(result["breakdown"]))
        
        st.divider()
        
       
        # FUNCTION BREAKDOWN
     
        
        st.markdown("## NIST Functions")
        
        for fn, data in scorecard["by_function"].items():
            pct = data["pct"]
            met = data["met"]
            total = data["total"]
            
            col1, col2, col3, col4 = st.columns([1, 2, 1, 1])
            
            with col1:
                st.markdown(f"**{fn}**")
            
            with col2:
                st.progress(pct / 100)
            
            with col3:
                st.markdown(f"{met}/{total}")
            
            with col4:
                if pct >= 60:
                    st.markdown('<span class="badge badge-success">Strong</span>', unsafe_allow_html=True)
                elif pct >= 30:
                    st.markdown('<span class="badge badge-warning">Moderate</span>', unsafe_allow_html=True)
                else:
                    st.markdown('<span class="badge badge-danger">Weak</span>', unsafe_allow_html=True)
        
        st.divider()
        
        
        # TABS

        tab1, tab2, tab3, tab4 = st.tabs(["Breakdown", "Roadmap", "Report", "Policy"])
        
        with tab1:
            st.markdown("### Controls")
            
            show_gaps = st.checkbox("Gaps only", value=True)
            
            breakdown = result["breakdown"]
            if show_gaps:
                breakdown = [c for c in breakdown if not c["met"]]
            
            for control in breakdown:
                col1, col2 = st.columns([4, 1])
                
                with col1:
                    st.markdown(f"""
                    **{control.get('id')}** ({control.get('function', 'N/A')})
                    
                    {control.get('description', '')}
                    """)
                
                with col2:
                    if not control["met"]:
                        st.markdown('<span class="badge badge-danger">Gap</span>', unsafe_allow_html=True)
                    else:
                        st.markdown('<span class="badge badge-success">Met</span>', unsafe_allow_html=True)
        
        with tab2:
            st.markdown("### Timeline")
            
            roadmap = result["roadmap"]
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Short (0-3m)", len(roadmap.get("short_term_0_3_months", [])))
            with col2:
                st.metric("Mid (3-6m)", len(roadmap.get("mid_term_3_6_months", [])))
            with col3:
                st.metric("Long (6-12m)", len(roadmap.get("long_term_6_12_months", [])))
            
            # FIX #2: Properly format roadmap items
            st.markdown("**Short Term (0-3 months)**")
            for item in roadmap.get("short_term_0_3_months", []):
                if isinstance(item, dict):
                    st.markdown(f"- **{item.get('id', 'N/A')}** [{item.get('function', 'N/A')}] {item.get('description', '')}")
                else:
                    st.markdown(f"- {item}")
            
            st.markdown("**Mid Term (3-6 months)**")
            for item in roadmap.get("mid_term_3_6_months", []):
                if isinstance(item, dict):
                    st.markdown(f"- **{item.get('id', 'N/A')}** [{item.get('function', 'N/A')}] {item.get('description', '')}")
                else:
                    st.markdown(f"- {item}")
            
            st.markdown("**Long Term (6-12 months)**")
            for item in roadmap.get("long_term_6_12_months", []):
                if isinstance(item, dict):
                    st.markdown(f"- **{item.get('id', 'N/A')}** [{item.get('function', 'N/A')}] {item.get('description', '')}")
                else:
                    st.markdown(f"- {item}")
        
        with tab3:
            st.markdown("### Report")
            st.markdown(result["report"])
            
            st.divider()
            
            st.download_button(
                "Download Report",
                data=result["report"],
                file_name=f"{result['policy_name']}_report.md",
                mime="text/markdown"
            )
        
        with tab4:
            st.markdown("### Revised Policy")
            st.markdown(result["revised_policy"])
            
            st.divider()
            
            st.download_button(
                "Download Policy",
                data=result["revised_policy"],
                file_name=f"{result['policy_name']}_revised.md",
                mime="text/markdown"
            )
    
    else:
        st.info("No results yet. Run an analysis first.")
        
        if st.button("Go to Analysis", use_container_width=True):
            st.session_state.current_page = "Upload & Analyze"
            st.rerun()

st.divider()

st.markdown("""
**GapBridge** — NIST CSF 2024 Gap Analysis  
Professional offline security policy assessment

Local processing • No external APIs • No data transmission
""")

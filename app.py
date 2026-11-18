import streamlit as st
from analyzer import (
    evaluate_shannon_entropy, 
    inspect_structural_vulnerabilities, 
    cross_reference_breach_corpus
)
from generator import (
    generate_cryptographic_token, 
    construct_diceware_passphrase
)

# 1. Page Configuration
st.set_page_config(
    page_title="CipherGuard | Cryptographic Entropy Suite",
    page_icon="🛡️",
    layout="centered"
)

# 2. Custom CSS styling (Dark Terminal Aesthetic & Hide Anchor Links)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #e6edf3;
    }
    div[data-testid="stMetricValue"] {
        font-family: 'Courier New', monospace;
        color: #00ff9d;
    }
    .header-card {
        padding: 1.5rem;
        border-radius: 10px;
        background: linear-gradient(135deg, #161b22 0%, #0d1117 100%);
        border: 1px solid #30363d;
        margin-bottom: 1.5rem;
    }
    h1 a, h2 a, h3 a, h4 a {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Application Header Card
st.markdown("""
    <div class="header-card">
        <h2 style="margin:0; color:#58a6ff;">🛡️ CipherGuard Security Suite</h2>
        <p style="margin:0; color:#8b949e; font-size:0.9rem;">
            Advanced Shannon Entropy Auditing, Structural Heuristics & Token Generation
        </p>
    </div>
""", unsafe_allow_html=True)

# 4. Interface Navigation Tabs
tab_audit, tab_generator = st.tabs(["🔍 Credential Audit", "⚙️ Token Generation"])

# --- TAB 1: AUDIT ENGINE ---
with tab_audit:
    credential_input = st.text_input("Enter target credential:", type="password", placeholder="Input password or passphrase string...")

    if credential_input:
        entropy_score = evaluate_shannon_entropy(credential_input)
        vulnerabilities = inspect_structural_vulnerabilities(credential_input)
        is_compromised = cross_reference_breach_corpus(credential_input)

        # Strength progression scaling (normalized to 128-bit benchmark)
        entropy_ratio = min(entropy_score / 128.0, 1.0)
        st.write("**Entropy Density Gauge:**")
        st.progress(entropy_ratio)

        # Key Performance Indicators
        col_metric1, col_metric2, col_metric3 = st.columns(3)
        with col_metric1:
            st.metric("Shannon Entropy", f"{entropy_score} bits")
        with col_metric2:
            st.metric("String Length", f"{len(credential_input)} chars")
        with col_metric3:
            if is_compromised:
                security_status = "COMPROMISED"
            elif entropy_score >= 60 and not vulnerabilities:
                security_status = "SECURE"
            else:
                security_status = "SUBOPTIMAL"
            st.metric("Audit Status", security_status)

        st.divider()

        # Detailed Diagnostic Breakdown
        st.subheader("Diagnostic Evaluation")
        if is_compromised:
            st.error("🚨 **CRITICAL VULNERABILITY:** Matched against local common password corpus.")
        else:
            st.success("✅ **Corpus Verification:** Clear of local dictionary listings.")

        if vulnerabilities:
            st.warning("⚠️ **Heuristic Anomalies Flagged:**")
            for anomaly in vulnerabilities:
                st.markdown(f"- `{anomaly}`")
        else:
            st.success("✅ **Structural Heuristics:** No sequential repeats or predictable walks detected.")

# --- TAB 2: GENERATION ENGINE ---
with tab_generator:
    st.subheader("Cryptographic Token Synthesis")
    generation_mode = st.segmented_control("Synthesis Protocol", ["Random Character Token", "Diceware Passphrase"], default="Random Character Token")

    if generation_mode == "Random Character Token":
        token_length = st.slider("Token Length", min_value=8, max_value=32, value=16)
        if st.button("⚡ Synthesize Secure Token", use_container_width=True):
            generated_token = generate_cryptographic_token(length=token_length)
            st.code(generated_token, language="text")
            st.caption(f"Calculated Entropy: ~{evaluate_shannon_entropy(generated_token)} bits")
    else:
        word_quantity = st.slider("Passphrase Word Count", min_value=3, max_value=8, value=4)
        if st.button("⚡ Synthesize Passphrase", use_container_width=True):
            generated_phrase = construct_diceware_passphrase(word_count=word_quantity)
            st.code(generated_phrase, language="text")
            st.caption(f"Calculated Entropy: ~{evaluate_shannon_entropy(generated_phrase)} bits")
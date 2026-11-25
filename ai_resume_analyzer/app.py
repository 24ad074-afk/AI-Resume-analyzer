# ============================================================
# app.py  ←  RUN THIS FILE with:  streamlit run app.py
# PURPOSE: Main entry point for the AI Resume Analyzer app.
#          Builds the entire Streamlit UI and wires up all
#          analysis modules.
# ============================================================

import streamlit as st
import pandas as pd
import time

# ── Our custom modules ────────────────────────────────────────
from utils.text_extractor  import extract_text
from utils.skills_analyzer import (
    analyze_skills,
    calculate_ats_score,
    get_ats_label,
    generate_suggestions,
    get_strengths_weaknesses,
    extract_all_skills,
)
from utils.charts     import (
    ats_gauge, category_radar, skills_bar,
    ats_breakdown_bar, skill_match_donut,
)
from utils.pdf_report import generate_pdf_report
from job_roles        import JOB_ROLES

# ═══════════════════════════════════════════════════════════════
# PAGE CONFIG  (must be the very first Streamlit command)
# ═══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title = "AI Resume Analyzer",
    page_icon  = "🎯",
    layout     = "wide",
    initial_sidebar_state = "expanded",
)

# ═══════════════════════════════════════════════════════════════
# CUSTOM CSS — dark professional theme
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<style>
/* ── Global ────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ── Metric cards ──────────────────────────────────── */
.metric-card {
    background: linear-gradient(135deg, #1E2130 0%, #252840 100%);
    border: 1px solid rgba(108, 99, 255, 0.25);
    border-radius: 14px;
    padding: 20px 24px;
    margin-bottom: 12px;
    transition: box-shadow 0.2s;
}
.metric-card:hover { box-shadow: 0 4px 24px rgba(108, 99, 255, 0.18); }

.metric-title {
    color: #9E9CB8;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 4px;
}
.metric-value {
    color: #FAFAFA;
    font-size: 2rem;
    font-weight: 700;
    line-height: 1.1;
}
.metric-sub {
    color: #6C63FF;
    font-size: 0.82rem;
    margin-top: 4px;
}

/* ── Section headers ───────────────────────────────── */
.section-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 28px 0 14px;
    padding-bottom: 8px;
    border-bottom: 2px solid rgba(108, 99, 255, 0.35);
}
.section-header h2 {
    color: #FAFAFA;
    font-size: 1.2rem;
    font-weight: 700;
    margin: 0;
}

/* ── Skill chip ────────────────────────────────────── */
.skill-chip {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 500;
    margin: 3px;
    line-height: 1.6;
}
.chip-matched { background: rgba(0,200,83,0.15); color: #00C853; border: 1px solid rgba(0,200,83,0.4); }
.chip-missing { background: rgba(255,101,132,0.15); color: #FF6584; border: 1px solid rgba(255,101,132,0.4); }

/* ── Suggestion cards ──────────────────────────────── */
.suggestion-card {
    background: #1A1D2E;
    border-left: 3px solid #6C63FF;
    border-radius: 6px;
    padding: 10px 16px;
    margin: 6px 0;
    color: #DDD;
    font-size: 0.9rem;
    line-height: 1.55;
}

/* ── Strength / Weakness ────────────────────────────── */
.strength-item {
    background: rgba(0,200,83,0.08);
    border-left: 3px solid #00C853;
    border-radius: 6px;
    padding: 8px 14px;
    margin: 5px 0;
    color: #CFFFE6;
    font-size: 0.88rem;
}
.weakness-item {
    background: rgba(255,179,0,0.08);
    border-left: 3px solid #FFB300;
    border-radius: 6px;
    padding: 8px 14px;
    margin: 5px 0;
    color: #FFEFC2;
    font-size: 0.88rem;
}

/* ── Upload zone ───────────────────────────────────── */
.upload-zone {
    background: linear-gradient(135deg, #1A1D2E, #1E2130);
    border: 2px dashed rgba(108,99,255,0.45);
    border-radius: 16px;
    padding: 36px;
    text-align: center;
    margin-bottom: 16px;
}

/* ── Progress bar overrides ─────────────────────────── */
.stProgress > div > div { border-radius: 6px; }

/* ── Sidebar ─────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background: #10121F;
    border-right: 1px solid rgba(108,99,255,0.18);
}

/* ── Buttons ─────────────────────────────────────────── */
.stDownloadButton > button, .stButton > button {
    background: linear-gradient(135deg, #6C63FF, #8B5CF6);
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    padding: 10px 20px;
    transition: opacity 0.15s;
}
.stDownloadButton > button:hover, .stButton > button:hover { opacity: 0.88; }

/* ── Expander ─────────────────────────────────────────── */
[data-testid="stExpander"] {
    background: #1A1D2E;
    border: 1px solid rgba(108,99,255,0.18);
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("## 🎯 AI Resume Analyzer")
    st.markdown("*Powered by NLP · Built with Streamlit*")
    st.divider()

    # Candidate name (optional, used in PDF report)
    candidate_name = st.text_input(
        "Your Name (for report)",
        placeholder="e.g. Arjun Mehta",
        help="Optional — appears on the downloaded PDF report."
    )

    # Job role selector
    st.markdown("#### 🏢 Target Job Role")
    job_role = st.selectbox(
        "Select the role you are applying for",
        options=list(JOB_ROLES.keys()),
        help="The analyzer compares your resume skills against this role's requirements.",
    )

    st.divider()

    # Info block
    st.markdown("""
**How it works:**
1. Upload your resume (PDF/DOCX)
2. Select your target job role
3. Click **Analyze Resume**
4. Review your ATS score & suggestions
5. Download the PDF report
""")

    st.markdown("""
---
**ATS Score Bands:**
- 🟢 80–100 → Excellent
- 🔵 60–79  → Good
- 🟡 40–59  → Average
- 🔴 0–39   → Needs Work
""")


# ═══════════════════════════════════════════════════════════════
# HERO HEADER
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div style='text-align:center; padding: 28px 0 8px;'>
  <h1 style='color:#6C63FF; font-size:2.4rem; font-weight:800; margin:0;'>
    🎯 AI Resume Analyzer
  </h1>
  <p style='color:#9E9CB8; font-size:1.05rem; margin-top:8px;'>
    Upload your resume · Get your ATS score · Discover what's missing
  </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ═══════════════════════════════════════════════════════════════
# FILE UPLOAD
# ═══════════════════════════════════════════════════════════════
col_upload, col_info = st.columns([2, 1])

with col_upload:
    st.markdown('<div class="upload-zone">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "📁 Drop your resume here or click to browse",
        type=["pdf", "docx"],
        help="Supported formats: PDF and DOCX (Word document).",
        label_visibility="collapsed",
    )
    st.markdown(
        "<p style='color:#9E9CB8; font-size:0.82rem; margin-top:6px;'>"
        "Supported formats: <b>.pdf</b> and <b>.docx</b></p>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

with col_info:
    st.markdown("""
<div class="metric-card">
  <div class="metric-title">Analyzing for role</div>
  <div class="metric-value" style="font-size:1.1rem;">""" + job_role + """</div>
  <div class="metric-sub">Change role in sidebar →</div>
</div>
""", unsafe_allow_html=True)

    if not uploaded_file:
        st.info("👆 Upload a resume to begin analysis.")

# ═══════════════════════════════════════════════════════════════
# ANALYZE BUTTON + MAIN LOGIC
# ═══════════════════════════════════════════════════════════════
if uploaded_file:
    analyze_btn = st.button("🚀 Analyze Resume", use_container_width=True, type="primary")

    if analyze_btn:
        # ── Step 1: Extract Text ──────────────────────────────
        with st.spinner("📄 Extracting text from your resume…"):
            raw_text, clean_text = extract_text(uploaded_file)
            time.sleep(0.4)   # Small delay for UX feedback

        if not clean_text:
            st.error(
                "❌ Could not extract text from this file. "
                "Ensure the PDF has selectable text (not a scanned image) "
                "or try uploading a DOCX version."
            )
            st.stop()

        # ── Step 2: Analyze Skills ────────────────────────────
        with st.spinner("🔍 Analyzing skills against job requirements…"):
            skill_analysis = analyze_skills(clean_text, job_role)
            time.sleep(0.3)

        # ── Step 3: Calculate ATS Score ───────────────────────
        with st.spinner("📊 Calculating ATS score…"):
            ats_data  = calculate_ats_score(clean_text, job_role, skill_analysis)
            ats_label, ats_color = get_ats_label(ats_data["total"])
            time.sleep(0.3)

        # ── Step 4: Generate Suggestions ─────────────────────
        suggestions            = generate_suggestions(clean_text, job_role, ats_data, skill_analysis)
        strengths, weaknesses  = get_strengths_weaknesses(skill_analysis, ats_data)
        all_resume_skills      = extract_all_skills(clean_text)

        st.success("✅ Analysis complete! Scroll down to see your results.")

        # ══════════════════════════════════════════════════════
        # RESULTS SECTION
        # ══════════════════════════════════════════════════════
        st.divider()
        st.markdown("## 📊 Your Resume Analysis Results")

        # ── Top KPI row ───────────────────────────────────────
        k1, k2, k3, k4 = st.columns(4)

        with k1:
            st.markdown(f"""
<div class="metric-card">
  <div class="metric-title">ATS Score</div>
  <div class="metric-value" style="color:{ats_color};">{ats_data['total']}<span style="font-size:1rem;">/100</span></div>
  <div class="metric-sub">{ats_label}</div>
</div>""", unsafe_allow_html=True)

        with k2:
            match_pct = round(skill_analysis["total_matched"] / max(skill_analysis["total_required"], 1) * 100, 1)
            st.markdown(f"""
<div class="metric-card">
  <div class="metric-title">Skills Matched</div>
  <div class="metric-value">{skill_analysis['total_matched']}<span style="font-size:1rem;">/{skill_analysis['total_required']}</span></div>
  <div class="metric-sub">{match_pct}% coverage</div>
</div>""", unsafe_allow_html=True)

        with k3:
            st.markdown(f"""
<div class="metric-card">
  <div class="metric-title">Sections Found</div>
  <div class="metric-value">{len(ats_data['sections_found'])}</div>
  <div class="metric-sub">of {12} standard sections</div>
</div>""", unsafe_allow_html=True)

        with k4:
            st.markdown(f"""
<div class="metric-card">
  <div class="metric-title">Action Verbs</div>
  <div class="metric-value">{len(ats_data['verbs_found'])}</div>
  <div class="metric-sub">impact-driven phrases</div>
</div>""", unsafe_allow_html=True)

        # ── ATS Gauge + Donut ──────────────────────────────────
        st.markdown('<div class="section-header"><h2>📈 ATS Score Overview</h2></div>', unsafe_allow_html=True)
        g1, g2, g3 = st.columns([1.3, 1, 1.7])

        with g1:
            st.plotly_chart(
                ats_gauge(ats_data["total"], ats_label, ats_color),
                use_container_width=True, config={"displayModeBar": False}
            )

        with g2:
            st.plotly_chart(
                skill_match_donut(skill_analysis["total_matched"], skill_analysis["total_required"]),
                use_container_width=True, config={"displayModeBar": False}
            )

        with g3:
            st.markdown("**Score Breakdown**")
            st.plotly_chart(
                ats_breakdown_bar(ats_data),
                use_container_width=True, config={"displayModeBar": False}
            )
            # Mini progress bars for each component
            components = {
                "Skill Match": (ats_data["skill_score"],     60),
                "Structure"  : (ats_data["completeness_score"], 15),
                "Action Verbs": (ats_data["verb_score"],     15),
                "Keywords"   : (ats_data["density_score"],   10),
            }
            for name, (val, max_val) in components.items():
                pct = int(val / max_val * 100)
                st.markdown(f"<small style='color:#9E9CB8'>{name}: {val:.1f}/{max_val}</small>", unsafe_allow_html=True)
                st.progress(pct)

        # ── Radar + Bar ────────────────────────────────────────
        st.markdown('<div class="section-header"><h2>🎯 Skill Category Breakdown</h2></div>', unsafe_allow_html=True)
        r1, r2 = st.columns(2)

        with r1:
            st.plotly_chart(
                category_radar(skill_analysis["category_scores"]),
                use_container_width=True, config={"displayModeBar": False}
            )

        with r2:
            st.plotly_chart(
                skills_bar(skill_analysis["category_scores"]),
                use_container_width=True, config={"displayModeBar": False}
            )

        # ── Matched & Missing Skills ───────────────────────────
        st.markdown('<div class="section-header"><h2>✅ Matched Skills</h2></div>', unsafe_allow_html=True)
        for category, skills in skill_analysis["matched_skills"].items():
            if skills:
                with st.expander(f"**{category}** — {len(skills)} skills matched", expanded=False):
                    chips = "".join(
                        f'<span class="skill-chip chip-matched">{s}</span>'
                        for s in skills
                    )
                    st.markdown(chips, unsafe_allow_html=True)

        st.markdown('<div class="section-header"><h2>❌ Missing Skills</h2></div>', unsafe_allow_html=True)
        for category, skills in skill_analysis["missing_skills"].items():
            if skills:
                with st.expander(f"**{category}** — {len(skills)} skills to add", expanded=False):
                    chips = "".join(
                        f'<span class="skill-chip chip-missing">{s}</span>'
                        for s in skills
                    )
                    st.markdown(chips, unsafe_allow_html=True)

        # ── Strengths & Weaknesses ─────────────────────────────
        st.markdown('<div class="section-header"><h2>💪 Strengths & Weaknesses</h2></div>', unsafe_allow_html=True)
        sw1, sw2 = st.columns(2)

        with sw1:
            st.markdown("#### ✅ Strengths")
            if strengths:
                for s in strengths:
                    clean_s = s.replace("**", "").replace("*", "").replace("✅ ", "")
                    st.markdown(f'<div class="strength-item">✅ {clean_s}</div>', unsafe_allow_html=True)
            else:
                st.info("Keep adding skills — your strengths will appear here!")

        with sw2:
            st.markdown("#### ⚠️ Areas to Improve")
            if weaknesses:
                for w in weaknesses:
                    clean_w = w.replace("**", "").replace("*", "").replace("⚠️ ", "")
                    st.markdown(f'<div class="weakness-item">⚠️ {clean_w}</div>', unsafe_allow_html=True)
            else:
                st.success("No major weaknesses detected. Great work!")

        # ── Improvement Suggestions ────────────────────────────
        st.markdown('<div class="section-header"><h2>💡 Improvement Suggestions</h2></div>', unsafe_allow_html=True)
        for i, tip in enumerate(suggestions, 1):
            # Strip markdown bold for clean display
            clean_tip = tip.replace("**", "<b>", 1).replace("**", "</b>", 1)
            st.markdown(
                f'<div class="suggestion-card"><b>{i}.</b> {clean_tip}</div>',
                unsafe_allow_html=True,
            )

        # ── Keyword & Section Analysis ─────────────────────────
        st.markdown('<div class="section-header"><h2>🔑 Keyword & Structure Analysis</h2></div>', unsafe_allow_html=True)
        ka1, ka2, ka3 = st.columns(3)

        with ka1:
            st.markdown("**All Skills Detected in Resume**")
            if all_resume_skills:
                chips = "".join(
                    f'<span class="skill-chip chip-matched">{s}</span>'
                    for s in all_resume_skills[:30]
                )
                st.markdown(chips, unsafe_allow_html=True)
            else:
                st.warning("No recognizable tech skills detected.")

        with ka2:
            st.markdown("**Resume Sections Detected**")
            for sec in ["summary","education","experience","skills",
                         "projects","certifications","achievements"]:
                icon  = "✅" if sec in ats_data["sections_found"] else "❌"
                color = "#00C853" if sec in ats_data["sections_found"] else "#E53935"
                st.markdown(
                    f"<span style='color:{color};'>{icon} {sec.capitalize()}</span>",
                    unsafe_allow_html=True,
                )

        with ka3:
            st.markdown("**Action Verbs Found**")
            if ats_data["verbs_found"]:
                chips = "".join(
                    f'<span class="skill-chip chip-matched">{v}</span>'
                    for v in ats_data["verbs_found"]
                )
                st.markdown(chips, unsafe_allow_html=True)
            else:
                st.warning("No action verbs detected. Add verbs like: built, led, improved…")

        # ── Raw Text Preview ───────────────────────────────────
        with st.expander("📄 View Extracted Resume Text", expanded=False):
            st.text_area(
                "Raw extracted text (first 2000 characters):",
                raw_text[:2000] if raw_text else "No text extracted.",
                height=220,
            )

        # ── Download PDF Report ────────────────────────────────
        st.divider()
        st.markdown("### 📥 Download Your Analysis Report")

        pdf_bytes = generate_pdf_report(
            candidate_name = candidate_name or "Candidate",
            job_role       = job_role,
            ats_data       = ats_data,
            ats_label      = ats_label,
            skill_analysis = skill_analysis,
            suggestions    = suggestions,
            strengths      = strengths,
            weaknesses     = weaknesses,
        )

        st.download_button(
            label     = "⬇️ Download PDF Report",
            data      = pdf_bytes,
            file_name = f"resume_analysis_{job_role.lower().replace(' ', '_')}.pdf",
            mime      = "application/pdf",
            use_container_width=True,
        )

        st.caption(
            "The report includes your ATS score, matched/missing skills, "
            "strengths, weaknesses, and all improvement suggestions."
        )

# ═══════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════
st.divider()
st.markdown("""
<div style='text-align:center; color:#4A4A6A; font-size:0.8rem; padding:10px 0 20px;'>
  Built with ❤️ using Python · Streamlit · Plotly · FPDF2<br>
  AI Resume Analyzer · Open Source Project for Learning
</div>
""", unsafe_allow_html=True)

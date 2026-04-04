import streamlit as st
import pandas as pd
import os
from datetime import datetime
import plotly.express as px





st.set_page_config(
    page_title="ECS Stakeholder Platform",
    layout="wide"
)













# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------
st.set_page_config(
    page_title="ECS Stakeholder Learning and Engagement Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------
# GLOBAL GREEN THEME
# -------------------------------------------------------
st.markdown("""
<style>
:root {
    --ecs-dark: #233F05;
    --ecs-primary: #3F6F45;
    --ecs-soft: #86A392;
    --ecs-light: #AEBCB3;
    --ecs-bg: #B7BDB6;
    --ecs-panel: #F6F8F4;
    --ecs-white: #FBFCFA;
    --ecs-text: #2F3A31;
    --ecs-muted: #5D6A61;
    --ecs-border: #C8D2CA;
    --ecs-shadow: rgba(35, 63, 5, 0.08);
    --ecs-shadow-strong: rgba(35, 63, 5, 0.14);
}

/* -------------------- APP BACKGROUND -------------------- */
.stApp {
    background: linear-gradient(180deg, #F5F7F2 0%, #EDF2EC 100%);
    color: var(--ecs-text);
}

.block-container {
    padding-top: 1.8rem;
    padding-bottom: 2rem;
    max-width: 1280px;
}

/* -------------------- SIDEBAR -------------------- */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #F4F7F2 0%, #E8EEE8 100%);
    border-right: 1px solid var(--ecs-border);
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h4,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] div {
    color: var(--ecs-text);
}

/* -------------------- TYPOGRAPHY -------------------- */
h1, h2, h3, h4 {
    color: var(--ecs-dark) !important;
    letter-spacing: -0.01em;
}

p, li, label, div {
    color: var(--ecs-text);
}

.section-heading {
    font-size: 1.65rem;
    font-weight: 800;
    color: var(--ecs-dark);
    margin-top: 0.4rem;
    margin-bottom: 0.9rem;
}

.section-subtext {
    color: var(--ecs-muted);
    font-size: 1rem;
    line-height: 1.75;
    margin-bottom: 1.1rem;
    max-width: 860px;
}

/* -------------------- TOP STRIP -------------------- */
.top-strip {
    height: 10px;
    width: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #233F05 0%, #3F6F45 55%, #86A392 100%);
    margin-bottom: 1rem;
}

/* -------------------- HERO / PAGE HEADERS -------------------- */
.hero-wrap {
    position: relative;
    background:
        linear-gradient(90deg, rgba(35,63,5,0.86) 0%, rgba(63,111,69,0.78) 45%, rgba(134,163,146,0.58) 100%),
        url("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1600&q=80");
    background-size: cover;
    background-position: center;
    border-radius: 28px;
    padding: 3.2rem 3rem 2.8rem 3rem;
    min-height: 330px;
    box-shadow: 0 18px 40px var(--ecs-shadow-strong);
    overflow: hidden;
    margin-bottom: 1.2rem;
}

.page-hero,
.sim-hero {
    background: linear-gradient(135deg, #FBFCFA 0%, #E7EEE7 100%);
    border: 1px solid var(--ecs-border);
    border-radius: 24px;
    padding: 1.6rem 1.6rem 1.3rem 1.6rem;
    box-shadow: 0 12px 28px var(--ecs-shadow);
    margin-bottom: 1rem;
}

.hero-kicker,
.page-kicker,
.sim-kicker,
.mini-tag,
.card-tag,
.sim-card-tag,
.info-feature-tag,
.resource-meta,
.news-type {
    display: inline-block;
    background: #E4ECE5;
    color: var(--ecs-primary);
    border-radius: 999px;
    padding: 0.28rem 0.72rem;
    font-size: 0.8rem;
    font-weight: 700;
    margin-bottom: 0.75rem;
    letter-spacing: 0.01em;
}

.hero-title {
    color: #FFFFFF;
    font-size: 3rem;
    font-weight: 800;
    line-height: 1.08;
    max-width: 760px;
    margin-bottom: 0.9rem;
}

.page-title,
.sim-title {
    font-size: 2rem;
    font-weight: 800;
    color: var(--ecs-dark);
    margin-bottom: 0.45rem;
    line-height: 1.2;
}

.hero-subtitle {
    color: rgba(255,255,255,0.96);
    font-size: 1.08rem;
    line-height: 1.8;
    max-width: 800px;
}

.page-subtitle,
.sim-subtitle {
    color: var(--ecs-muted);
    font-size: 1rem;
    line-height: 1.75;
    max-width: 920px;
}

/* -------------------- NOTES / HIGHLIGHTS -------------------- */
.notice-box,
.highlight-box,
.insight-box,
.page-note,
.sim-note,
.sim-result-box {
    background: linear-gradient(135deg, #EEF4EF 0%, #DEE8E0 100%);
    border-left: 6px solid var(--ecs-primary);
    color: var(--ecs-dark);
    padding: 1rem 1.1rem;
    border-radius: 16px;
    margin: 0.8rem 0 1rem 0;
    box-shadow: 0 8px 20px rgba(63,111,69,0.06);
    line-height: 1.7;
}

/* -------------------- GENERAL CARD SYSTEM -------------------- */
.portal-card,
.section-card,
.news-card,
.resource-card,
.quick-link-card,
.info-feature-card,
.engage-card,
.phase-card,
.sim-card,
.sim-flow-box,
.sim-step-card,
.capacity-highlight-card,
.metric-shell {
    background: linear-gradient(180deg, #FFFFFF 0%, #F6F9F5 100%);
    border: 1px solid var(--ecs-border);
    border-radius: 18px;
    padding: 1rem;
    box-shadow: 0 8px 22px var(--ecs-shadow);
    margin-bottom: 1rem;
}

.portal-card:hover,
.news-card:hover,
.resource-card:hover,
.quick-link-card:hover,
.info-feature-card:hover,
.engage-card:hover,
.phase-card:hover,
.sim-card:hover,
.sim-flow-box:hover,
.sim-step-card:hover,
.capacity-highlight-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 14px 30px var(--ecs-shadow-strong);
}

.card-title,
.news-title,
.resource-title,
.info-feature-title,
.engage-title,
.phase-title,
.sim-card-title,
.sim-flow-title,
.sim-step-title,
.capacity-highlight-title {
    color: var(--ecs-dark);
    font-size: 1.08rem;
    font-weight: 800;
    margin-bottom: 0.45rem;
    line-height: 1.35;
}

.card-text,
.news-text,
.resource-text,
.info-feature-text,
.engage-text,
.phase-text,
.sim-card-text,
.sim-flow-text,
.sim-step-text,
.capacity-highlight-text {
    color: var(--ecs-muted);
    font-size: 0.95rem;
    line-height: 1.7;
}

/* -------------------- SPECIAL CARDS -------------------- */
.portal-card {
    min-height: 240px;
    padding: 1.15rem 1.15rem 1rem 1.15rem;
}

.news-card {
    overflow: hidden;
    padding: 0;
}

.news-body {
    padding: 1rem 1.1rem 1rem 1.1rem;
}

.news-image {
    width: 100%;
    height: 180px;
    object-fit: cover;
    display: block;
}

.resource-card {
    min-height: 150px;
    padding: 1rem 1rem 0.9rem 1rem;
}

.quick-link-card {
    background: linear-gradient(135deg, #3F6F45 0%, #233F05 100%);
    color: white;
    min-height: 150px;
    box-shadow: 0 12px 28px rgba(35,63,5,0.18);
}

.quick-link-card h4 {
    color: white;
    font-size: 1.08rem;
    font-weight: 800;
    margin-bottom: 0.45rem;
}

.quick-link-card p {
    color: rgba(255,255,255,0.96);
    line-height: 1.7;
    font-size: 0.95rem;
}

.info-feature-card {
    min-height: 185px;
}

.engage-card {
    min-height: 175px;
}

.phase-card {
    min-height: 210px;
}

.sim-card,
.capacity-highlight-card {
    min-height: 180px;
}

.sim-flow-box,
.sim-step-card {
    min-height: 150px;
}

/* -------------------- BUTTONS -------------------- */
.stButton > button {
    background: linear-gradient(135deg, #3F6F45 0%, #233F05 100%);
    color: white !important;
    border: none;
    border-radius: 12px;
    padding: 0.58rem 1rem;
    font-weight: 700;
    box-shadow: 0 8px 18px rgba(35,63,5,0.15);
}

.stButton > button:hover {
    background: linear-gradient(135deg, #233F05 0%, #3F6F45 100%);
    color: white !important;
}

/* -------------------- INPUTS -------------------- */
.stTextInput input,
.stNumberInput input,
.stTextArea textarea,
div[data-baseweb="select"] > div,
.stDateInput input {
    border-radius: 12px !important;
    border: 1px solid var(--ecs-border) !important;
    background: #FCFDFC !important;
}

.stSlider [data-baseweb="slider"] div {
    color: var(--ecs-primary) !important;
}

/* -------------------- TABS -------------------- */
.stTabs [data-baseweb="tab-list"] {
    gap: 0.4rem;
}

.stTabs [data-baseweb="tab"] {
    color: var(--ecs-dark);
    font-weight: 600;
    border-radius: 10px 10px 0 0;
    padding-left: 0.9rem;
    padding-right: 0.9rem;
}

.stTabs [aria-selected="true"] {
    color: var(--ecs-primary) !important;
    border-bottom: 3px solid var(--ecs-primary) !important;
}

/* -------------------- METRICS -------------------- */
[data-testid="stMetric"] {
    background: linear-gradient(180deg, #FFFFFF 0%, #F6F9F5 100%);
    border: 1px solid var(--ecs-border);
    border-radius: 18px;
    padding: 0.8rem 0.9rem;
    box-shadow: 0 8px 20px var(--ecs-shadow);
}

[data-testid="stMetricLabel"] {
    font-size: 0.88rem !important;
    color: var(--ecs-muted) !important;
}

[data-testid="stMetricValue"] {
    font-size: 1.1rem !important;
    line-height: 1.2 !important;
    font-weight: 700 !important;
    color: var(--ecs-dark) !important;
}

/* -------------------- TABLES / DATAFRAMES -------------------- */
[data-testid="stDataFrame"] {
    border: 1px solid var(--ecs-border);
    border-radius: 14px;
    overflow: hidden;
}

/* -------------------- EXPANDERS -------------------- */
details {
    border: 1px solid var(--ecs-border);
    border-radius: 14px;
    background: #FBFCFA;
}

/* -------------------- CODE BLOCKS -------------------- */
code {
    color: var(--ecs-dark);
}

/* -------------------- SMALL POLISH -------------------- */
hr {
    border: none;
    border-top: 1px solid var(--ecs-border);
    margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)

















# -------------------------------------------------------
# FILES
# -------------------------------------------------------
FEEDBACK_FILE = "feedback_submissions.xlsx"

def save_to_excel(file_name, new_row):
    new_df = pd.DataFrame([new_row])

    if os.path.exists(file_name):
        existing_df = pd.read_excel(file_name)
        updated_df = pd.concat([existing_df, new_df], ignore_index=True)
    else:
        updated_df = new_df

    updated_df.to_excel(file_name, index=False)

def load_excel(file_name):
    if os.path.exists(file_name):
        return pd.read_excel(file_name)
    return pd.DataFrame()













# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------
st.sidebar.markdown("## ECS Platform")
st.sidebar.caption("Stakeholder-facing learning and engagement platform for ECS")
st.sidebar.markdown("---")

user_role = st.sidebar.selectbox(
    "View as",
    ["Administrator", "Public User", "Industry Stakeholder", "Policy Stakeholder", "Facilitator"],
)

st.sidebar.markdown("---")

module = st.sidebar.radio(
    "Select Section",
    [
        "Home",
        "Information & Awareness",
        "Stakeholder Engagement",
        "Capacity Building & Learning",
        "Simulation & Demonstration",
    ],
)












# -------------------------------------------------------
# GLOBAL INTRO
# -------------------------------------------------------
st.info(
    "This platform is an illustrative prototype designed to support stakeholder engagement, "
    "capacity building, awareness, consultation, and learning for the Emissions Compliance System (ECS)."
)















# -------------------------------------------------------
# HOME
# -------------------------------------------------------
if module == "Home":

    st.markdown('<div class="top-strip"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-kicker">ECS Knowledge Hub</div>
        <div class="hero-title">ECS Stakeholder Learning and Engagement Platform</div>
        <div class="hero-subtitle">
            A stakeholder-facing digital platform prototype designed to support awareness, consultation,
            capacity building, and interactive learning for the Emissions Compliance System (ECS).
            The platform brings together policy communication, structured engagement, practical guidance,
            and simulation-based learning in one integrated interface.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="notice-box">
        <b>Illustrative prototype only.</b> This platform is intended for engagement, awareness,
        consultation, and learning purposes. It does not serve as a regulatory compliance system,
        enforcement mechanism, or allowance registry.
    </div>
    """, unsafe_allow_html=True)




if module == "Home":

    st.markdown('<div class="top-strip"></div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="portal-card">
        <div class="card-tag">Structure</div>
        <div class="card-title">4 Core Sections</div>
        <div class="card-text">Information, engagement, learning, and simulation modules.</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="portal-card">
        <div class="card-tag">Focus</div>
        <div class="card-title">Stakeholder Awareness</div>
        <div class="card-text">Providing accessible explanations of ECS policy and system design.</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="portal-card">
        <div class="card-tag">Engagement</div>
        <div class="card-title">Consultation Channels</div>
        <div class="card-text">Supporting dialogue, workshops, and structured stakeholder feedback.</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="portal-card">
        <div class="card-tag">Learning</div>
        <div class="card-title">Simulation Lab</div>
        <div class="card-text">Interactive exercises to explore ETS market dynamics and compliance.</div>
        </div>
        """, unsafe_allow_html=True)












    st.markdown('<div class="section-heading">Platform Overview</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-subtext">
        This homepage is designed as a portal landing page. It provides
        a brief introduction to the platform, highlights recent updates, surfaces featured knowledge resources,
        and gives stakeholders quick access to the core ECS learning areas.
    </div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------
    # FEATURED UPDATES
    # ---------------------------------------------------
    st.markdown('<div class="section-heading">Featured Updates</div>', unsafe_allow_html=True)
    news_col1, news_col2, news_col3 = st.columns(3)

    with news_col1:
        st.markdown("""
        <div class="news-card">
            <img class="news-image" src="https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w=1200&q=80">
            <div class="news-body">
                <div class="news-type">News</div>
                <div class="news-title">Illustrative ECS stakeholder workshop series launched</div>
                <div class="news-text">
                    A series of introductory stakeholder sessions may support awareness-building,
                    consultation, and early dialogue on ECS design and implementation considerations.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with news_col2:
        st.markdown("""
        <div class="news-card">
            <img class="news-image" src="https://images.unsplash.com/photo-1466611653911-95081537e5b7?auto=format&fit=crop&w=1200&q=80">
            <div class="news-body">
                 <div class="news-type">Publication</div>
                 <div class="news-title">New introductory note on ECS concepts and stakeholder roles</div>
                 <div class="news-text">
                A concise knowledge note may help stakeholders understand system purpose,
                key terminology, and how different institutions may interact with the ECS.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    


    with news_col3:
        st.markdown("""
        <div class="news-card">
            <img class="news-image" src="https://images.unsplash.com/photo-1466611653911-95081537e5b7?auto=format&fit=crop&w=1200&q=80">
            <div class="news-body">
                <div class="news-type">Learning Lab</div>
                <div class="news-title">Interactive simulation exercises support practical understanding</div>
                <div class="news-text">
                    The ECS Learning Simulation Lab enables stakeholders to explore market behavior,
                    sector pathways, and design choices through guided exercises.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ---------------------------------------------------
    # QUICK ACCESS + RESOURCES
    # ---------------------------------------------------
    left_col, right_col = st.columns([1.05, 1.35])

    with left_col:
        st.markdown('<div class="section-heading">Quick Access</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="quick-link-card">
            <h4>Information & Awareness</h4>
            <p>
                Access ECS overview materials, system logic, terminology, roadmap content,
                FAQs, and supporting policy guidance.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="quick-link-card">
            <h4>Stakeholder Engagement</h4>
            <p>
                Explore consultation papers, feedback channels, workshop activities,
                engagement updates, and meeting-related content.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="quick-link-card">
            <h4>Capacity Building & Learning</h4>
            <p>
                Review learning modules, recorded workshops, MRV guidance,
                case studies, and practical stakeholder resources.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="quick-link-card">
            <h4>ECS Learning Simulation Lab</h4>
            <p>
                Interact with guided exercises on firm strategy, trading dynamics,
                price pathways, market balance, and design choices.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with right_col:
        st.markdown('<div class="section-heading">Featured Knowledge Resources</div>', unsafe_allow_html=True)

        r1, r2 = st.columns(2)

        with r1:
            st.markdown("""
            <div class="resource-card">
                <div class="resource-meta">Overview Note</div>
                <div class="resource-title">What is the ECS?</div>
                <div class="resource-text">
                    A brief introductory note explaining the purpose of the ECS, why it matters,
                    and how stakeholders may engage with it.
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="resource-card">
                <div class="resource-meta">Guidance</div>
                <div class="resource-title">Introduction to MRV</div>
                <div class="resource-text">
                    A practical explainer on monitoring, reporting, and verification concepts
                    to support stakeholder readiness and understanding.
                </div>
            </div>
            """, unsafe_allow_html=True)

        with r2:
            st.markdown("""
            <div class="resource-card">
                <div class="resource-meta">Consultation</div>
                <div class="resource-title">Stakeholder Engagement Note</div>
                <div class="resource-text">
                    An overview of how consultation, workshops, and structured dialogue
                    can support ECS development and implementation.
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="resource-card">
                <div class="resource-meta">Simulation Lab</div>
                <div class="resource-title">Interactive Learning Exercises</div>
                <div class="resource-text">
                    A set of guided simulation exercises showing how market logic,
                    firm behavior, and policy design choices may interact.
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ---------------------------------------------------
    # OPTIONAL EVENTS / ANNOUNCEMENTS
    # ---------------------------------------------------
    st.markdown('<div class="section-heading">Upcoming Activities</div>', unsafe_allow_html=True)

    activities_df = pd.DataFrame(
        {
            "Activity": [
                "Illustrative stakeholder roundtable",
                "Introductory ECS webinar",
                "MRV awareness session",
                "Simulation lab demonstration",
            ],
            "Purpose": [
                "Support structured dialogue on ECS design and stakeholder perspectives.",
                "Provide an accessible introduction to ECS concepts and terminology.",
                "Build awareness of reporting and verification basics.",
                "Demonstrate how simulation-based learning can support stakeholder understanding.",
            ],
            "Illustrative Timing": [
                "Q2 2026",
                "Q2 2026",
                "Q3 2026",
                "Q3 2026",
            ],
        }
    )
    st.dataframe(activities_df, use_container_width=True, hide_index=True)











# -------------------------------------------------------
# INFORMATION & AWARENESS
# -------------------------------------------------------
elif module == "Information & Awareness":
    st.markdown("""
    <div class="page-hero">
        <div class="page-kicker">Information & Awareness</div>
        <div class="page-title">Understand the ECS and access core stakeholder resources</div>
        <div class="page-subtitle">
            This section is designed to support stakeholder awareness, foundational understanding,
            and access to introductory ECS materials, updates, and learning resources.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="page-note">
        <b>Illustrative prototype only.</b> This section is designed for awareness, learning, and engagement.
        It does not function as an MRV submission portal, registry, or operational compliance system.
    </div>
    """, unsafe_allow_html=True)

    top1, top2, top3 = st.columns([1.4, 1.4, 1.2])

    with top1:
        st.markdown("""
        <div class="info-feature-card">
            <div class="info-feature-tag">About ECS</div>
            <div class="info-feature-title">What stakeholders should understand first</div>
            <div class="info-feature-text">
                ECS is presented here as an illustrative policy framework that can support emissions transparency,
                stakeholder readiness, and structured policy development.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with top2:
        st.markdown("""
        <div class="info-feature-card">
            <div class="info-feature-tag">Knowledge Hub</div>
            <div class="info-feature-title">Guidance, FAQs, and introductory materials</div>
            <div class="info-feature-text">
                Stakeholders can access simple explanations, key concepts, introductory notes,
                workshop materials, and featured publications in one place.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with top3:
        st.markdown("""
        <div class="info-feature-card">
            <div class="info-feature-tag">Related Systems</div>
            <div class="info-feature-title">Learn where MRV and registry tools fit</div>
            <div class="info-feature-text">
                This page explains related operational systems at a high level and shows
                illustrative external links, without turning the platform into those systems.
            </div>
        </div>
        """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "About ECS",
            "How It Works",
            "Key Concepts",
            "Resources & FAQs",
            "Related Systems",
        ]
    )

    with tab1:
        st.markdown("### What is the ECS?")
        st.write(
            "The Emissions Compliance System (ECS) is presented in this prototype as an illustrative policy framework "
            "that can support emissions transparency, structured stakeholder participation, and clearer understanding "
            "of how emissions-related obligations may be organized."
        )

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Why ECS may be introduced**")
            st.write("- Improve emissions transparency")
            st.write("- Support more informed climate and industrial policy")
            st.write("- Create clearer incentives for emissions reduction")
            st.write("- Strengthen long-term planning and system readiness")

        with c2:
            st.markdown("**Illustrative stakeholder groups**")
            st.write("- Industry participants")
            st.write("- Government and policy institutions")
            st.write("- Technical experts and verifiers")
            st.write("- Researchers and wider stakeholders")

        st.markdown("### Why this page matters")
        st.info(
            "This page is intended to serve as a stakeholder-facing information portal, helping users understand "
            "the ECS before they engage with consultations, learning modules, or simulation exercises."
        )

    with tab2:
        st.markdown("### How the ECS Works")
        st.write(
            "This simplified view explains ECS logic without going into regulator-only operational detail."
        )

        process_df = pd.DataFrame(
            {
                "Step": [
                    "System design",
                    "Stakeholder consultation",
                    "Monitoring and reporting concepts",
                    "Review and reconciliation",
                    "Implementation and refinement",
                ],
                "Description": [
                    "Authorities define the broad policy structure and system objectives.",
                    "Stakeholders provide feedback through workshops, consultations, and dialogue channels.",
                    "Participants learn how emissions-related information may be monitored and reported.",
                    "Reported information is reviewed and linked to the broader compliance cycle.",
                    "The system evolves through phased implementation, engagement, and improvement.",
                ],
            }
        )
        st.dataframe(process_df, use_container_width=True, hide_index=True)

    with tab3:
        st.markdown("### Key Concepts and Terminology")

        concepts = {
            "Emissions Compliance System (ECS)": "An illustrative system used here to explain how emissions-related obligations and stakeholder roles may be structured.",
            "Cap": "A policy parameter that limits covered emissions or activity.",
            "Allowance": "An illustrative unit associated with emissions within the policy framework.",
            "Carbon Price": "A value associated with emissions that can shape incentives and decisions.",
            "Allocation": "How allowances may be distributed or made available under the system.",
            "MRV": "Monitoring, Reporting, and Verification of emissions-related information.",
            "Stakeholder Engagement": "Structured dialogue with affected and interested parties during policy development and implementation.",
            "Trading": "The exchange of allowances in systems that permit market transactions.",
        }

        for term, definition in concepts.items():
            with st.expander(term):
                st.write(definition)

    with tab4:
        st.markdown("### Featured Resources")
        r1, r2 = st.columns(2)

        with r1:
            st.markdown("""
            <div class="resource-card">
                <div class="resource-meta">Overview</div>
                <div class="resource-title">ECS Overview Note</div>
                <div class="resource-text">A short note introducing ECS objectives, structure, and stakeholder relevance.</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="resource-card">
                <div class="resource-meta">Roadmap</div>
                <div class="resource-title">Introductory ECS Roadmap</div>
                <div class="resource-text">A simple overview of the design, pilot, and operational readiness journey.</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="resource-card">
                <div class="resource-meta">FAQ</div>
                <div class="resource-title">Illustrative ECS FAQ</div>
                <div class="resource-text">Answers to common stakeholder questions about purpose, structure, and learning pathways.</div>
            </div>
            """, unsafe_allow_html=True)

        with r2:
            st.markdown("""
            <div class="resource-card">
                <div class="resource-meta">Consultation</div>
                <div class="resource-title">Stakeholder Consultation Note</div>
                <div class="resource-text">An overview of how stakeholder participation and consultation can support ECS design.</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="resource-card">
                <div class="resource-meta">Guidance</div>
                <div class="resource-title">MRV Introductory Guide</div>
                <div class="resource-text">A simple explainer on MRV concepts for awareness and readiness purposes.</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="resource-card">
                <div class="resource-meta">Workshops</div>
                <div class="resource-title">Workshop Summary Pack</div>
                <div class="resource-text">Illustrative workshop materials, presentation summaries, and learning takeaways.</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("### FAQs")
        faq_items = {
            "What is the purpose of this platform?":
                "This platform is for stakeholder engagement, awareness, consultation, and learning.",
            "Is this a real compliance system?":
                "No. It is an illustrative prototype and not a live regulatory system.",
            "Can stakeholders use this platform to manage allowances or compliance status?":
                "No. This platform is not designed for registry operations, compliance tracking, or enforcement.",
            "Who is this platform for?":
                "It is intended for stakeholders who need to understand ECS design, consultation processes, and learning materials.",
        }

        for q, a in faq_items.items():
            with st.expander(q):
                st.write(a)

    with tab5:
        st.markdown("### Related Operational Systems")
        st.write(
            "The ECS stakeholder platform is not itself an MRV portal or registry. However, stakeholders may still need "
            "to understand what those systems do and how they relate to the broader ECS ecosystem."
        )

        sys1, sys2 = st.columns(2)

        with sys1:
            st.markdown("""
            <div class="resource-card">
                <div class="resource-meta">Illustrative External Link</div>
                <div class="resource-title">MRV Portal</div>
                <div class="resource-text">
                    A separate operational system where monitoring, reporting, and verification activities may be managed.
                    This card is for awareness and orientation only.
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.code("https://ecs/mrv-portal", language=None)

        with sys2:
            st.markdown("""
            <div class="resource-card">
                <div class="resource-meta">Illustrative External Link</div>
                <div class="resource-title">Allowance Registry Platform</div>
                <div class="resource-text">
                    A separate operational platform where allowance accounts, transfers, and related actions may be administered.
                    This card is for awareness and orientation only.
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.code("https://ecs/registry-platform", language=None)

        st.info(
            "These URLs are mock examples included only to help stakeholders understand where operational systems may sit "
            "alongside a stakeholder-facing information and engagement platform."
        )
















# -------------------------------------------------------
# STAKEHOLDER ENGAGEMENT
# -------------------------------------------------------
elif module == "Stakeholder Engagement":

    st.markdown("""
    <div class="page-hero">
        <div class="page-kicker">Stakeholder Engagement</div>
        <div class="page-title">Participate in ECS consultation and dialogue</div>
        <div class="page-subtitle">
            This section is designed to support structured stakeholder engagement throughout ECS development.
            It explains how stakeholders can participate, submit feedback, and stay informed about engagement
            activities across the design, pilot, and operational readiness phases.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="page-note">
        <b>Illustrative prototype only.</b> This section is intended to demonstrate consultation,
        dialogue, and feedback processes. It is not a compliance reporting or enforcement tool.
    </div>
    """, unsafe_allow_html=True)

    top1, top2, top3 = st.columns(3)

    with top1:
        st.markdown("""
        <div class="info-feature-card">
            <div class="info-feature-tag">Overview</div>
            <div class="info-feature-title">Why stakeholder engagement matters</div>
            <div class="info-feature-text">
                Stakeholder engagement helps improve transparency, collect practical input,
                and support more informed ECS design and implementation.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with top2:
        st.markdown("""
        <div class="info-feature-card">
            <div class="info-feature-tag">Participation</div>
            <div class="info-feature-title">How stakeholders can participate</div>
            <div class="info-feature-text">
                Stakeholders may participate through consultation papers, workshops, meetings,
                and structured feedback submissions.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with top3:
        st.markdown("""
        <div class="info-feature-card">
            <div class="info-feature-tag">Feedback</div>
            <div class="info-feature-title">How feedback is collected</div>
            <div class="info-feature-text">
                Feedback may be submitted through a structured online form and reviewed
                by engagement phase, stakeholder type, and topic.
            </div>
        </div>
        """, unsafe_allow_html=True)

    engagement_tab1, engagement_tab2, engagement_tab3, engagement_tab4, engagement_tab5 = st.tabs(
        [
            "Engagement Overview",
            "How to Participate",
            "Submit Feedback",
            "Schedule & Channels",
            "Timeline by Phase",
        ]
    )

    # ---------------------------------------------------
    # TAB 1: ENGAGEMENT OVERVIEW
    # ---------------------------------------------------
    with engagement_tab1:
        st.markdown("### Engagement Overview")
        st.write(
            "The ECS stakeholder engagement approach is intended to create structured dialogue between "
            "government institutions, industry stakeholders, technical experts, and other relevant groups. "
            "It supports transparency, improves understanding of stakeholder needs, and helps strengthen "
            "policy design through consultation and feedback."
        )

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Primary objectives of engagement**")
            st.write("- Improve transparency during ECS development")
            st.write("- Collect stakeholder views on key design issues")
            st.write("- Support dialogue across affected sectors")
            st.write("- Identify implementation questions early")
            st.write("- Build trust and participation over time")

        with col2:
            st.markdown("**Illustrative stakeholder groups**")
            st.write("- Entities under the compliance system")
            st.write("- Government and public institutions")
            st.write("- Technical experts and advisors")
            st.write("- Industry associations")
            st.write("- Researchers and wider stakeholders")

        st.info(
            "This page focuses on engagement and consultation only. Training materials and simulation exercises "
            "should sit in the Capacity Building and Simulation sections, not here."
        )

    # ---------------------------------------------------
    # TAB 2: HOW TO PARTICIPATE
    # ---------------------------------------------------
    with engagement_tab2:
        st.markdown("### How Stakeholders Can Participate")
        st.write(
            "Stakeholders may participate in the ECS engagement process through several consultation and dialogue channels."
        )

        p1, p2 = st.columns(2)

        with p1:
            st.markdown("""
            <div class="engage-card">
                <div class="engage-title">Consultation Papers</div>
                <div class="engage-text">
                    Stakeholders review draft papers, concept notes, and policy materials,
                    then submit comments and observations through formal consultation channels.
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="engage-card">
                <div class="engage-title">Stakeholder Workshops</div>
                <div class="engage-text">
                    Workshops provide an opportunity to discuss sector-specific questions,
                    implementation issues, and stakeholder concerns in a more interactive setting.
                </div>
            </div>
            """, unsafe_allow_html=True)

        with p2:
            st.markdown("""
            <div class="engage-card">
                <div class="engage-title">Technical Working Groups</div>
                <div class="engage-text">
                    Technical working groups bring together relevant experts and stakeholder representatives
                    to review design options, methodologies, and operational considerations.
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="engage-card">
                <div class="engage-title">Direct Feedback Submission</div>
                <div class="engage-text">
                    Stakeholders may use the feedback form below to provide comments, suggestions,
                    clarification requests, and implementation observations.
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("### What stakeholders may comment on")
        st.write("- Policy design")
        st.write("- Market functioning")
        st.write("- Sector-specific implementation questions")
        st.write("- Stakeholder readiness")
        st.write("- General comments and suggestions")

    # ---------------------------------------------------
    # TAB 3: SUBMIT FEEDBACK
    # ---------------------------------------------------
    with engagement_tab3:
        st.markdown("### Submit Feedback")
        st.write(
            "Stakeholders may submit structured feedback on ECS design, stakeholder engagement activities, "
            "sector-specific concerns, and implementation-related questions."
        )

        form_col1, form_col2 = st.columns([2, 1])

        with form_col1:
            with st.form("feedback_form"):
                name = st.text_input("Stakeholder Name")
                organization = st.text_input("Organization")

                stakeholder_group = st.selectbox(
                    "Stakeholder Group",
                    [
                        "Entities under the compliance system",
                        "Government / Public Institution",
                        "Technical Expert / Advisor",
                        "Industry Association",
                        "Research / Academic",
                        "Other",
                    ],
                )

                sector = st.selectbox(
                    "Sector / Area",
                    [
                        "Power and Utilities",
                        "Cement and Construction Materials",
                        "Petrochemical Value Chains",
                        "Steel and Manufacturing",
                        "Government / Public Institutions",
                        "Other",
                    ],
                )

                feedback_type = st.selectbox(
                    "Feedback Type",
                    [
                        "Policy Design",
                        "Market Functioning",
                        "Sector Readiness",
                        "Technical Clarification",
                        "General Comment",
                    ],
                )

                engagement_phase = st.selectbox(
                    "Engagement Phase",
                    ["Design Phase", "Pilot Phase", "Operational Readiness Phase"],
                )

                comment = st.text_area("Comment / Feedback")

                submitted = st.form_submit_button("Submit Feedback")

                if submitted:
                    feedback_row = {
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "stakeholder_name": name,
                        "organization": organization,
                        "stakeholder_group": stakeholder_group,
                        "sector": sector,
                        "feedback_type": feedback_type,
                        "engagement_phase": engagement_phase,
                        "comment": comment,
                    }

                    save_to_excel(FEEDBACK_FILE, feedback_row)
                    st.success("Feedback submitted successfully.")

        with form_col2:
            st.markdown("**How feedback is handled**")
            st.write("- Submitted through a structured online form")
            st.write("- Tagged by stakeholder type and engagement phase")
            st.write("- Used to support transparent review and follow-up")
            st.write("- Can help identify key themes and stakeholder concerns")

            st.markdown("**Illustrative focus areas**")
            st.write("- Policy design")
            st.write("- Market functioning")
            st.write("- Sector readiness")
            st.write("- Technical clarification")
            st.write("- General comments")

        feedback_df = load_excel(FEEDBACK_FILE)
        if not feedback_df.empty:
            st.markdown("---")
            st.markdown("### Submitted Feedback Records")
            st.dataframe(feedback_df, use_container_width=True, hide_index=True)

    # ---------------------------------------------------
    # TAB 4: SCHEDULE & CHANNELS
    # ---------------------------------------------------
    with engagement_tab4:
        st.markdown("### Engagement Channels and Schedule")
        st.write(
            "The ECS stakeholder engagement process may include regular meetings and consultation activities "
            "to gather feedback, discuss sector issues, and support transparent communication."
        )

        channel_tab1, channel_tab2, channel_tab3, channel_tab4 = st.tabs(
            [
                "Technical Working Groups",
                "Sector Workshops",
                "Public Consultation Sessions",
                "Steering / Coordination Meetings",
            ]
        )

        with channel_tab1:
            st.markdown("#### Technical Working Groups")
            st.write("**Illustrative Frequency:** Monthly")
            st.write("**Participants:** Technical experts, stakeholder representatives, relevant institutions")
            st.markdown("**Purpose**")
            st.write("- Discuss technical aspects of ECS design")
            st.write("- Review methodologies and assumptions")
            st.write("- Address implementation questions")

        with channel_tab2:
            st.markdown("#### Sector Workshops")
            st.write("**Illustrative Frequency:** Quarterly")
            st.markdown("**Purpose**")
            st.write("- Present policy updates")
            st.write("- Discuss sector-specific implications")
            st.write("- Collect stakeholder input and concerns")

            st.markdown("**Illustrative sectors**")
            st.write("- Power and Utilities")
            st.write("- Cement and Construction Materials")
            st.write("- Petrochemical Value Chains")
            st.write("- Steel and Manufacturing")

        with channel_tab3:
            st.markdown("#### Public Consultation Sessions")
            st.write("**Illustrative Frequency:** At key policy milestones")
            st.markdown("**Purpose**")
            st.write("- Present draft policy documents")
            st.write("- Gather formal stakeholder comments")
            st.write("- Strengthen transparency and visibility")

        with channel_tab4:
            st.markdown("#### Steering / Coordination Meetings")
            st.write("**Illustrative Frequency:** As required")
            st.write("**Participants:** Senior officials, policy leads, coordination bodies")
            st.markdown("**Purpose**")
            st.write("- Review key decisions")
            st.write("- Align on strategic direction")
            st.write("- Support coordination across institutions")

        st.markdown("---")
        st.markdown("### Engagement Structure Summary")

        engagement_df = pd.DataFrame(
            {
                "Engagement Channel": [
                    "Technical Working Groups",
                    "Sector Workshops",
                    "Public Consultation Sessions",
                    "Steering / Coordination Meetings",
                ],
                "Illustrative Frequency": [
                    "Monthly",
                    "Quarterly",
                    "At key policy milestones",
                    "As required",
                ],
                "Primary Purpose": [
                    "Technical discussion and design review",
                    "Sector dialogue and input collection",
                    "Formal consultation and transparency",
                    "Strategic review and coordination",
                ],
            }
        )

        st.dataframe(engagement_df, use_container_width=True, hide_index=True)

    # ---------------------------------------------------
    # TAB 5: TIMELINE BY PHASE
    # ---------------------------------------------------
    with engagement_tab5:
        st.markdown("### Engagement Timeline by Phase")
        st.write(
            "Engagement activities may evolve across different ECS development phases. "
            "The structure below illustrates how stakeholder interaction may change over time."
        )

        t1, t2, t3 = st.columns(3)

        with t1:
            st.markdown("""
            <div class="phase-card">
                <div class="phase-title">Design Phase</div>
                <div class="phase-text">
                    - Public consultations<br>
                    - Technical working groups<br>
                    - Sector stakeholder workshops<br>
                    - Early dialogue on design options
                </div>
            </div>
            """, unsafe_allow_html=True)

        with t2:
            st.markdown("""
            <div class="phase-card">
                <div class="phase-title">Pilot Phase</div>
                <div class="phase-text">
                    - Targeted stakeholder meetings<br>
                    - Pilot-related feedback sessions<br>
                    - Readiness discussions<br>
                    - Review of initial implementation issues
                </div>
            </div>
            """, unsafe_allow_html=True)

        with t3:
            st.markdown("""
            <div class="phase-card">
                <div class="phase-title">Operational Readiness Phase</div>
                <div class="phase-text">
                    - Ongoing stakeholder forums<br>
                    - Consultation on updates<br>
                    - Continuous feedback channels<br>
                    - Communication on next steps
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        timeline_df = pd.DataFrame(
            {
                "Phase": [
                    "Design Phase",
                    "Pilot Phase",
                    "Operational Readiness Phase",
                ],
                "Illustrative Engagement Activities": [
                    "Public consultations, technical working groups, sector workshops, early dialogue on policy design",
                    "Targeted stakeholder meetings, pilot feedback sessions, readiness discussions, implementation review",
                    "Stakeholder forums, consultation on updates, continuous feedback channels, communication on next steps",
                ],
            }
        )

        st.dataframe(timeline_df, use_container_width=True, hide_index=True)
















# -------------------------------------------------------
# CAPACITY BUILDING & LEARNING
# -------------------------------------------------------
elif module == "Capacity Building & Learning":

    st.markdown("""
    <div class="page-hero">
        <div class="page-kicker">Capacity Building & Learning</div>
        <div class="page-title">Build practical readiness for ECS participation</div>
        <div class="page-subtitle">
            This section focuses on stakeholder learning and preparation.
            It provides structured learning pathways, training materials,
            and practical guidance that help stakeholders understand how
            ECS mechanisms and market dynamics may operate.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="page-note">
        <b>Illustrative prototype only.</b>
        The materials below are designed for stakeholder learning and readiness.
        They do not represent operational regulatory instructions.
    </div>
    """, unsafe_allow_html=True)

    top1, top2, top3 = st.columns(3)

    with top1:
        st.markdown("""
        <div class="info-feature-card">
        <div class="info-feature-tag">Learning Path</div>
        <div class="info-feature-title">Structured understanding</div>
        <div class="info-feature-text">
        Stakeholders move from basic awareness to practical understanding
        through guided learning modules and practical explanations.
        </div>
        </div>
        """, unsafe_allow_html=True)

    with top2:
        st.markdown("""
        <div class="info-feature-card">
        <div class="info-feature-tag">Training Materials</div>
        <div class="info-feature-title">Learning resources</div>
        <div class="info-feature-text">
        Guidance notes, workshop summaries, and learning materials
        help stakeholders build familiarity with ECS policy concepts.
        </div>
        </div>
        """, unsafe_allow_html=True)

    with top3:
        st.markdown("""
        <div class="info-feature-card">
        <div class="info-feature-tag">Simulation Preparation</div>
        <div class="info-feature-title">Prepare for exercises</div>
        <div class="info-feature-text">
        Stakeholders can review practical explanations and manuals
        before interacting with ECS simulation exercises.
        </div>
        </div>
        """, unsafe_allow_html=True)

    capacity_tab1, capacity_tab2, capacity_tab3, capacity_tab4, capacity_tab5 = st.tabs(
        [
            "Learning Pathway",
            "Training Resources",
            "Practical Guidance",
            "Simulation Preparation",
            "Reference Materials"
        ]
    )

    # ---------------------------------------------------
    # LEARNING PATHWAY
    # ---------------------------------------------------

    with capacity_tab1:

        st.markdown("### Learning Pathway")

        st.write(
            "The learning pathway helps stakeholders progressively build understanding of ECS "
            "concepts and system logic before engaging with consultations or simulation exercises."
        )

        pathway_df = pd.DataFrame({
            "Learning Stage":[
                "Stage 1 — System Awareness",
                "Stage 2 — Stakeholder Roles",
                "Stage 3 — Market Concepts",
                "Stage 4 — Policy Design Understanding",
                "Stage 5 — Simulation Preparation"
            ],
            "Purpose":[
                "Understand the role and purpose of ECS policy frameworks.",
                "Recognize how different stakeholder groups may interact with the system.",
                "Understand allowances, carbon price signals, and market incentives.",
                "Understand how design choices influence system outcomes.",
                "Prepare for interactive simulation and scenario exercises."
            ]
        })

        st.dataframe(pathway_df, use_container_width=True, hide_index=True)

    # ---------------------------------------------------
    # TRAINING RESOURCES
    # ---------------------------------------------------

    with capacity_tab2:

        st.markdown("### Training Resources")

        r1, r2 = st.columns(2)

        with r1:

            st.markdown("""
            <div class="engage-card">
            <div class="engage-title">Guidance Notes</div>
            <div class="engage-text">
            Concise briefing notes explaining ECS concepts,
            market structure, and policy design principles.
            </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="engage-card">
            <div class="engage-title">Workshop Materials</div>
            <div class="engage-text">
            Presentation slides and workshop summaries used
            during stakeholder engagement sessions.
            </div>
            </div>
            """, unsafe_allow_html=True)

        with r2:

            st.markdown("""
            <div class="engage-card">
            <div class="engage-title">Learning Briefs</div>
            <div class="engage-text">
            Short explainers that translate technical policy
            discussions into accessible stakeholder insights.
            </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="engage-card">
            <div class="engage-title">Concept Explainers</div>
            <div class="engage-text">
            Practical explanations describing allowances,
            emissions caps, and price signals.
            </div>
            </div>
            """, unsafe_allow_html=True)

    # ---------------------------------------------------
    # PRACTICAL GUIDANCE
    # ---------------------------------------------------

    with capacity_tab3:

        st.markdown("### Practical Guidance")

        guidance_df = pd.DataFrame({

            "Topic":[
                "Allowance Allocation",
                "Carbon Price Signals",
                "Monitoring and Reporting Concepts",
                "Verification and Data Integrity",
                "Policy Design Choices"
            ],

            "Purpose":[
                "Explain how allowances may be distributed within the system.",
                "Illustrate how carbon pricing influences behavior and investment decisions.",
                "Explain how emissions-related information may be monitored and reported.",
                "Highlight why verification supports transparency and credibility.",
                "Explain how cap levels and allocation design influence market outcomes."
            ]

        })

        st.dataframe(guidance_df, use_container_width=True, hide_index=True)

    # ---------------------------------------------------
    # SIMULATION PREPARATION
    # ---------------------------------------------------

    with capacity_tab4:

        st.markdown("### Simulation Preparation")

        st.write(
            "Before participating in ECS simulation exercises, stakeholders can review "
            "a short user manual explaining how the simulator works and what learning "
            "objectives each exercise is designed to demonstrate."
        )

        st.markdown("""
        <div class="resource-card">
        <div class="resource-meta">User Guide</div>
        <div class="resource-title">ECS Simulation User Manual</div>
        <div class="resource-text">
        A practical guide explaining how to navigate the simulation interface,
        interpret allowance balances, and explore carbon market scenarios.
        </div>
        </div>
        """, unsafe_allow_html=True)

        st.code("https://ecs-platform/simulation-user-manual")

        st.info(
            "The simulation manual will support stakeholders interacting with the "
            "ECS demonstration simulator available in the Simulation section."
        )

    # ---------------------------------------------------
    # REFERENCE MATERIALS
    # ---------------------------------------------------

    with capacity_tab5:

        st.markdown("### Reference Materials")

        c1, c2 = st.columns(2)

        with c1:

            st.markdown("""
            <div class="resource-card">
            <div class="resource-meta">Learning Note</div>
            <div class="resource-title">Understanding Carbon Markets</div>
            <div class="resource-text">
            A short explainer introducing the economic logic
            behind emissions trading systems.
            </div>
            </div>
            """, unsafe_allow_html=True)

        with c2:

            st.markdown("""
            <div class="resource-card">
            <div class="resource-meta">Policy Explainer</div>
            <div class="resource-title">ECS Design Principles</div>
            <div class="resource-text">
            A briefing explaining how different design parameters
            influence system performance and stakeholder incentives.
            </div>
            </div>
            """, unsafe_allow_html=True)

























# -------------------------------------------------------
# SIMULATION & DEMONSTRATION
# -------------------------------------------------------
elif module == "Simulation & Demonstration":

    st.markdown("""
    <div class="sim-hero">
        <div class="sim-kicker">Simulation & Demonstration</div>
        <div class="sim-title">ECS Learning Simulation Lab</div>
        <div class="sim-subtitle">
            This lab combines guided learning modules with one integrated linked simulator to help
            stakeholders explore how ECS design choices, market conditions, firm responses, and
            emissions outcomes may interact in practice.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sim-note">
        <b>Illustrative prototype only.</b> This section is designed for stakeholder learning,
        engagement, and applied understanding. It includes guided modules for focused learning
        and one integrated simulator that links design, market dynamics, firm behavior,
        trading activity, and emissions outcomes.
    </div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------
    # RESET
    # ---------------------------------------------------
    sim_keys_to_clear = [
        "policy_scenario",
        "firm_sector",
        "firm_carbon_price",
        "firm_emissions",
        "firm_allowances",
        "firm_abatement_cost",
        "firm_abatement_amount",
        "market_carbon_price",
        "trajectory_start_year",
        "trajectory_end_year",
        "trajectory_initial_price",
        "trajectory_annual_increase",
        "pathway_sector",
        "pathway_baseline_emissions",
        "pathway_reduction_rate",
        "pathway_start_year",
        "pathway_end_year",
        "market_supply",
        "demand_power",
        "demand_cement",
        "demand_petrochem",
        "demand_metals",
        "trading_carbon_price",
        "trade_buyer",
        "trade_seller",
        "trade_quantity",
        "firms_data",
        "trade_log",
        "design_cap_type",
        "design_cap_stringency",
        "design_allocation_method",
        "design_price_floor",
        "design_price_ceiling",
        "design_banking",
        "design_offsets",
        "learning_exercise",
        "integrated_cap_type",
        "integrated_cap_stringency",
        "integrated_allocation_method",
        "integrated_banking",
        "integrated_offsets",
        "integrated_sector",
        "integrated_baseline_emissions",
        "integrated_firm_emissions",
        "integrated_abatement_cost",
        "integrated_reduction_potential",
        "integrated_sector_demand_factor",
        "integrated_external_market_pressure",
    ]

    reset_col1, reset_col2 = st.columns([6, 1])
    with reset_col2:
        if st.button("Reset Lab"):
            for key in sim_keys_to_clear:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

    # ---------------------------------------------------
    # ADMINISTRATOR VIEW
    # ---------------------------------------------------
    with st.expander("Administrator View – Training Configuration", expanded=False):
        st.caption(
            "This configuration area is intended for administrator or facilitator use during training sessions."
        )

        scenario = st.selectbox(
            "Training Scenario",
            [
                "Conservative Carbon Price",
                "Accelerated Decarbonization",
                "Tight Cap Scenario",
                "Technology Breakthrough",
            ],
            key="policy_scenario",
        )

        scenario_defaults = {
            "Conservative Carbon Price": {
                "carbon_price": 35,
                "annual_increase": 3,
                "abatement_cost_multiplier": 1.0,
                "allowance_multiplier": 1.0,
                "reduction_rate": 4,
                "supply_multiplier": 1.05,
            },
            "Accelerated Decarbonization": {
                "carbon_price": 60,
                "annual_increase": 6,
                "abatement_cost_multiplier": 1.0,
                "allowance_multiplier": 0.92,
                "reduction_rate": 8,
                "supply_multiplier": 0.95,
            },
            "Tight Cap Scenario": {
                "carbon_price": 75,
                "annual_increase": 8,
                "abatement_cost_multiplier": 1.1,
                "allowance_multiplier": 0.85,
                "reduction_rate": 7,
                "supply_multiplier": 0.85,
            },
            "Technology Breakthrough": {
                "carbon_price": 55,
                "annual_increase": 4,
                "abatement_cost_multiplier": 0.7,
                "allowance_multiplier": 0.95,
                "reduction_rate": 10,
                "supply_multiplier": 0.95,
            },
        }

        selected_scenario = scenario_defaults[scenario]

        cfg1, cfg2, cfg3 = st.columns(3)
        cfg1.metric("Starting Carbon Price", f"${selected_scenario['carbon_price']}/tCO2")
        cfg2.metric("Annual Price Increase", f"{selected_scenario['annual_increase']}")
        cfg3.metric("Reduction Rate", f"{selected_scenario['reduction_rate']}%")

    if "policy_scenario" not in st.session_state:
        st.session_state["policy_scenario"] = "Conservative Carbon Price"

    scenario_defaults = {
        "Conservative Carbon Price": {
            "carbon_price": 35,
            "annual_increase": 3,
            "abatement_cost_multiplier": 1.0,
            "allowance_multiplier": 1.0,
            "reduction_rate": 4,
            "supply_multiplier": 1.05,
        },
        "Accelerated Decarbonization": {
            "carbon_price": 60,
            "annual_increase": 6,
            "abatement_cost_multiplier": 1.0,
            "allowance_multiplier": 0.92,
            "reduction_rate": 8,
            "supply_multiplier": 0.95,
        },
        "Tight Cap Scenario": {
            "carbon_price": 75,
            "annual_increase": 8,
            "abatement_cost_multiplier": 1.1,
            "allowance_multiplier": 0.85,
            "reduction_rate": 7,
            "supply_multiplier": 0.85,
        },
        "Technology Breakthrough": {
            "carbon_price": 55,
            "annual_increase": 4,
            "abatement_cost_multiplier": 0.7,
            "allowance_multiplier": 0.95,
            "reduction_rate": 10,
            "supply_multiplier": 0.95,
        },
    }

    selected_scenario = scenario_defaults[st.session_state["policy_scenario"]]

    sector_descriptions = {
        "Power and Utilities": (
            "Typically the largest source of emissions in many systems. Transition options may include "
            "renewable electricity, fuel switching, efficiency improvements, and carbon capture."
        ),
        "Cement and Construction Materials": (
            "Often emissions-intensive due to process and fuel emissions. Transition options may include "
            "clinker substitution, fuel switching, efficiency measures, and low-carbon production pathways."
        ),
        "Metals and Materials": (
            "This sector may face high energy demand and process emissions. Options may include electrification, "
            "efficiency gains, and lower-carbon inputs."
        ),
        "Petrochemical Value Chains": (
            "A complex industrial sector where emissions arise across multiple value chains. Transition options "
            "may include efficiency, process redesign, cleaner feedstocks, and innovation."
        ),
        "Refining and Processing": (
            "This sector may face both direct process emissions and indirect energy-related emissions. "
            "Transition strategies may include efficiency measures, fuel switching, and technology upgrades."
        ),
    }

    sim_tab1, sim_tab2, sim_tab3 = st.tabs(
        [
            "Lab Overview",
            "Modules & Integrated Simulator",
            "Key Insights",
        ]
    )

    # ---------------------------------------------------
    # TAB 1: LAB OVERVIEW
    # ---------------------------------------------------
    with sim_tab1:
        st.markdown("### Lab Overview")
        st.write(
            "This lab includes seven guided modules that explain specific parts of ECS logic, followed by "
            "one integrated simulator that links design choices, supply, scarcity, price, firm response, "
            "trading needs, and emissions outcomes."
        )

        ov1, ov2, ov3, ov4 = st.columns(4)
        ov1.metric("Guided Modules", "7")
        ov2.metric("Integrated Simulator", "1")
        ov3.metric("Market Topics", "Supply, Price, Trading")
        ov4.metric("Learning Scope", "Firm + Sector + Design")

        c1, c2 = st.columns(2)

        with c1:
            st.markdown("""
            <div class="sim-card">
                <div class="sim-card-tag">Guided Modules</div>
                <div class="sim-card-title">Focused learning areas</div>
                <div class="sim-card-text">
                    The first seven modules help stakeholders explore specific questions one at a time,
                    such as firm strategy, market balance, price pathways, and design choices.
                </div>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div class="sim-card">
                <div class="sim-card-tag">Integrated Simulator</div>
                <div class="sim-card-title">Linked system behavior</div>
                <div class="sim-card-text">
                    The eighth module links policy design, allowance supply, market scarcity,
                    carbon price, firm response, trading demand, and emissions outcomes in one flow.
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("### Learning Flow")
        f1, f2, f3, f4 = st.columns(4)

        with f1:
            st.markdown("""
            <div class="sim-flow-box">
                <div class="sim-flow-title">1. Guided understanding</div>
                <div class="sim-flow-text">
                    Explore individual concepts such as price signals, market balance, and trading logic.
                </div>
            </div>
            """, unsafe_allow_html=True)

        with f2:
            st.markdown("""
            <div class="sim-flow-box">
                <div class="sim-flow-title">2. Design choices</div>
                <div class="sim-flow-text">
                    Review how cap design, allocation, and flexibility mechanisms shape system conditions.
                </div>
            </div>
            """, unsafe_allow_html=True)

        with f3:
            st.markdown("""
            <div class="sim-flow-box">
                <div class="sim-flow-title">3. Firm response</div>
                <div class="sim-flow-text">
                    Assess how firms may respond through abatement, allowance purchasing, or trading.
                </div>
            </div>
            """, unsafe_allow_html=True)

        with f4:
            st.markdown("""
            <div class="sim-flow-box">
                <div class="sim-flow-title">4. Linked outcomes</div>
                <div class="sim-flow-text">
                    Use the integrated simulator to see how all these elements affect one another.
                </div>
            </div>
            """, unsafe_allow_html=True)

        overview_df = pd.DataFrame(
            {
                "Module": [
                    "1. Firm Compliance Strategy",
                    "2. Allowance Trading Market",
                    "3. Carbon Price Pathways",
                    "4. Sector Decarbonization Pathways",
                    "5. Allowance Market Balance",
                    "6. Carbon Allowance Trading Desk",
                    "7. Carbon Market Design Lab",
                    "8. Integrated ECS Policy & Market Simulator",
                ],
                "Purpose": [
                    "Understand how firms compare allowance purchase versus emissions reduction options.",
                    "See how buyer and seller positions emerge in an allowance market.",
                    "Understand how price trajectories may influence planning and decisions.",
                    "Explore how emissions pathways may differ across sectors.",
                    "Understand how supply and demand create scarcity or surplus pressure.",
                    "Visualize allowance exchange between firms in a simplified trading environment.",
                    "Explore how design choices influence supply, scarcity, and price signals.",
                    "Link policy design, supply, scarcity, price, firm response, trading demand, and emissions outcomes.",
                ],
            }
        )
        st.dataframe(overview_df, use_container_width=True, hide_index=True)

    # ---------------------------------------------------
    # TAB 2: MODULES & INTEGRATED SIMULATOR
    # ---------------------------------------------------
    with sim_tab2:
        st.markdown("### Guided Modules and Integrated Simulator")
        st.write(
            "Select one guided module to explore a focused learning topic, or choose the integrated simulator "
            "to examine how system components interact within one linked model."
        )

        exercise = st.selectbox(
            "Select Module",
            [
                "1. Firm Compliance Strategy",
                "2. Allowance Trading Market",
                "3. Carbon Price Pathways",
                "4. Sector Decarbonization Pathways",
                "5. Allowance Market Balance",
                "6. Carbon Allowance Trading Desk",
                "7. Carbon Market Design Lab",
                "8. Integrated ECS Policy & Market Simulator",
            ],
            key="learning_exercise",
        )

        # 1
        if exercise == "1. Firm Compliance Strategy":
            st.markdown("### 1. Firm Compliance Strategy")
            st.caption("Guided module: compare firm responses under different price and abatement conditions.")

            col1, col2 = st.columns([1, 1])

            with col1:
                selected_sector = st.selectbox(
                    "Illustrative Sector",
                    list(sector_descriptions.keys()),
                    key="firm_sector",
                )
                st.caption(sector_descriptions[selected_sector])

                default_price = selected_scenario["carbon_price"]
                default_allowances = int(80 * selected_scenario["allowance_multiplier"])
                default_abatement_cost = int(30 * selected_scenario["abatement_cost_multiplier"])

                carbon_price = st.slider("Carbon Price ($/tCO2)", 0, 200, default_price, key="firm_carbon_price")
                emissions = st.number_input("Emissions (tCO2)", min_value=0, value=100, key="firm_emissions")
                allowances = st.number_input("Allowances Available", min_value=0, value=default_allowances, key="firm_allowances")
                abatement_cost = st.number_input("Abatement Cost ($/tCO2)", min_value=0, value=default_abatement_cost, key="firm_abatement_cost")
                abatement_amount = st.number_input("Potential Abatement Quantity (tCO2)", min_value=0, value=20, key="firm_abatement_amount")

            shortfall_before = max(emissions - allowances, 0)
            actual_abatement = min(abatement_amount, emissions)
            emissions_after = max(emissions - actual_abatement, 0)
            shortfall_after = max(emissions_after - allowances, 0)

            compliance_cost_before = shortfall_before * carbon_price
            abatement_total_cost = actual_abatement * abatement_cost
            compliance_cost_after = shortfall_after * carbon_price
            total_cost_with_abatement = abatement_total_cost + compliance_cost_after

            with col2:
                st.markdown("#### Results")
                st.metric("Shortfall Before Action", f"{shortfall_before} tCO2")
                st.metric("Shortfall After Abatement", f"{shortfall_after} tCO2")
                st.metric("Buy-Only Cost", f"${compliance_cost_before:,.0f}")
                st.metric("Abatement + Remaining Purchase", f"${total_cost_with_abatement:,.0f}")

            chart_data = pd.DataFrame(
                {"Option": ["Buy Only", "Abate + Buy Remaining"], "Illustrative Cost": [compliance_cost_before, total_cost_with_abatement]}
            )
            fig = px.bar(chart_data, x="Option", y="Illustrative Cost", title="Illustrative Compliance Decision Comparison")
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("#### Result Statement")
            if abatement_cost < carbon_price:
                st.success("Illustrative result: abatement appears more attractive because reducing emissions costs less than buying allowances.")
            elif abatement_cost > carbon_price:
                st.warning("Illustrative result: purchasing allowances may appear more attractive in the short term because the carbon price is lower than abatement cost.")
            else:
                st.info("Illustrative result: abatement and allowance purchase are broadly similar in cost in this case.")

            st.markdown("#### Learning Takeaway")
            st.write(
                "This module shows how carbon price, allowance availability, and abatement cost interact to shape firm-level choices."
            )

        # 2
        elif exercise == "2. Allowance Trading Market":
            st.markdown("### 2. Allowance Trading Market")
            st.caption("Guided module: understand how buyer and seller positions emerge in a simplified market.")

            carbon_price_market = st.slider(
                "Illustrative Market Carbon Price ($/tCO2)",
                0,
                200,
                selected_scenario["carbon_price"],
                key="market_carbon_price",
            )

            allowance_multiplier = selected_scenario["allowance_multiplier"]

            market_df = pd.DataFrame(
                {
                    "Firm": ["Firm A", "Firm B", "Firm C", "Firm D"],
                    "Sector": [
                        "Power and Utilities",
                        "Cement and Construction Materials",
                        "Petrochemical Value Chains",
                        "Metals and Materials",
                    ],
                    "Emissions": [120, 90, 70, 110],
                    "Allowances": [
                        int(100 * allowance_multiplier),
                        int(95 * allowance_multiplier),
                        int(85 * allowance_multiplier),
                        int(90 * allowance_multiplier),
                    ],
                }
            )

            market_df["Position"] = market_df["Allowances"] - market_df["Emissions"]
            market_df["Status"] = market_df["Position"].apply(lambda x: "Seller" if x > 0 else ("Buyer" if x < 0 else "Balanced"))
            market_df["Illustrative Cost"] = market_df["Position"].apply(lambda x: abs(x) * carbon_price_market if x < 0 else 0)

            st.dataframe(market_df, use_container_width=True)

            col1, col2 = st.columns(2)
            with col1:
                fig_status = px.bar(market_df, x="Firm", y="Position", color="Status", title="Illustrative Firm Positions")
                st.plotly_chart(fig_status, use_container_width=True)
            with col2:
                status_counts = market_df["Status"].value_counts().reset_index()
                status_counts.columns = ["Status", "Count"]
                fig_market = px.bar(status_counts, x="Status", y="Count", title="Buyers vs Sellers")
                st.plotly_chart(fig_market, use_container_width=True)

            buyers = len(market_df[market_df["Status"] == "Buyer"])
            sellers = len(market_df[market_df["Status"] == "Seller"])

            st.markdown("#### Result Statement")
            st.info(
                f"Illustrative result: this market view shows **{buyers} buyer(s)** and **{sellers} seller(s)**, demonstrating how trading emerges when some firms have shortfalls and others have surpluses."
            )

            st.markdown("#### Learning Takeaway")
            st.write("This module highlights how market participation depends on differences in allowance positions across firms.")

        # 3
        elif exercise == "3. Carbon Price Pathways":
            st.markdown("### 3. Carbon Price Pathways")
            st.caption("Guided module: explore how rising or changing prices may influence longer-term planning.")

            col1, col2 = st.columns(2)

            with col1:
                start_year = st.number_input("Start Year", 2025, 2050, 2027, key="trajectory_start_year")
                end_year = st.number_input("End Year", 2026, 2060, 2035, key="trajectory_end_year")
                initial_price = st.number_input("Initial Carbon Price ($/tCO2)", min_value=0, value=selected_scenario["carbon_price"], key="trajectory_initial_price")
                annual_increase = st.number_input("Annual Price Increase ($/tCO2)", min_value=0, value=selected_scenario["annual_increase"], key="trajectory_annual_increase")

            if end_year <= start_year:
                st.warning("End Year must be greater than Start Year.")
            else:
                years = list(range(start_year, end_year + 1))
                prices = [initial_price + annual_increase * (year - start_year) for year in years]
                trajectory_df = pd.DataFrame({"Year": years, "Carbon Price": prices})

                with col2:
                    st.metric("Starting Price", f"${initial_price}/tCO2")
                    st.metric("Ending Price", f"${prices[-1]}/tCO2")
                    st.metric("Years Covered", len(years))

                fig_price = px.line(trajectory_df, x="Year", y="Carbon Price", markers=True, title="Illustrative Carbon Price Path")
                st.plotly_chart(fig_price, use_container_width=True)
                st.dataframe(trajectory_df, use_container_width=True)

                st.markdown("#### Result Statement")
                st.info(f"Illustrative result: the carbon price rises from **${initial_price}/tCO2** to **${prices[-1]}/tCO2** over the selected period.")

                st.markdown("#### Learning Takeaway")
                st.write("This module shows how price pathways can shape the timing of investment and abatement decisions.")

        # 4
        elif exercise == "4. Sector Decarbonization Pathways":
            st.markdown("### 4. Sector Decarbonization Pathways")
            st.caption("Guided module: examine how emissions pathways may differ by sector.")

            col1, col2 = st.columns(2)

            with col1:
                pathway_sector = st.selectbox("Sector", list(sector_descriptions.keys()), key="pathway_sector")
                st.caption(sector_descriptions[pathway_sector])

                baseline_emissions = st.number_input("Baseline Emissions (tCO2)", min_value=0, value=1000, key="pathway_baseline_emissions")
                annual_reduction_rate = st.slider("Annual Reduction Rate (%)", 0, 20, selected_scenario["reduction_rate"], key="pathway_reduction_rate")
                start_year_path = st.number_input("Pathway Start Year", min_value=2025, max_value=2050, value=2027, key="pathway_start_year")
                end_year_path = st.number_input("Pathway End Year", min_value=2026, max_value=2060, value=2035, key="pathway_end_year")

            if end_year_path <= start_year_path:
                st.warning("Pathway End Year must be greater than Pathway Start Year.")
            else:
                years = list(range(start_year_path, end_year_path + 1))
                emissions_path = []
                current_emissions = baseline_emissions

                for _year in years:
                    emissions_path.append(current_emissions)
                    current_emissions = current_emissions * (1 - annual_reduction_rate / 100)

                pathway_df = pd.DataFrame({"Year": years, "Emissions": emissions_path, "Sector": pathway_sector})
                cumulative_reduction = baseline_emissions - emissions_path[-1]

                with col2:
                    st.metric("Baseline Emissions", f"{baseline_emissions:,.0f} tCO2")
                    st.metric("Final Year Emissions", f"{emissions_path[-1]:,.0f} tCO2")
                    st.metric("Illustrative Reduction", f"{cumulative_reduction:,.0f} tCO2")

                fig_path = px.line(pathway_df, x="Year", y="Emissions", markers=True, title=f"Illustrative Emissions Pathway: {pathway_sector}")
                st.plotly_chart(fig_path, use_container_width=True)
                st.dataframe(pathway_df, use_container_width=True)

                st.markdown("#### Result Statement")
                st.info(f"Illustrative result: under the selected assumptions, emissions in **{pathway_sector}** decline by approximately **{cumulative_reduction:,.0f} tCO2** over the pathway period.")

                st.markdown("#### Learning Takeaway")
                st.write("This module shows that sector pathways may vary depending on cost, technology, and policy signals.")

        # 5
        elif exercise == "5. Allowance Market Balance":
            st.markdown("### 5. Allowance Market Balance")
            st.caption("Guided module: understand how allowance supply and demand shape market conditions.")

            col1, col2 = st.columns(2)

            with col1:
                total_supply = st.number_input("Total Allowance Supply", min_value=0, value=int(400 * selected_scenario["supply_multiplier"]), key="market_supply")
                demand_power = st.number_input("Demand: Power and Utilities", min_value=0, value=120, key="demand_power")
                demand_cement = st.number_input("Demand: Cement and Construction Materials", min_value=0, value=90, key="demand_cement")
                demand_petrochem = st.number_input("Demand: Petrochemical Value Chains", min_value=0, value=100, key="demand_petrochem")
                demand_metals = st.number_input("Demand: Metals and Materials", min_value=0, value=110, key="demand_metals")

            total_demand = demand_power + demand_cement + demand_petrochem + demand_metals
            market_gap = total_supply - total_demand

            with col2:
                st.metric("Total Supply", f"{total_supply:,.0f}")
                st.metric("Total Demand", f"{total_demand:,.0f}")
                st.metric("Market Balance", f"{market_gap:,.0f}")

            supply_demand_df = pd.DataFrame(
                {
                    "Category": [
                        "Allowance Supply",
                        "Power Demand",
                        "Cement Demand",
                        "Petrochemicals Demand",
                        "Metals Demand",
                        "Total Demand",
                    ],
                    "Value": [
                        total_supply,
                        demand_power,
                        demand_cement,
                        demand_petrochem,
                        demand_metals,
                        total_demand,
                    ],
                }
            )

            fig_balance = px.bar(supply_demand_df, x="Category", y="Value", title="Illustrative Allowance Supply and Demand")
            st.plotly_chart(fig_balance, use_container_width=True)

            st.markdown("#### Result Statement")
            if market_gap > 0:
                st.success(f"Illustrative result: supply exceeds demand by **{market_gap:,.0f}**, suggesting lower scarcity pressure.")
            elif market_gap < 0:
                st.warning(f"Illustrative result: demand exceeds supply by **{abs(market_gap):,.0f}**, suggesting higher scarcity pressure.")
            else:
                st.info("Illustrative result: supply and demand are balanced in this case.")

            st.markdown("#### Learning Takeaway")
            st.write("This module demonstrates that market pressure depends on the relationship between supply and demand.")

        # 6
        elif exercise == "6. Carbon Allowance Trading Desk":
            st.markdown("### 6. Carbon Allowance Trading Desk")
            st.caption("Guided module: demonstrate allowance exchange between firms in a simplified market.")

            if "firms_data" not in st.session_state:
                st.session_state.firms_data = pd.DataFrame({
                    "Firm": ["Cement Co.", "Steel Co.", "Power Co.", "Petrochem Co."],
                    "Sector": ["Cement", "Steel", "Power", "Petrochemicals"],
                    "Emissions": [120, 90, 150, 110],
                    "Allowances": [100, 110, 130, 120],
                })
                st.session_state.firms_data["Position"] = st.session_state.firms_data["Allowances"] - st.session_state.firms_data["Emissions"]

            if "trade_log" not in st.session_state:
                st.session_state.trade_log = []

            firms_data = st.session_state.firms_data
            st.dataframe(firms_data, use_container_width=True)

            carbon_price_trade = st.slider("Current Carbon Price ($/tCO2)", 20, 150, selected_scenario["carbon_price"], key="trading_carbon_price")

            buyers = firms_data[firms_data["Position"] < 0]["Firm"].tolist()
            sellers = firms_data[firms_data["Position"] > 0]["Firm"].tolist()

            st.markdown("#### Execute Illustrative Trade")

            if buyers and sellers:
                buyer = st.selectbox("Buyer Firm", buyers, key="trade_buyer")
                seller = st.selectbox("Seller Firm", sellers, key="trade_seller")

                buyer_gap = abs(firms_data.loc[firms_data["Firm"] == buyer, "Position"].values[0])
                seller_surplus = firms_data.loc[firms_data["Firm"] == seller, "Position"].values[0]
                max_trade = int(min(buyer_gap, seller_surplus))

                quantity = st.number_input("Allowances to Trade", min_value=1, max_value=max_trade if max_trade > 0 else 1, value=1, key="trade_quantity")

                if st.button("Execute Trade"):
                    buyer_idx = firms_data[firms_data["Firm"] == buyer].index[0]
                    seller_idx = firms_data[firms_data["Firm"] == seller].index[0]

                    st.session_state.firms_data.loc[buyer_idx, "Allowances"] += quantity
                    st.session_state.firms_data.loc[seller_idx, "Allowances"] -= quantity
                    st.session_state.firms_data["Position"] = st.session_state.firms_data["Allowances"] - st.session_state.firms_data["Emissions"]

                    st.session_state.trade_log.append({
                        "Buyer": buyer,
                        "Seller": seller,
                        "Quantity": quantity,
                        "Price": carbon_price_trade,
                        "Value": quantity * carbon_price_trade,
                    })

                    st.success(f"Illustrative trade executed: {buyer} purchased {quantity} allowances from {seller}.")
                    st.rerun()
            else:
                st.warning("No valid buyers or sellers are currently available in this illustrative market state.")

            st.markdown("#### Transaction Log")
            if st.session_state.trade_log:
                trade_log_df = pd.DataFrame(st.session_state.trade_log)
                st.dataframe(trade_log_df, use_container_width=True)
            else:
                st.info("No trades have been executed yet.")

            if st.button("Reset Trading Desk"):
                st.session_state.firms_data = pd.DataFrame({
                    "Firm": ["Cement Co.", "Steel Co.", "Power Co.", "Petrochem Co."],
                    "Sector": ["Cement", "Steel", "Power", "Petrochemicals"],
                    "Emissions": [120, 90, 150, 110],
                    "Allowances": [100, 110, 130, 120],
                })
                st.session_state.firms_data["Position"] = st.session_state.firms_data["Allowances"] - st.session_state.firms_data["Emissions"]
                st.session_state.trade_log = []
                st.rerun()

            st.markdown("#### Result Statement")
            st.info(
                "Illustrative result: trades can occur when one firm faces a shortfall and another holds a surplus."
            )

            st.markdown("#### Learning Takeaway")
            st.write("This module helps stakeholders visualize how market exchange may work in practice.")

        # 7
        elif exercise == "7. Carbon Market Design Lab":
            st.markdown("### 7. Carbon Market Design Lab")
            st.caption("Guided module: explore how ECS design choices may shape scarcity and price signals.")

            col1, col2 = st.columns(2)

            with col1:
                cap_type = st.selectbox("Cap Design", ["Absolute Cap", "Intensity-Based Cap"], key="design_cap_type")
                cap_stringency = st.slider("Cap Stringency (% reduction)", 5, 50, 20, key="design_cap_stringency")
                allocation_method = st.selectbox(
                    "Allocation Method",
                    [
                        "Auctioning",
                        "Free Allocation (Benchmarking)",
                        "Free Allocation (Grandparenting)",
                        "Hybrid Allocation",
                    ],
                    key="design_allocation_method",
                )
                price_floor = st.slider("Price Floor ($/tCO2)", 0, 100, 20, key="design_price_floor")
                price_ceiling = st.slider("Price Ceiling ($/tCO2)", 50, 200, 120, key="design_price_ceiling")
                banking_allowed = st.checkbox("Banking Allowed", value=True, key="design_banking")
                offsets_allowed = st.checkbox("Offsets Allowed", value=False, key="design_offsets")

            base_supply = 500

            if cap_type == "Absolute Cap":
                allowance_supply = base_supply * (1 - cap_stringency / 100)
            else:
                allowance_supply = (base_supply * 0.95) * (1 - (cap_stringency * 0.8) / 100)

            market_demand = 420

            if allocation_method == "Auctioning":
                demand_adjustment = 15
            elif allocation_method == "Hybrid Allocation":
                demand_adjustment = 5
            else:
                demand_adjustment = -10

            if banking_allowed:
                demand_adjustment += 5
            if offsets_allowed:
                demand_adjustment -= 20

            adjusted_market_demand = market_demand + demand_adjustment
            scarcity = adjusted_market_demand - allowance_supply
            raw_price = 40 + scarcity * 0.12
            estimated_price = max(price_floor, min(price_ceiling, raw_price))

            with col2:
                st.metric("Allowance Supply", f"{allowance_supply:,.0f}")
                st.metric("Adjusted Market Demand", f"{adjusted_market_demand:,.0f}")
                st.metric("Estimated Carbon Price", f"${estimated_price:,.0f}")
                st.metric("Market Condition", "Scarcity" if scarcity > 0 else ("Surplus" if scarcity < 0 else "Balanced"))

            design_df = pd.DataFrame(
                {"Category": ["Allowance Supply", "Adjusted Market Demand"], "Value": [allowance_supply, adjusted_market_demand]}
            )

            fig_design = px.bar(design_df, x="Category", y="Value", title="Market Balance Under Selected Design")
            st.plotly_chart(fig_design, use_container_width=True)

            st.markdown("#### Result Statement")
            st.info(f"Illustrative result: the selected design produces an estimated carbon price of **${estimated_price:,.0f}/tCO2** under the current assumptions.")

            st.markdown("#### Learning Takeaway")
            st.write("This module shows how cap design, allocation, and flexibility settings can shape market conditions.")












        # 8
        elif exercise == "8. Integrated ECS Policy & Market Simulator":
            st.markdown("### 8. Integrated ECS Policy & Market Simulator")
            st.caption(
                "Integrated simulator: link policy design, allowance supply, market scarcity, carbon price, "
                "firm response, trading need, and emissions outcomes in one connected scenario flow."
            )

            # ---------------------------------
            # Scenario defaults from Administrator View
            # ---------------------------------
            active_scenario = st.session_state.get("policy_scenario", "Conservative Carbon Price")
            scenario_cfg = scenario_defaults[active_scenario]

            st.markdown("""
            <div class="sim-result-box">
                <b>Administrator scenario applied:</b> The integrated simulator starts from the training scenario
                selected in the Administrator View. Stakeholders can then adjust assumptions and run the scenario.
            </div>
            """, unsafe_allow_html=True)

            s1, s2, s3, s4 = st.columns(4)
            s1.metric("Scenario", active_scenario)
            s2.metric("Starting Carbon Price", f"${scenario_cfg['carbon_price']}/tCO2")
            s3.metric("Annual Price Increase", f"{scenario_cfg['annual_increase']}")
            s4.metric("Reduction Rate", f"{scenario_cfg['reduction_rate']}%")

            st.markdown("### Linked Flow")
            st.write(
                "Cap design → allowance supply → market scarcity → carbon price → firm decisions → trading need → sector emissions outcomes"
            )

            # ---------------------------------
            # Step 1: Policy Design
            # ---------------------------------
            st.markdown("### Step 1: Policy Design")

            dcol1, dcol2 = st.columns(2)

            with dcol1:
                st.markdown("""
                <div class="sim-step-card">
                    <div class="sim-step-title">Policy design assumptions</div>
                    <div class="sim-step-text">
                        These settings shape allowance supply and affect the market conditions faced by participants.
                    </div>
                </div>
                """, unsafe_allow_html=True)

                cap_type = st.selectbox(
                    "Cap Design",
                    ["Absolute Cap", "Intensity-Based Cap"],
                    key="integrated_cap_type",
                )

                cap_stringency = st.slider(
                    "Cap Stringency (% reduction)",
                    5,
                    50,
                    20,
                    key="integrated_cap_stringency",
                )

                allocation_method = st.selectbox(
                    "Allocation Method",
                    [
                        "Auctioning",
                        "Free Allocation (Benchmarking)",
                        "Free Allocation (Grandparenting)",
                        "Hybrid Allocation",
                    ],
                    key="integrated_allocation_method",
                )

            with dcol2:
                st.markdown("""
                <div class="sim-step-card">
                    <div class="sim-step-title">Flexibility settings</div>
                    <div class="sim-step-text">
                        These settings influence how constrained or flexible the market may be under the scenario.
                    </div>
                </div>
                """, unsafe_allow_html=True)

                banking_allowed = st.checkbox(
                    "Banking Allowed",
                    value=True,
                    key="integrated_banking",
                )

                offsets_allowed = st.checkbox(
                    "Offsets Allowed",
                    value=False,
                    key="integrated_offsets",
                )

                covered_sector = st.selectbox(
                    "Illustrative Sector",
                    list(sector_descriptions.keys()),
                    key="integrated_sector",
                )

            # ---------------------------------
            # Step 2: Market and Firm Assumptions
            # ---------------------------------
            st.markdown("### Step 2: Market and Firm Assumptions")

            mcol1, mcol2 = st.columns(2)

            with mcol1:
                st.markdown("""
                <div class="sim-step-card">
                    <div class="sim-step-title">Sector-level assumptions</div>
                    <div class="sim-step-text">
                        These assumptions shape baseline demand and the broader emissions context for the selected sector.
                    </div>
                </div>
                """, unsafe_allow_html=True)

                baseline_emissions = st.number_input(
                    "Baseline Sector Emissions (tCO2)",
                    min_value=100,
                    value=1000,
                    key="integrated_baseline_emissions",
                )

                sector_demand_factor = st.slider(
                    "Sector Demand Pressure",
                    50,
                    150,
                    100,
                    key="integrated_sector_demand_factor",
                )

                external_market_pressure = st.slider(
                    "External Market Pressure",
                    0,
                    50,
                    10,
                    key="integrated_external_market_pressure",
                )

            with mcol2:
                st.markdown("""
                <div class="sim-step-card">
                    <div class="sim-step-title">Firm-level assumptions</div>
                    <div class="sim-step-text">
                        These assumptions shape how one illustrative firm may respond under the resulting market conditions.
                    </div>
                </div>
                """, unsafe_allow_html=True)

                firm_emissions = st.number_input(
                    "Illustrative Firm Emissions (tCO2)",
                    min_value=10,
                    value=120,
                    key="integrated_firm_emissions",
                )

                abatement_cost = st.number_input(
                    "Firm Abatement Cost ($/tCO2)",
                    min_value=0,
                    value=int(40 * scenario_cfg["abatement_cost_multiplier"]),
                    key="integrated_abatement_cost",
                )

                reduction_potential = st.slider(
                    "Potential Abatement Quantity (tCO2)",
                    0,
                    100,
                    25,
                    key="integrated_reduction_potential",
                )

            # ---------------------------------
            # Run button
            # ---------------------------------
            run_sim = st.button("Run Simulation", type="primary")

            if run_sim:
                # ---------------------------------
                # Step 3: Linked simulation engine
                # ---------------------------------
                base_supply = 1000

                if cap_type == "Absolute Cap":
                    allowance_supply = base_supply * (1 - cap_stringency / 100)
                else:
                    allowance_supply = (base_supply * 0.95) * (1 - (cap_stringency * 0.8) / 100)

                allowance_supply = allowance_supply * scenario_cfg["allowance_multiplier"]

                if allocation_method == "Auctioning":
                    demand_adjustment = 40
                elif allocation_method == "Hybrid Allocation":
                    demand_adjustment = 20
                elif allocation_method == "Free Allocation (Benchmarking)":
                    demand_adjustment = 5
                else:
                    demand_adjustment = -10

                if banking_allowed:
                    demand_adjustment += 10
                if offsets_allowed:
                    demand_adjustment -= 25

                sector_demand = (baseline_emissions * sector_demand_factor) / 100
                total_market_demand = sector_demand + external_market_pressure + demand_adjustment

                market_balance = allowance_supply - total_market_demand
                scarcity = total_market_demand - allowance_supply

                raw_carbon_price = scenario_cfg["carbon_price"] + (scarcity * 0.08)
                carbon_price = max(5, round(raw_carbon_price, 1))

                illustrative_allowances_for_firm = allowance_supply / 10
                shortfall_before = max(firm_emissions - illustrative_allowances_for_firm, 0)

                actual_abatement = min(reduction_potential, firm_emissions)

                if abatement_cost < carbon_price:
                    firm_decision = "Abate first"
                    emissions_after = max(firm_emissions - actual_abatement, 0)
                else:
                    firm_decision = "Buy allowances first"
                    emissions_after = firm_emissions

                shortfall_after = max(emissions_after - illustrative_allowances_for_firm, 0)
                surplus_after = max(illustrative_allowances_for_firm - emissions_after, 0)

                trading_volume = shortfall_after
                final_sector_emissions = max(baseline_emissions - actual_abatement, 0)

                buy_cost_before = shortfall_before * carbon_price
                abatement_total_cost = actual_abatement * abatement_cost
                buy_cost_after = shortfall_after * carbon_price
                combined_cost = abatement_total_cost + buy_cost_after

                # ---------------------------------
                # Step 4: Results
                # ---------------------------------
                st.markdown("### Step 3: Integrated Results")

                r1, r2, r3, r4 = st.columns(4)
                r1.metric("Allowance Supply", f"{allowance_supply:,.0f}")
                r2.metric("Market Demand", f"{total_market_demand:,.0f}")
                r3.metric("Carbon Price", f"${carbon_price}/tCO2")
                r4.metric("Trading Volume", f"{trading_volume:,.0f}")

                r5, r6, r7, r8 = st.columns(4)
                r5.metric("Shortfall Before Action", f"{shortfall_before:,.0f}")
                r6.metric("Shortfall After Action", f"{shortfall_after:,.0f}")
                r7.metric("Final Sector Emissions", f"{final_sector_emissions:,.0f}")
                r8.metric("Firm Decision", firm_decision)

                result_df = pd.DataFrame(
                    {
                        "Stage": [
                            "Allowance Supply",
                            "Market Demand",
                            "Shortfall Before Action",
                            "Shortfall After Action",
                            "Final Sector Emissions",
                        ],
                        "Value": [
                            allowance_supply,
                            total_market_demand,
                            shortfall_before,
                            shortfall_after,
                            final_sector_emissions,
                        ],
                    }
                )

                fig_integrated = px.bar(
                    result_df,
                    x="Stage",
                    y="Value",
                    title="Integrated ECS Simulation Results",
                )
                st.plotly_chart(fig_integrated, use_container_width=True)

                # comparison chart
                compare_df = pd.DataFrame(
                    {
                        "Decision Option": ["Buy Only", "Abate + Buy Remaining"],
                        "Illustrative Cost": [buy_cost_before, combined_cost],
                    }
                )

                fig_compare = px.bar(
                    compare_df,
                    x="Decision Option",
                    y="Illustrative Cost",
                    title="Illustrative Firm Response Comparison",
                )
                st.plotly_chart(fig_compare, use_container_width=True)

                st.markdown("### System Interpretation")

                c1, c2 = st.columns(2)

                with c1:
                    st.markdown("""
                    <div class="sim-step-card">
                        <div class="sim-step-title">What happened in the market?</div>
                        <div class="sim-step-text">
                    """, unsafe_allow_html=True)

                    st.write(f"- Policy design produced an allowance supply of **{allowance_supply:,.0f}**.")
                    st.write(f"- Market demand was estimated at **{total_market_demand:,.0f}**.")
                    st.write(f"- Market balance was **{market_balance:,.0f}**.")
                    st.write(f"- The resulting illustrative carbon price was **${carbon_price}/tCO2**.")

                    st.markdown("</div></div>", unsafe_allow_html=True)

                with c2:
                    st.markdown("""
                    <div class="sim-step-card">
                        <div class="sim-step-title">How did the firm respond?</div>
                        <div class="sim-step-text">
                    """, unsafe_allow_html=True)

                    st.write(f"- The firm started with a shortfall of **{shortfall_before:,.0f}**.")
                    st.write(f"- Preferred response under this scenario: **{firm_decision}**.")
                    st.write(f"- Remaining shortfall after action: **{shortfall_after:,.0f}**.")
                    st.write(f"- Trading need was estimated at **{trading_volume:,.0f} allowances**.")

                    st.markdown("</div></div>", unsafe_allow_html=True)

                st.markdown("### Result Statement")
                if scarcity > 0 and abatement_cost < carbon_price:
                    st.success(
                        "Illustrative result: tighter market conditions increase the price signal, which makes abatement more attractive and reduces final emissions while still leaving some trading demand."
                    )
                elif scarcity > 0 and abatement_cost > carbon_price:
                    st.warning(
                        "Illustrative result: the market is scarce and the carbon price rises, but the firm still finds allowance purchasing more attractive than abatement in the short term."
                    )
                else:
                    st.info(
                        "Illustrative result: supply is relatively sufficient compared with demand, which reduces scarcity pressure and weakens the incentive for stronger abatement."
                    )

                st.markdown("### Learning Takeaway")
                st.write(
                    "This integrated simulator links policy design, allowance supply, scarcity, carbon price, firm behavior, trading need, and emissions outcomes within one connected scenario flow. It is the part of the lab where the system behaves as one linked model rather than as separate guided modules."
                )

            else:
                st.markdown("""
                <div class="sim-result-box">
                    Configure the scenario assumptions above, then click <b>Run Simulation</b> to generate
                    linked market and firm outcomes.
                </div>
                """, unsafe_allow_html=True)

    # ---------------------------------------------------
    # TAB 3: KEY INSIGHTS
    # ---------------------------------------------------
    with sim_tab3:
        st.markdown("### Key Insights")

        insight_col1, insight_col2 = st.columns(2)

        with insight_col1:
            st.markdown("""
            <div class="sim-card">
                <div class="sim-card-tag">Guided Modules</div>
                <div class="sim-card-title">Focused learning across specific topics</div>
                <div class="sim-card-text">
                    The first seven modules help stakeholders understand individual ECS concepts,
                    such as price signals, market balance, trading logic, firm choices,
                    and sector pathways, one topic at a time.
                </div>
            </div>
            """, unsafe_allow_html=True)

        with insight_col2:
            st.markdown("""
            <div class="sim-card">
                <div class="sim-card-tag">Integrated Simulator</div>
                <div class="sim-card-title">Linked system behavior</div>
                <div class="sim-card-text">
                    The eighth module brings policy design, market dynamics, firm response,
                    trading need, and emissions outcomes together within one linked scenario flow.
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class="sim-note">
            The lab is strongest when the guided modules are used to understand individual concepts first,
            and the integrated simulator is then used to test how those concepts interact within one scenario.
        </div>
        """, unsafe_allow_html=True)

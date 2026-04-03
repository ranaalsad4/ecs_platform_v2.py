import streamlit as st
import pandas as pd
import os
from datetime import datetime
import plotly.express as px








st.markdown("""
<style>
    .main {
        background: linear-gradient(180deg, #f7f9fc 0%, #eef4fb 100%);
    }

    .hero-box {
        background: linear-gradient(135deg, #123c73 0%, #1f5fa8 55%, #4f8edc 100%);
        padding: 2.2rem 2rem;
        border-radius: 22px;
        color: white;
        box-shadow: 0 12px 30px rgba(18, 60, 115, 0.18);
        margin-bottom: 1.25rem;
    }

    .hero-title {
        font-size: 2.6rem;
        font-weight: 800;
        line-height: 1.15;
        margin-bottom: 0.6rem;
    }

    .hero-subtitle {
        font-size: 1.08rem;
        opacity: 0.96;
        line-height: 1.7;
    }

    .section-card {
        background: white;
        padding: 1.3rem 1.2rem;
        border-radius: 18px;
        border: 1px solid #e6edf7;
        box-shadow: 0 8px 22px rgba(31, 95, 168, 0.08);
        min-height: 220px;
        margin-bottom: 1rem;
    }

    .section-card h3 {
        color: #163a70;
        font-size: 1.45rem;
        margin-bottom: 0.5rem;
    }

    .section-card p {
        color: #374151;
        line-height: 1.7;
        font-size: 1rem;
    }

    .mini-tag {
        display: inline-block;
        background: #e9f2ff;
        color: #174a8b;
        padding: 0.3rem 0.7rem;
        border-radius: 999px;
        font-size: 0.82rem;
        font-weight: 600;
        margin-bottom: 0.8rem;
    }

    .highlight-box {
        background: linear-gradient(135deg, #fff7db 0%, #fff0b8 100%);
        border-left: 6px solid #d4a017;
        padding: 1rem 1.2rem;
        border-radius: 14px;
        margin-top: 1rem;
        margin-bottom: 1rem;
        color: #6b4f00;
        font-size: 1.02rem;
        line-height: 1.7;
    }

    .insight-box {
        background: linear-gradient(135deg, #edf7ff 0%, #dceeff 100%);
        border-left: 6px solid #2f6ebd;
        padding: 1rem 1.2rem;
        border-radius: 14px;
        margin-top: 1rem;
        margin-bottom: 1rem;
        color: #173b70;
        font-size: 1rem;
        line-height: 1.7;
    }

    .metric-shell {
        background: white;
        border-radius: 18px;
        padding: 0.8rem;
        box-shadow: 0 8px 18px rgba(0,0,0,0.06);
        border: 1px solid #edf2f7;
    }
</style>
""", unsafe_allow_html=True)






# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------
st.set_page_config(
    page_title="ECS Stakeholder Learning and Engagement Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------
# LOGIN
# -------------------------------------------------------
USERNAME = "ecs_demo"
PASSWORD = "ecs2026"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("ECS Stakeholder Learning and Engagement Platform")
    st.write(
        "Please enter credentials to access the illustrative ECS stakeholder-facing platform."
    )

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Invalid username or password.")

    st.stop()

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
    st.markdown("""
    <div class="hero-box">
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
    <div class="highlight-box">
        <b>Illustrative prototype only.</b> This platform is intended for engagement, awareness,
        consultation, and learning purposes. It does not serve as a regulatory compliance system,
        enforcement mechanism, or allowance registry.
    </div>
    """, unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="metric-shell">', unsafe_allow_html=True)
        st.metric("Core Sections", "4")
        st.markdown('</div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-shell">', unsafe_allow_html=True)
        st.metric("Primary Focus", "Stakeholder Learning")
        st.markdown('</div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="metric-shell">', unsafe_allow_html=True)
        st.metric("Engagement Scope", "Consultation + Capacity Building")
        st.markdown('</div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="metric-shell">', unsafe_allow_html=True)
        st.metric("Simulation Type", "Illustrative Learning Lab")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("## Platform Modules")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="section-card">
            <div class="mini-tag">Module 1</div>
            <h3>Information & Awareness</h3>
            <p>
                Provides clear and accessible ECS information to help stakeholders understand the system,
                its purpose, its terminology, and its overall development journey. This module may include
                ECS overview materials, system logic, key concepts, FAQs, roadmap content, and supporting
                policy and guidance documents.
            </p>
            <p>
                <b>Purpose:</b> Build foundational understanding and improve stakeholder awareness of the ECS.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="section-card">
            <div class="mini-tag">Module 2</div>
            <h3>Stakeholder Engagement</h3>
            <p>
                Supports structured dialogue between the platform and stakeholders through consultation papers,
                feedback channels, engagement activities, workshops, sector discussions, meeting summaries,
                and announcements. This module is designed to make stakeholder interaction visible,
                organized, and continuous.
            </p>
            <p>
                <b>Purpose:</b> Facilitate consultation, participation, and two-way communication.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="section-card">
            <div class="mini-tag">Module 3</div>
            <h3>Capacity Building & Learning</h3>
            <p>
                Provides practical learning resources to strengthen stakeholder understanding of ECS-related
                concepts and readiness needs. This module may include learning modules, recorded workshops,
                MRV guidance, case studies, interactive explainers, and curated training resources tailored
                to different stakeholder groups.
            </p>
            <p>
                <b>Purpose:</b> Strengthen knowledge, readiness, and practical understanding.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="section-card">
            <div class="mini-tag">Module 4</div>
            <h3>ECS Learning Simulation Lab</h3>
            <p>
                An integrated simulation environment designed to help stakeholders understand how ECS logic
                may work in practice through guided learning exercises. The lab brings together firm compliance
                strategy, allowance trading market dynamics, carbon price pathways, sector decarbonization
                pathways, market balance, illustrative trading interaction, and design choices in one
                structured simulation experience.
            </p>
            <p>
                <b>Purpose:</b> Support learning through interactive simulation rather than static calculation.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## Why this platform matters")
    st.markdown("""
    <div class="insight-box">
        This platform is designed to help stakeholders move from basic awareness to deeper understanding.
        Rather than functioning as a compliance tool, it serves as a structured environment for learning,
        engagement, and dialogue. The combination of information, consultation, capacity building,
        and simulation makes the platform suitable for stakeholder-facing demonstrations and training.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Illustrative Stakeholder Journey")

    journey_df = pd.DataFrame(
        {
            "Stage": [
                "1. Build awareness",
                "2. Understand ECS concepts",
                "3. Participate in engagement activities",
                "4. Strengthen learning and readiness",
                "5. Explore ECS through simulation",
            ],
            "Illustrative Journey": [
                "Stakeholders begin by reviewing introductory ECS information and key messages.",
                "Users explore terminology, FAQs, guidance materials, and the broader ECS structure.",
                "Stakeholders engage through consultation materials, workshops, and feedback channels.",
                "Users access learning modules, MRV guidance, training resources, and practical explainers.",
                "Stakeholders interact with the ECS Learning Simulation Lab to understand market logic, firm behavior, sector pathways, and design choices.",
            ],
        }
    )

    st.dataframe(journey_df, use_container_width=True)

    st.markdown("## Platform Positioning")
    st.write(
        "This prototype is positioned as a stakeholder-facing platform for ECS learning and engagement. "
        "It is designed to communicate complex policy concepts in a more accessible way, while also "
        "supporting consultation and simulation-based understanding."
    )













# -------------------------------------------------------
# INFORMATION & AWARENESS
# -------------------------------------------------------






elif module == "Information & Awareness":
    st.title("Information & Awareness")

    st.write(
        "This section explains the ECS in a simple and accessible way. It is designed to support awareness, "
        "foundational understanding, and transparent communication with stakeholders."
    )

    info_tab1, info_tab2, info_tab3, info_tab4 = st.tabs(
        ["What is ECS?", "How It Works", "Key Concepts", "FAQs & Documents"]
    )

    with info_tab1:
        st.subheader("What is the ECS?")
        st.write(
            "The Emissions Compliance System (ECS) is an illustrative policy framework that can support "
            "emissions transparency, encourage lower-carbon action, and help stakeholders understand how "
            "emissions-related obligations may be structured."
        )

        st.markdown("**Why ECS may be introduced**")
        st.write("- To improve emissions transparency")
        st.write("- To support more informed climate and industrial policy")
        st.write("- To create clearer incentives for emissions reduction")
        st.write("- To strengthen long-term planning and system readiness")

        st.markdown("**Illustrative stakeholder groups**")
        st.write("- Industry participants")
        st.write("- Government and policy institutions")
        st.write("- Technical experts and verifiers")
        st.write("- Researchers and wider stakeholders")

    with info_tab2:
        st.subheader("How the ECS Works")
        st.write(
            "This section provides a simplified explanation of system logic so stakeholders can understand "
            "the overall structure without going into regulator-only operational detail."
        )

        process_df = pd.DataFrame(
            {
                "Step": [
                    "System design",
                    "Stakeholder consultation",
                    "Monitoring and reporting",
                    "Review of emissions information",
                    "Illustrative policy implementation",
                ],
                "Description": [
                    "Authorities define the overall policy structure and system objectives.",
                    "Stakeholders provide feedback through workshops, consultations, and meetings.",
                    "Participants track and report emissions information using agreed approaches.",
                    "Reported information is reviewed to support transparency and system functioning.",
                    "The system evolves through phased development, learning, and refinement.",
                ],
            }
        )
        st.dataframe(process_df, use_container_width=True)

    with info_tab3:
        st.subheader("Key Concepts and Terminology")

        concepts = {
            "Emissions Compliance System (ECS)": "A system designed to structure emissions-related obligations and support policy objectives.",
            "MRV": "Monitoring, Reporting, and Verification of emissions-related data.",
            "Allowance": "An illustrative unit representing permission associated with emissions within a policy framework.",
            "Carbon Price": "A value associated with emissions that can influence decisions and incentives.",
            "Cap": "A policy parameter that limits the amount of emissions or covered activity in the system.",
            "Stakeholder Engagement": "Structured dialogue with affected and interested parties during design and implementation.",
        }

        for term, definition in concepts.items():
            with st.expander(term):
                st.write(definition)

    with info_tab4:
        st.subheader("FAQs & Documents")

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

        docs_df = pd.DataFrame(
            {
                "Document": [
                    "ECS Overview Note",
                    "Introductory ECS Roadmap",
                    "Stakeholder Consultation Note",
                    "MRV Introductory Guide",
                    "Workshop Summary Pack",
                    "Illustrative ECS FAQ",
                ],
                "Category": [
                    "Overview",
                    "Roadmap",
                    "Consultation",
                    "Guidance",
                    "Workshops",
                    "FAQ",
                ],
                "Status": [
                    "Published",
                    "Published",
                    "Draft",
                    "Published",
                    "Draft",
                    "Published",
                ],
            }
        )
        st.dataframe(docs_df, use_container_width=True)

# -------------------------------------------------------
# STAKEHOLDER ENGAGEMENT
# -------------------------------------------------------
elif module == "Stakeholder Engagement":
    st.title("Stakeholder Engagement")

    st.write(
        "This section supports structured dialogue, consultation, and feedback collection. "
        "It is designed to facilitate stakeholder participation and visibility on engagement activities."
    )

    st.info(
        "This section is for engagement and consultation purposes only. It is not a compliance reporting or enforcement tool."
    )

    engagement_tab1, engagement_tab2, engagement_tab3, engagement_tab4 = st.tabs(
        [
            "Consultation Papers",
            "Submit Feedback",
            "Workshops & Meetings",
            "Engagement Calendar",
        ]
    )

    with engagement_tab1:
        st.subheader("Consultation Papers")
        papers_df = pd.DataFrame(
            {
                "Paper": [
                    "Consultation Paper 01 - ECS Objectives",
                    "Consultation Paper 02 - Stakeholder Roles",
                    "Consultation Paper 03 - MRV Readiness",
                    "Consultation Paper 04 - Illustrative Market Design",
                ],
                "Phase": [
                    "Design Phase",
                    "Design Phase",
                    "Pilot Phase",
                    "Pilot Phase",
                ],
                "Status": [
                    "Published",
                    "Draft",
                    "Draft",
                    "Draft",
                ],
            }
        )
        st.dataframe(papers_df, use_container_width=True)

    with engagement_tab2:
        st.subheader("Submit Feedback")

        with st.form("feedback_form"):
            name = st.text_input("Stakeholder Name")
            organization = st.text_input("Organization")

            stakeholder_group = st.selectbox(
                "Stakeholder Group",
                [
                    "Industry Stakeholder",
                    "Government / Public Institution",
                    "Technical Expert / Verifier",
                    "Research / Academic",
                    "Other",
                ],
            )

            engagement_phase = st.selectbox(
                "Engagement Phase",
                ["Design Phase", "Pilot Phase", "Operational Readiness Phase"],
            )

            feedback_type = st.selectbox(
                "Feedback Type",
                [
                    "General Comment",
                    "Consultation Feedback",
                    "Workshop Feedback",
                    "Technical Clarification",
                    "Learning Suggestion",
                ],
            )

            comment = st.text_area("Comment")
            submitted = st.form_submit_button("Submit Feedback")

            if submitted:
                feedback_row = {
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "stakeholder_name": name,
                    "organization": organization,
                    "stakeholder_group": stakeholder_group,
                    "engagement_phase": engagement_phase,
                    "feedback_type": feedback_type,
                    "comment": comment,
                }
                save_to_excel(FEEDBACK_FILE, feedback_row)
                st.success("Feedback submitted successfully.")

        feedback_df = load_excel(FEEDBACK_FILE)
        if not feedback_df.empty:
            st.markdown("---")
            st.subheader("Submitted Feedback")
            st.dataframe(feedback_df, use_container_width=True)

    with engagement_tab3:
        st.subheader("Workshops & Meetings")

        workshops_df = pd.DataFrame(
            {
                "Activity": [
                    "Technical Working Group",
                    "Sector Workshop",
                    "Public Consultation Session",
                    "Stakeholder Dialogue Meeting",
                ],
                "Purpose": [
                    "Discuss technical design elements and clarify concepts",
                    "Gather sector-specific views and identify concerns",
                    "Present consultation materials and receive stakeholder input",
                    "Enable direct dialogue on implementation and learning needs",
                ],
                "Illustrative Frequency": [
                    "Monthly",
                    "Quarterly",
                    "At policy milestones",
                    "As needed",
                ],
            }
        )
        st.dataframe(workshops_df, use_container_width=True)

    with engagement_tab4:
        st.subheader("Engagement Calendar")

        calendar_df = pd.DataFrame(
            {
                "Phase": [
                    "Design Phase",
                    "Pilot Phase",
                    "Operational Readiness Phase",
                ],
                "Illustrative Activities": [
                    "Consultation papers, technical meetings, stakeholder mapping, introductory workshops",
                    "Pilot discussions, MRV readiness sessions, targeted engagement workshops",
                    "Ongoing forums, update sessions, feedback collection, learning refreshers",
                ],
            }
        )
        st.dataframe(calendar_df, use_container_width=True)

# -------------------------------------------------------
# CAPACITY BUILDING & LEARNING
# -------------------------------------------------------
elif module == "Capacity Building & Learning":
    st.title("Capacity Building & Learning")

    st.write(
        "This section helps stakeholders build understanding of the ECS through structured learning materials, "
        "guidance content, and practical resources."
    )

    capacity_tab1, capacity_tab2, capacity_tab3, capacity_tab4 = st.tabs(
        [
            "Learning Modules",
            "Training Resources",
            "MRV Guidance",
            "Case Studies & Explainers",
        ]
    )

    with capacity_tab1:
        st.subheader("Learning Modules")

        modules_df = pd.DataFrame(
            {
                "Module": [
                    "ECS Fundamentals",
                    "Stakeholder Roles in ECS",
                    "Introduction to MRV",
                    "Understanding Carbon Price Signals",
                    "ECS Design and Policy Choices",
                ],
                "Purpose": [
                    "Build foundational understanding of ECS",
                    "Clarify how different stakeholders may engage with the system",
                    "Explain monitoring, reporting, and verification concepts",
                    "Introduce how price signals may influence decisions",
                    "Explain how design choices affect system outcomes",
                ],
            }
        )
        st.dataframe(modules_df, use_container_width=True)

    with capacity_tab2:
        st.subheader("Training Resources")
        st.write("- Introductory guidance notes")
        st.write("- Recorded workshop materials")
        st.write("- Slide packs and explanatory summaries")
        st.write("- Glossary of key ECS terms")
        st.write("- Frequently asked questions")
        st.write("- Illustrative exercises and learning prompts")

    with capacity_tab3:
        st.subheader("MRV Guidance")
        st.write(
            "This section provides simplified guidance on Monitoring, Reporting, and Verification (MRV) "
            "to support stakeholder awareness and readiness."
        )

        mrv_df = pd.DataFrame(
            {
                "Topic": [
                    "What is monitored?",
                    "How reporting works",
                    "Why verification matters",
                    "Why data quality matters",
                ],
                "Simple Explanation": [
                    "Stakeholders track relevant emissions-related information.",
                    "Reported data is submitted using agreed approaches and timelines.",
                    "Verification helps improve confidence in reported information.",
                    "Clear and reliable data supports transparency and system credibility.",
                ],
            }
        )
        st.dataframe(mrv_df, use_container_width=True)

    with capacity_tab4:
        st.subheader("Case Studies & Interactive Explainers")
        st.write(
            "Case studies and explainers can help stakeholders connect ECS concepts to practical examples "
            "and real policy design questions."
        )

        st.markdown("**Examples of learning content**")
        st.write("- How different sectors may experience transition differently")
        st.write("- How carbon price signals can influence planning decisions")
        st.write("- Why consultation matters during ECS design")
        st.write("- How policy choices may affect market behavior")
        st.write("- What stakeholders need to understand before implementation")

# -------------------------------------------------------
# SIMULATION & DEMONSTRATION
# -------------------------------------------------------



















elif module == "Simulation & Demonstration":

    st.header("ECS Learning Simulation Lab")

    st.write(
        "This simulation lab is designed to help stakeholders understand how an Emissions Compliance "
        "System (ECS) may function through guided learning exercises. It combines market logic, firm-level "
        "decision-making, sector pathways, and design choices in one integrated learning environment."
    )

    st.info(
        "Illustrative learning simulator only. This module is intended for stakeholder engagement and "
        "capacity building. It does not represent a live compliance system, registry, or enforcement mechanism."
    )

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

        st.write("**Current training configuration**")
        cfg1, cfg2, cfg3 = st.columns(3)
        cfg1.metric("Starting Carbon Price", f"${selected_scenario['carbon_price']}/tCO2")
        cfg2.metric("Annual Price Increase", f"{selected_scenario['annual_increase']}")
        cfg3.metric("Reduction Rate", f"{selected_scenario['reduction_rate']}%")

    # default if expander not touched
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

    # ---------------------------------------------------
    # MAIN TABS
    # ---------------------------------------------------
    sim_tab1, sim_tab2, sim_tab3 = st.tabs(
        [
            "Simulation Overview",
            "Interactive ECS Learning Simulator",
            "Key Insights",
        ]
    )

    # ---------------------------------------------------
    # TAB 1: OVERVIEW
    # ---------------------------------------------------
    with sim_tab1:
        st.subheader("Simulation Overview")
        st.caption(
            "Objective: Provide stakeholders with a structured overview of the main ECS learning areas covered in this lab."
        )

        ov1, ov2, ov3, ov4 = st.columns(4)
        ov1.metric("Learning Modules", "7")
        ov2.metric("Firm-Level Exercises", "2")
        ov3.metric("Market & Pathway Views", "3")
        ov4.metric("Design Explorer", "1")

        st.markdown("### What stakeholders can learn in this lab")

        overview_df = pd.DataFrame(
            {
                "Learning Area": [
                    "Firm Compliance Strategy",
                    "Allowance Trading Market",
                    "Carbon Price Pathways",
                    "Sector Decarbonization Pathways",
                    "Allowance Market Balance",
                    "Carbon Allowance Trading Desk",
                    "Carbon Market Design Lab",
                ],
                "What it helps explain": [
                    "How firms compare allowance purchase versus emissions reduction options.",
                    "How firms with surplus allowances can become sellers while others become buyers.",
                    "How changing price pathways may affect long-term planning.",
                    "How transition pathways may differ by sector.",
                    "How supply and demand interact to create scarcity or surplus.",
                    "How trades may occur between buyers and sellers in an illustrative market setting.",
                    "How design choices can shape scarcity, price signals, and stakeholder experience.",
                ],
            }
        )
        st.dataframe(overview_df, use_container_width=True)

        st.markdown("### Learning Journey")
        st.write(
            "This lab is designed as a stakeholder learning experience rather than a single calculator. "
            "Users move from understanding firm-level decisions to market dynamics, sector pathways, "
            "and finally broader ECS design choices."
        )

    # ---------------------------------------------------
    # TAB 2: INTERACTIVE ECS LEARNING SIMULATOR
    # ---------------------------------------------------
    with sim_tab2:
        st.subheader("Interactive ECS Learning Simulator")
        st.caption(
            "Objective: Allow stakeholders to explore how decisions, market conditions, and ECS design choices "
            "interact within one integrated simulation environment."
        )

        exercise = st.selectbox(
            "Select Learning Exercise",
            [
                "1. Firm Compliance Strategy",
                "2. Allowance Trading Market",
                "3. Carbon Price Pathways",
                "4. Sector Decarbonization Pathways",
                "5. Allowance Market Balance",
                "6. Carbon Allowance Trading Desk",
                "7. Carbon Market Design Lab",
            ],
            key="learning_exercise",
        )

        # -----------------------------
        # 1. Firm Compliance Strategy
        # -----------------------------
        if exercise == "1. Firm Compliance Strategy":
            st.markdown("### 1. Firm Compliance Strategy")
            st.caption(
                "Objective: Understand how firms evaluate whether to buy allowances or reduce emissions."
            )

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

                carbon_price = st.slider(
                    "Carbon Price ($/tCO2)",
                    0,
                    200,
                    default_price,
                    key="firm_carbon_price",
                )
                emissions = st.number_input(
                    "Emissions (tCO2)",
                    min_value=0,
                    value=100,
                    key="firm_emissions",
                )
                allowances = st.number_input(
                    "Allowances Available",
                    min_value=0,
                    value=default_allowances,
                    key="firm_allowances",
                )
                abatement_cost = st.number_input(
                    "Abatement Cost ($/tCO2)",
                    min_value=0,
                    value=default_abatement_cost,
                    key="firm_abatement_cost",
                )
                abatement_amount = st.number_input(
                    "Potential Abatement Quantity (tCO2)",
                    min_value=0,
                    value=20,
                    key="firm_abatement_amount",
                )

            shortfall_before = max(emissions - allowances, 0)
            actual_abatement = min(abatement_amount, emissions)
            emissions_after = max(emissions - actual_abatement, 0)
            shortfall_after = max(emissions_after - allowances, 0)
            surplus_after = max(allowances - emissions_after, 0)

            compliance_cost_before = shortfall_before * carbon_price
            abatement_total_cost = actual_abatement * abatement_cost
            compliance_cost_after = shortfall_after * carbon_price
            total_cost_with_abatement = abatement_total_cost + compliance_cost_after
            sale_revenue_after = surplus_after * carbon_price

            with col2:
                st.markdown("#### Results")
                st.metric("Shortfall Before Action", f"{shortfall_before} tCO2")
                st.metric("Shortfall After Abatement", f"{shortfall_after} tCO2")
                st.metric("Buy-Only Cost", f"${compliance_cost_before:,.0f}")
                st.metric("Abatement + Remaining Purchase", f"${total_cost_with_abatement:,.0f}")

            chart_data = pd.DataFrame(
                {
                    "Option": ["Buy Only", "Abate + Buy Remaining"],
                    "Illustrative Cost": [compliance_cost_before, total_cost_with_abatement],
                }
            )

            fig = px.bar(
                chart_data,
                x="Option",
                y="Illustrative Cost",
                title="Illustrative Compliance Decision Comparison",
            )
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("#### Result Statement")
            if abatement_cost < carbon_price:
                st.success(
                    "Illustrative result: abatement appears more attractive than buying allowances alone, "
                    "because the cost of reducing emissions is lower than the carbon price."
                )
            elif abatement_cost > carbon_price:
                st.warning(
                    "Illustrative result: purchasing allowances may appear more attractive in the short term, "
                    "because the carbon price is lower than the cost of abatement."
                )
            else:
                st.info(
                    "Illustrative result: abatement and allowance purchase are broadly similar in cost in this case."
                )

            st.markdown("#### What This Means")
            st.write(
                f"For the **{selected_sector}** sector, this exercise shows how carbon price, allowance availability, "
                "and abatement cost interact to shape firm decision-making."
            )

            st.markdown("#### Learning Takeaway")
            st.write(
                "Stakeholders can see that firm behavior is influenced not by one number, but by the interaction "
                "between price signals, allowance availability, and technical abatement options."
            )

        # -----------------------------
        # 2. Allowance Trading Market
        # -----------------------------
        elif exercise == "2. Allowance Trading Market":
            st.markdown("### 2. Allowance Trading Market")
            st.caption(
                "Objective: Illustrate how firms with surpluses become sellers and firms with shortfalls become buyers."
            )

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
            market_df["Status"] = market_df["Position"].apply(
                lambda x: "Seller" if x > 0 else ("Buyer" if x < 0 else "Balanced")
            )
            market_df["Illustrative Cost"] = market_df["Position"].apply(
                lambda x: abs(x) * carbon_price_market if x < 0 else 0
            )

            st.dataframe(market_df, use_container_width=True)

            col1, col2 = st.columns(2)

            with col1:
                fig_status = px.bar(
                    market_df,
                    x="Firm",
                    y="Position",
                    color="Status",
                    title="Illustrative Firm Positions",
                )
                st.plotly_chart(fig_status, use_container_width=True)

            with col2:
                status_counts = market_df["Status"].value_counts().reset_index()
                status_counts.columns = ["Status", "Count"]
                fig_market = px.bar(
                    status_counts,
                    x="Status",
                    y="Count",
                    title="Buyers vs Sellers",
                )
                st.plotly_chart(fig_market, use_container_width=True)

            buyers = len(market_df[market_df["Status"] == "Buyer"])
            sellers = len(market_df[market_df["Status"] == "Seller"])

            st.markdown("#### Result Statement")
            st.info(
                f"Illustrative result: this market view shows **{buyers} buyer(s)** and **{sellers} seller(s)**, "
                "demonstrating how trading emerges when some firms have shortfalls and others have surpluses."
            )

            st.markdown("#### Learning Takeaway")
            st.write(
                "Trading does not occur in isolation. It emerges from differences in firm positions and the balance "
                "between allowance needs and available supply."
            )

        # -----------------------------
        # 3. Carbon Price Pathways
        # -----------------------------
        elif exercise == "3. Carbon Price Pathways":
            st.markdown("### 3. Carbon Price Pathways")
            st.caption(
                "Objective: Demonstrate how changing carbon price pathways may influence long-term planning."
            )

            col1, col2 = st.columns(2)

            with col1:
                start_year = st.number_input("Start Year", 2025, 2050, 2027, key="trajectory_start_year")
                end_year = st.number_input("End Year", 2026, 2060, 2035, key="trajectory_end_year")
                initial_price = st.number_input(
                    "Initial Carbon Price ($/tCO2)",
                    min_value=0,
                    value=selected_scenario["carbon_price"],
                    key="trajectory_initial_price",
                )
                annual_increase = st.number_input(
                    "Annual Price Increase ($/tCO2)",
                    min_value=0,
                    value=selected_scenario["annual_increase"],
                    key="trajectory_annual_increase",
                )

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

                fig_price = px.line(
                    trajectory_df,
                    x="Year",
                    y="Carbon Price",
                    markers=True,
                    title="Illustrative Carbon Price Path",
                )
                st.plotly_chart(fig_price, use_container_width=True)
                st.dataframe(trajectory_df, use_container_width=True)

                st.markdown("#### Result Statement")
                st.info(
                    f"Illustrative result: the carbon price rises from **${initial_price}/tCO2** "
                    f"to **${prices[-1]}/tCO2** over the selected period."
                )

                st.markdown("#### Learning Takeaway")
                st.write(
                    "A rising price path may strengthen the investment signal for lower-carbon technologies "
                    "and influence the timing of firm decisions."
                )

        # -----------------------------
        # 4. Sector Decarbonization Pathways
        # -----------------------------
        elif exercise == "4. Sector Decarbonization Pathways":
            st.markdown("### 4. Sector Decarbonization Pathways")
            st.caption(
                "Objective: Show how the pace of emissions reduction may differ by sector."
            )

            col1, col2 = st.columns(2)

            with col1:
                pathway_sector = st.selectbox(
                    "Sector",
                    list(sector_descriptions.keys()),
                    key="pathway_sector",
                )

                st.caption(sector_descriptions[pathway_sector])

                baseline_emissions = st.number_input(
                    "Baseline Emissions (tCO2)",
                    min_value=0,
                    value=1000,
                    key="pathway_baseline_emissions",
                )
                annual_reduction_rate = st.slider(
                    "Annual Reduction Rate (%)",
                    0,
                    20,
                    selected_scenario["reduction_rate"],
                    key="pathway_reduction_rate",
                )
                start_year_path = st.number_input(
                    "Pathway Start Year",
                    min_value=2025,
                    max_value=2050,
                    value=2027,
                    key="pathway_start_year",
                )
                end_year_path = st.number_input(
                    "Pathway End Year",
                    min_value=2026,
                    max_value=2060,
                    value=2035,
                    key="pathway_end_year",
                )

            if end_year_path <= start_year_path:
                st.warning("Pathway End Year must be greater than Pathway Start Year.")
            else:
                years = list(range(start_year_path, end_year_path + 1))
                emissions_path = []
                current_emissions = baseline_emissions

                for _year in years:
                    emissions_path.append(current_emissions)
                    current_emissions = current_emissions * (1 - annual_reduction_rate / 100)

                pathway_df = pd.DataFrame(
                    {"Year": years, "Emissions": emissions_path, "Sector": pathway_sector}
                )

                cumulative_reduction = baseline_emissions - emissions_path[-1]

                with col2:
                    st.metric("Baseline Emissions", f"{baseline_emissions:,.0f} tCO2")
                    st.metric("Final Year Emissions", f"{emissions_path[-1]:,.0f} tCO2")
                    st.metric("Illustrative Reduction", f"{cumulative_reduction:,.0f} tCO2")

                fig_path = px.line(
                    pathway_df,
                    x="Year",
                    y="Emissions",
                    markers=True,
                    title=f"Illustrative Emissions Pathway: {pathway_sector}",
                )
                st.plotly_chart(fig_path, use_container_width=True)
                st.dataframe(pathway_df, use_container_width=True)

                st.markdown("#### Result Statement")
                st.info(
                    f"Illustrative result: under the selected assumptions, emissions in **{pathway_sector}** "
                    f"decline by approximately **{cumulative_reduction:,.0f} tCO2** over the pathway period."
                )

                st.markdown("#### Learning Takeaway")
                st.write(
                    "Different sectors may face different transition speeds depending on technology availability, "
                    "costs, and policy signals."
                )

        # -----------------------------
        # 5. Allowance Market Balance
        # -----------------------------
        elif exercise == "5. Allowance Market Balance":
            st.markdown("### 5. Allowance Market Balance")
            st.caption(
                "Objective: Understand how total supply and demand interact to shape scarcity pressure."
            )

            col1, col2 = st.columns(2)

            with col1:
                total_supply = st.number_input(
                    "Total Allowance Supply",
                    min_value=0,
                    value=int(400 * selected_scenario["supply_multiplier"]),
                    key="market_supply",
                )
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

            fig_balance = px.bar(
                supply_demand_df,
                x="Category",
                y="Value",
                title="Illustrative Allowance Supply and Demand",
            )
            st.plotly_chart(fig_balance, use_container_width=True)

            st.markdown("#### Result Statement")
            if market_gap > 0:
                st.success(
                    f"Illustrative result: supply exceeds demand by **{market_gap:,.0f}**, suggesting lower scarcity pressure."
                )
            elif market_gap < 0:
                st.warning(
                    f"Illustrative result: demand exceeds supply by **{abs(market_gap):,.0f}**, suggesting higher scarcity pressure."
                )
            else:
                st.info("Illustrative result: supply and demand are balanced in this case.")

            st.markdown("#### Learning Takeaway")
            st.write(
                "Allowance scarcity is not fixed. It depends on the relationship between system-wide supply "
                "and demand across covered sectors."
            )

        # -----------------------------
        # 6. Carbon Allowance Trading Desk
        # -----------------------------
        elif exercise == "6. Carbon Allowance Trading Desk":
            st.markdown("### 6. Carbon Allowance Trading Desk")
            st.caption(
                "Objective: Demonstrate how firms may buy and sell allowances in a simplified trading environment."
            )

            if "firms_data" not in st.session_state:
                st.session_state.firms_data = pd.DataFrame({
                    "Firm": ["Cement Co.", "Steel Co.", "Power Co.", "Petrochem Co."],
                    "Sector": ["Cement", "Steel", "Power", "Petrochemicals"],
                    "Emissions": [120, 90, 150, 110],
                    "Allowances": [100, 110, 130, 120],
                })
                st.session_state.firms_data["Position"] = (
                    st.session_state.firms_data["Allowances"]
                    - st.session_state.firms_data["Emissions"]
                )

            if "trade_log" not in st.session_state:
                st.session_state.trade_log = []

            firms_data = st.session_state.firms_data
            st.dataframe(firms_data, use_container_width=True)

            carbon_price_trade = st.slider(
                "Current Carbon Price ($/tCO2)",
                20,
                150,
                selected_scenario["carbon_price"],
                key="trading_carbon_price",
            )

            buyers = firms_data[firms_data["Position"] < 0]["Firm"].tolist()
            sellers = firms_data[firms_data["Position"] > 0]["Firm"].tolist()

            st.markdown("#### Execute Illustrative Trade")

            if buyers and sellers:
                buyer = st.selectbox("Buyer Firm", buyers, key="trade_buyer")
                seller = st.selectbox("Seller Firm", sellers, key="trade_seller")

                buyer_gap = abs(firms_data.loc[firms_data["Firm"] == buyer, "Position"].values[0])
                seller_surplus = firms_data.loc[firms_data["Firm"] == seller, "Position"].values[0]
                max_trade = int(min(buyer_gap, seller_surplus))

                quantity = st.number_input(
                    "Allowances to Trade",
                    min_value=1,
                    max_value=max_trade if max_trade > 0 else 1,
                    value=1,
                    key="trade_quantity",
                )

                if st.button("Execute Trade"):
                    buyer_idx = firms_data[firms_data["Firm"] == buyer].index[0]
                    seller_idx = firms_data[firms_data["Firm"] == seller].index[0]

                    st.session_state.firms_data.loc[buyer_idx, "Allowances"] += quantity
                    st.session_state.firms_data.loc[seller_idx, "Allowances"] -= quantity

                    st.session_state.firms_data["Position"] = (
                        st.session_state.firms_data["Allowances"]
                        - st.session_state.firms_data["Emissions"]
                    )

                    st.session_state.trade_log.append({
                        "Buyer": buyer,
                        "Seller": seller,
                        "Quantity": quantity,
                        "Price": carbon_price_trade,
                        "Value": quantity * carbon_price_trade,
                    })

                    st.success(
                        f"Illustrative trade executed: {buyer} purchased {quantity} allowances from {seller}."
                    )
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
                st.session_state.firms_data["Position"] = (
                    st.session_state.firms_data["Allowances"]
                    - st.session_state.firms_data["Emissions"]
                )
                st.session_state.trade_log = []
                st.rerun()

            st.markdown("#### Result Statement")
            st.info(
                "Illustrative result: trades can occur when one firm faces a shortfall and another holds a surplus. "
                "This demonstrates the role of trading in balancing positions across participants."
            )

            st.markdown("#### Learning Takeaway")
            st.write(
                "The trading desk helps stakeholders visualize how allowance exchange may work in a simplified market environment."
            )

        # -----------------------------
        # 7. Carbon Market Design Lab
        # -----------------------------
        elif exercise == "7. Carbon Market Design Lab":
            st.markdown("### 7. Carbon Market Design Lab")
            st.caption(
                "Objective: Explore how ECS design choices can shape allowance scarcity and price signals."
            )

            col1, col2 = st.columns(2)

            with col1:
                cap_type = st.selectbox(
                    "Cap Design",
                    ["Absolute Cap", "Intensity-Based Cap"],
                    key="design_cap_type",
                )

                cap_stringency = st.slider(
                    "Cap Stringency (% reduction)",
                    5,
                    50,
                    20,
                    key="design_cap_stringency",
                )

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

                price_floor = st.slider(
                    "Price Floor ($/tCO2)",
                    0,
                    100,
                    20,
                    key="design_price_floor",
                )

                price_ceiling = st.slider(
                    "Price Ceiling ($/tCO2)",
                    50,
                    200,
                    120,
                    key="design_price_ceiling",
                )

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
                st.metric(
                    "Market Condition",
                    "Scarcity" if scarcity > 0 else ("Surplus" if scarcity < 0 else "Balanced")
                )

            design_df = pd.DataFrame(
                {
                    "Category": ["Allowance Supply", "Adjusted Market Demand"],
                    "Value": [allowance_supply, adjusted_market_demand],
                }
            )

            fig_design = px.bar(
                design_df,
                x="Category",
                y="Value",
                title="Market Balance Under Selected Design",
            )
            st.plotly_chart(fig_design, use_container_width=True)

            st.markdown("#### Result Statement")
            st.info(
                f"Illustrative result: the selected design produces an estimated carbon price of "
                f"**${estimated_price:,.0f}/tCO2** under the current assumptions."
            )

            st.markdown("#### Design Summary")
            st.write(f"- Cap design: **{cap_type}**")
            st.write(f"- Cap stringency: **{cap_stringency}%**")
            st.write(f"- Allocation method: **{allocation_method}**")
            st.write(f"- Price floor: **${price_floor}/tCO2**")
            st.write(f"- Price ceiling: **${price_ceiling}/tCO2**")
            st.write(f"- Banking allowed: **{'Yes' if banking_allowed else 'No'}**")
            st.write(f"- Offsets allowed: **{'Yes' if offsets_allowed else 'No'}**")

            st.markdown("#### Learning Takeaway")
            st.write(
                "ECS outcomes are shaped not only by market behavior but also by policy design choices "
                "such as cap type, stringency, allocation, and price containment."
            )

    # ---------------------------------------------------
    # TAB 3: KEY INSIGHTS
    # ---------------------------------------------------
    with sim_tab3:
        st.subheader("Key Insights")
        st.caption(
            "Objective: Summarize the main learning points stakeholders should take away from the simulation lab."
        )

        insight_col1, insight_col2 = st.columns(2)

        with insight_col1:
            st.markdown("### Firm and Market Behavior")
            st.write("- Firms with lower abatement costs may reduce emissions earlier.")
            st.write("- Firms with allowance surpluses may become potential sellers.")
            st.write("- Higher carbon prices strengthen incentives to abate rather than buy.")
            st.write("- Scarcity conditions can increase market pressure on buyers.")

        with insight_col2:
            st.markdown("### System and Design Implications")
            st.write("- Clear price pathways support planning and investment decisions.")
            st.write("- Sector transition pathways may differ significantly.")
            st.write("- Market balance depends on overall supply and demand.")
            st.write("- Design choices shape price signals and stakeholder experience.")

        st.markdown("### Final Learning Message")
        st.success(
            "This lab is designed to help stakeholders understand ECS logic through guided simulation exercises. "
            "It is not a calculator or operational market tool; it is a structured learning environment."
        )

import os
import time
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task, LLM

load_dotenv()

# ------------------------- PAGE CONFIG ---------------------------------------

st.set_page_config(
    page_title="DevCrew AI | Multi-Agent Studio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------- RGB NEON UI ---------------------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
    --bg: #090612;
    --panel: #120d22;
    --purple: #9b5cff;
    --cyan: #42e8ff;
    --pink: #ff4fd8;
    --text: #f4efff;
    --muted: #b4a9cc;
}

.stApp {
    background:
        radial-gradient(ellipse at 15% 0%, #29104a 0%, transparent 38%),
        radial-gradient(ellipse at 95% 10%, #102c4c 0%, transparent 32%),
        var(--bg);
    color: var(--text);
    font-family: Inter, sans-serif;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #160b2c, #0c1020 75%);
    border-right: 1px solid #713dba66;
}

h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif !important;
}

.hero {
    padding: 28px 30px;
    border: 1px solid #a45cff88;
    border-radius: 22px;
    background: linear-gradient(120deg, #25113dce, #10192bde);
    box-shadow: 0 0 28px #9b5cff20, inset 0 0 24px #42e8ff08;
    margin-bottom: 22px;
}

.eyebrow {
    color: var(--cyan);
    font-size: 12px;
    letter-spacing: 3px;
    font-weight: 800;
    text-transform: uppercase;
}

.hero-title {
    font-size: clamp(32px, 4vw, 48px);
    font-weight: 800;
    line-height: 1.1;
    margin: 10px 0;
}

.gradient-text {
    background: linear-gradient(90deg, #c79aff, #42e8ff, #ff70df);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-sub {
    color: #c6badf;
    font-size: 15px;
    max-width: 760px;
    line-height: 1.7;
}

.metric {
    background: #171029d9;
    border: 1px solid #8855c855;
    border-radius: 16px;
    padding: 16px;
    min-height: 95px;
}

.metric-label {
    color: #b8a9d3;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1.4px;
}

.metric-value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 22px;
    font-weight: 700;
    margin-top: 7px;
}

.agent-card {
    background: linear-gradient(135deg, #1a1230, #101a2a);
    border: 1px solid #7c55b855;
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 12px;
}

.agent-icon {
    font-size: 24px;
}

.agent-name {
    font-weight: 800;
    font-size: 15px;
    margin: 8px 0 5px;
}

.agent-desc {
    color: #b8accf;
    font-size: 12px;
    line-height: 1.6;
}

div.stButton > button[kind="primary"],
div.stFormSubmitButton > button[kind="primary"] {
    background: linear-gradient(90deg, #8b35ff, #526dff, #00c8e8);
    border: 0;
    color: white;
    border-radius: 12px;
    font-weight: 800;
    padding: 0.7rem 1.2rem;
    box-shadow: 0 0 22px #8b35ff44;
}

div.stButton > button[kind="secondary"] {
    border: 1px solid #a45cff99;
    color: #e9dfff;
    background: #1b1230;
    border-radius: 10px;
}

.stTextArea textarea,
.stTextInput input,
.stSelectbox div[data-baseweb="select"] {
    background: #100b1d !important;
    color: #f5efff !important;
    border-color: #7751a9 !important;
}

.stTabs [data-baseweb="tab"] {
    color: #d7c9ef;
}

.stTabs [aria-selected="true"] {
    border-bottom-color: #42e8ff !important;
    color: #42e8ff !important;
}

div[data-testid="stExpander"] {
    border: 1px solid #67458e88;
    border-radius: 12px;
    background: #120d20bb;
}

.small-muted {
    color: #a99abd;
    font-size: 12px;
}

.stAlert {
    border-radius: 12px;
}

hr {
    border-color: #6e4a8f55;
}
</style>
""", unsafe_allow_html=True)


# ------------------------- API KEY --------------------------------------------

def get_api_key():
    """Read the Gemini API key without displaying it."""
    key = (
        os.getenv("GEMINI_API_KEY")
        or os.getenv("GOOGLE_API_KEY")
    )

    if not key:
        try:
            key = (
                st.secrets.get("GEMINI_API_KEY")
                or st.secrets.get("GOOGLE_API_KEY")
            )
        except Exception:
            key = None

    return key.strip() if key else None


# ------------------------- CREW BUILDER --------------------------------------

def build_crew(
    api_key: str,
    model_name: str,
    idea: str,
    stack: str,
    constraints: str,
    depth: str,
):
    llm = LLM(
        model=model_name,
        api_key=api_key,
        temperature=0.2,
    )

    planner = Agent(
        role="Senior Software Architect and Project Planner",
        goal=(
            "Translate the user's software idea into a clear, realistic, "
            "implementation-ready plan."
        ),
        backstory=(
            "You are a pragmatic software architect. Clarify scope, modules, "
            "data flow, architecture and risks. Avoid inventing requirements."
        ),
        llm=llm,
        verbose=False,
        allow_delegation=False,
        max_iter=3,
    )

    developer = Agent(
        role="Senior Software Developer",
        goal=(
            "Produce readable, maintainable implementation guidance and "
            "starter code aligned with the approved plan."
        ),
        backstory=(
            "You are an experienced engineer. Prefer secure defaults, "
            "clear functions, input validation and useful comments. "
            "Never claim code was executed when it was not."
        ),
        llm=llm,
        verbose=False,
        allow_delegation=False,
        max_iter=3,
    )

    reviewer = Agent(
        role="Code Reviewer and Security Analyst",
        goal=(
            "Review the implementation for correctness, maintainability, "
            "security and missing edge cases."
        ),
        backstory=(
            "Look for unsafe execution, secrets in code, injection risks, "
            "error-handling gaps and mismatches with requirements."
        ),
        llm=llm,
        verbose=False,
        allow_delegation=False,
        max_iter=3,
    )

    qa = Agent(
        role="Quality Assurance and Test Engineer",
        goal=(
            "Create practical tests and a release-readiness checklist "
            "for the proposed implementation."
        ),
        backstory=(
            "Design positive, negative, boundary and failure-path tests. "
            "Clearly distinguish suggested tests from tests actually run."
        ),
        llm=llm,
        verbose=False,
        allow_delegation=False,
        max_iter=3,
    )

    plan_task = Task(
        description=(
            "Create a structured software development plan for this idea:\n"
            "{project_idea}\n\n"
            "Preferred stack: {tech_stack}\n"
            "Constraints: {constraints}\n"
            "Depth: {depth}\n\n"
            "Include the problem statement, assumptions, features, "
            "architecture, modules/files, data flow, dependencies, "
            "implementation milestones, risks and acceptance criteria."
        ),
        expected_output=(
            "A structured plan containing requirements, architecture, "
            "modules, milestones and acceptance criteria."
        ),
        agent=planner,
    )

    build_task = Task(
        description=(
            "Using the planner's output, produce an implementation "
            "blueprint and useful starter code for:\n{project_idea}\n\n"
            "Preferred stack: {tech_stack}\n"
            "Constraints: {constraints}\n"
            "Depth: {depth}\n\n"
            "Include a folder structure, key files, setup commands and "
            "core code snippets. Put code in fenced code blocks with "
            "filenames. Never include real secrets. If the project is "
            "large, deliver a runnable minimal version and next steps."
        ),
        expected_output=(
            "Implementation blueprint, folder structure, setup commands "
            "and filename-labelled starter code."
        ),
        agent=developer,
        context=[plan_task],
    )

    review_task = Task(
        description=(
            "Review the implementation blueprint and code. List critical "
            "issues first, followed by improvements. Check correctness, "
            "missing requirements, security, dependencies and error "
            "handling. Give actionable corrections.\n"
            "Project constraints: {constraints}"
        ),
        expected_output=(
            "A code review with findings by severity and actionable corrections."
        ),
        agent=reviewer,
        context=[build_task],
    )

    qa_task = Task(
        description=(
            "Create a QA plan. Include test name, input/setup, expected "
            "result and priority. Cover normal use, invalid input, boundary "
            "cases, API failures and security. Finish with a release checklist. "
            "Mark tests NOT RUN unless execution evidence is supplied."
        ),
        expected_output=(
            "A practical test matrix and release-readiness checklist, "
            "distinguishing proposed tests from executed tests."
        ),
        agent=qa,
        context=[plan_task, build_task, review_task],
    )

    crew = Crew(
        agents=[planner, developer, reviewer, qa],
        tasks=[plan_task, build_task, review_task, qa_task],
        process=Process.sequential,
        verbose=False,
    )

    inputs = {
        "project_idea": idea,
        "tech_stack": stack,
        "constraints": constraints or "No additional constraints supplied.",
        "depth": depth,
    }

    # Retry only temporary 503 service-unavailable errors.
    # Retries may repeat work and API usage if a run partially completed.
    for attempt in range(3):
        try:
            result = crew.kickoff(inputs=inputs)
            return result, crew

        except Exception as exc:
            error_text = str(exc).upper()

            temporary_503 = (
                "503" in error_text
                or "UNAVAILABLE" in error_text
                or "SERVICE UNAVAILABLE" in error_text
            )

            if temporary_503 and attempt < 2:
                wait_seconds = 2 ** (attempt + 1)
                time.sleep(wait_seconds)
            else:
                raise

    raise RuntimeError("The Gemini request failed after retries.")


# ------------------------- SIDEBAR --------------------------------------------

with st.sidebar:
    st.markdown("## ⚡ DevCrew **AI**")
    st.caption("MULTI-AGENT ENGINEERING STUDIO")
    st.markdown("---")

    st.markdown("### ⚙️ Runtime settings")

    model_name = st.selectbox(
        "Gemini model",
        [
            "gemini/gemini-3.8-flash",
            "gemini/gemini-3.6-flash",
        ],
        index=0,
        help=(
            "Choose a model supported by your Google AI Studio API key. "
            "Model availability can vary."
        ),
    )

    depth = st.selectbox(
        "Output depth",
        ["Advanced", "Detailed", "Compact"],
        index=0,
    )

    st.markdown("---")
    st.markdown("### 🤖 Agent squad")
    st.markdown("🟣 **Planner** · Requirements & architecture")
    st.markdown("🔵 **Developer** · Blueprint & starter code")
    st.markdown("🩷 **Reviewer** · Quality & security review")
    st.markdown("🟢 **QA Engineer** · Test matrix")

    st.markdown("---")
    st.markdown(
        '<p class="small-muted">Powered by CrewAI + Google Gemini. '
        'No OpenAI API required.</p>',
        unsafe_allow_html=True,
    )


# ------------------------- HEADER ---------------------------------------------

st.markdown("""
<div class="hero">
    <div class="eyebrow">✦ AUTONOMOUS ENGINEERING WORKFLOW</div>
    <div class="hero-title">
        Build smarter with <span class="gradient-text">DevCrew AI</span>
    </div>
    <div class="hero-sub">
        Turn a software idea into a development plan, implementation
        blueprint, code review, and QA strategy — with four specialized
        agents collaborating in a sequential CrewAI workflow.
    </div>
</div>
""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)

for col, label, value in [
    (m1, "AGENTS", "04 specialists"),
    (m2, "WORKFLOW", "Sequential"),
    (m3, "LLM PROVIDER", "Google Gemini"),
    (m4, "OUTPUT", "Build + Review + QA"),
]:
    with col:
        st.markdown(
            f'<div class="metric">'
            f'<div class="metric-label">{label}</div>'
            f'<div class="metric-value">{value}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )


# ------------------------- PROJECT FORM ---------------------------------------

st.write("")

left, right = st.columns([1.12, 0.88], gap="large")

with left:
    st.markdown("### 🧠 Define your software project")

    with st.form("project_form"):
        idea = st.text_area(
            "What do you want to build?",
            placeholder=(
                "Example: Build a task management web app with login, "
                "project boards, due dates, and a dashboard."
            ),
            height=140,
        )

        stack = st.text_input(
            "Preferred technology stack",
            value="Python, Streamlit, SQLite",
            help="Example: FastAPI, React, PostgreSQL",
        )

        constraints = st.text_area(
            "Requirements / constraints (optional)",
            placeholder=(
                "Example: beginner-friendly, responsive UI, secure input "
                "validation, no paid services."
            ),
            height=95,
        )

        submitted = st.form_submit_button(
            "⚡ Launch Agent Squad",
            type="primary",
            use_container_width=True,
        )


with right:
    st.markdown("### 🌌 Mission preview")

    for icon, title, description in [
        (
            "🧭", "01 / Plan",
            "Scope, architecture, modules, milestones and acceptance criteria."
        ),
        (
            "💻", "02 / Build",
            "Folder structure, setup instructions and starter code."
        ),
        (
            "🛡️", "03 / Review",
            "Bug risks, security concerns and actionable improvements."
        ),
        (
            "🧪", "04 / Test",
            "Test matrix, edge cases and release-readiness checklist."
        ),
    ]:
        st.markdown(
            f'<div class="agent-card">'
            f'<div class="agent-icon">{icon}</div>'
            f'<div class="agent-name">{title}</div>'
            f'<div class="agent-desc">{description}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    st.caption(
        "Generated code is a proposal. Review it before running; "
        "this app does not automatically execute generated code."
    )


# ------------------------- RUN CREW -------------------------------------------

if submitted:
    if not idea.strip():
        st.warning("Please describe your software idea before launching the agents.")

    else:
        api_key = get_api_key()

        if not api_key:
            st.error(
                "Gemini API key not found. Add GEMINI_API_KEY to your "
                ".env file in the project root, then restart Streamlit."
            )
            st.code(
                "GEMINI_API_KEY=your_new_api_key_here",
                language="text",
            )
            st.info(
                "Create or manage your API key at "
                "https://aistudio.google.com/apikey"
            )

        else:
            try:
                with st.status(
                    "CrewAI is coordinating your agent squad…",
                    expanded=True,
                ) as status:
                    st.write("🧭 Planner is defining requirements and architecture.")
                    st.write("💻 Developer is preparing the implementation blueprint.")
                    st.write("🛡️ Reviewer is checking risks and code quality.")
                    st.write("🧪 QA Engineer is preparing test scenarios.")

                    result, crew = build_crew(
                        api_key=api_key,
                        model_name=model_name,
                        idea=idea.strip(),
                        stack=stack.strip(),
                        constraints=constraints.strip(),
                        depth=depth,
                    )

                    st.session_state["devcrew_result"] = str(
                        getattr(result, "raw", result)
                    )

                    st.session_state["devcrew_tasks"] = [
                        {
                            "name": (
                                getattr(task, "name", None)
                                or getattr(
                                    getattr(task, "agent", None),
                                    "role",
                                    f"Task {i + 1}",
                                )
                            ),
                            "output": str(
                                getattr(
                                    getattr(task, "output", None),
                                    "raw",
                                    getattr(task, "output", ""),
                                )
                            ),
                        }
                        for i, task in enumerate(crew.tasks)
                    ]

                    st.session_state["devcrew_idea"] = idea.strip()
                    st.session_state["devcrew_time"] = datetime.now().strftime(
                        "%Y-%m-%d %H:%M"
                    )

                    status.update(
                        label="Agent workflow completed",
                        state="complete",
                        expanded=False,
                    )

                st.success("Your DevCrew AI report is ready!")

            except Exception as exc:
                error_text = str(exc)
                error_upper = error_text.upper()

                st.error("The CrewAI workflow could not be completed.")

                if (
                    "503" in error_upper
                    or "UNAVAILABLE" in error_upper
                    or "SERVICE UNAVAILABLE" in error_upper
                ):
                    st.warning(
                        "Gemini is temporarily unavailable or experiencing "
                        "high demand. Wait a little and try again. The app "
                        "already attempted automatic retries."
                    )
                    st.markdown(
                        "[Gemini API troubleshooting guide]"
                        "(https://ai.google.dev/gemini-api/docs/troubleshooting)"
                    )

                elif (
                    "429" in error_upper
                    or "QUOTA" in error_upper
                    or "RESOURCE_EXHAUSTED" in error_upper
                ):
                    st.warning(
                        "Gemini rate limit or quota may have been reached. "
                        "Check your API usage and model limits."
                    )
                    st.markdown(
                        "[Google AI Studio]"
                        "(https://aistudio.google.com/)"
                    )

                elif (
                    "401" in error_text
                    or "403" in error_text
                    or "API KEY" in error_upper
                    or "AUTHENTICATION" in error_upper
                    or "PERMISSION DENIED" in error_upper
                ):
                    st.warning(
                        "Check that your API key is valid and that your "
                        "account has access to the selected model."
                    )

                elif (
                    "404" in error_text
                    or "NOT FOUND" in error_upper
                ):
                    st.warning(
                        "The selected model may not be available to your "
                        "API key. Verify its exact model ID in Google's "
                        "official model list."
                    )
                    st.markdown(
                        "[Gemini models]"
                        "(https://ai.google.dev/gemini-api/docs/models)"
                    )

                else:
                    st.warning(
                        "Check the diagnostic below. It may indicate a "
                        "configuration, dependency, or provider issue."
                    )

                # Do not print the API key or environment variables here.
                st.code(error_text[:3000], language="text")


# ------------------------- RESULTS --------------------------------------------

if st.session_state.get("devcrew_result"):
    st.markdown("---")
    st.markdown("## ✨ Mission results")

    st.caption(
        f"Project: {st.session_state.get('devcrew_idea', 'Software project')} "
        f"· Generated: {st.session_state.get('devcrew_time', '')}"
    )

    tab_names = [
        "📦 Final output",
        "🧭 Plan",
        "💻 Build",
        "🛡️ Review",
        "🧪 QA",
    ]

    tabs = st.tabs(tab_names)
    tasks = st.session_state.get("devcrew_tasks", [])

    with tabs[0]:
        st.markdown(st.session_state["devcrew_result"])

        st.download_button(
            "⬇️ Download full report (.md)",
            data="# DevCrew AI Report\n\n"
            + st.session_state["devcrew_result"],
            file_name="devcrew_report.md",
            mime="text/markdown",
        )

    for idx, tab in enumerate(tabs[1:]):
        with tab:
            if idx < len(tasks) and tasks[idx].get("output"):
                st.markdown(tasks[idx]["output"])
            else:
                st.info(
                    "This task did not return a separate output. "
                    "See the Final output tab."
                )

else:
    st.markdown("---")
    st.markdown("### 🚀 Ready when you are")
    st.markdown(
        "Describe your project and launch the squad to generate your "
        "first engineering report."
    )
    st.caption(
        "Tip: try “Build a personal expense tracker with categories, "
        "monthly summaries, CSV export, and a responsive dashboard.”"
    )

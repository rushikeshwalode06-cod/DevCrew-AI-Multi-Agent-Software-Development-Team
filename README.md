# 🤖 DevCrew-AI-Multi-Agent-Software-Development-Team

⚡ DevCrew AI is an intelligent multi-agent software development platform built with CrewAI, Google Gemini API, and Streamlit. It transforms software ideas into development plans, starter code, architecture blueprints, security reviews, and QA test strategies using four specialized AI agents in a futuristic RGB neon dashboard.

# ⚡ DevCrew AI — Intelligent Multi-Agent Engineering Studio

### 🤖 Transform Software Ideas into Development Plans, Starter Code, Code Reviews & QA Strategies

DevCrew AI is an AI-powered multi-agent software development platform built using **CrewAI, Google Gemini API, and Streamlit**. It converts software ideas into structured development plans, implementation blueprints, code reviews, and quality assurance strategies through four specialized AI agents working together in a sequential workflow.

## 🌟 Key Features

- 🧭 **AI Project Planning:** Generate project requirements, architecture, modules, milestones, and acceptance criteria.
- 💻 **Implementation Blueprint:** Create folder structures, setup commands, implementation guidance, and starter code.
- 🛡️ **Automated Code Review:** Identify potential bugs, security risks, missing requirements, and code-quality improvements.
- 🧪 **Quality Assurance Planning:** Generate test scenarios, expected results, priorities, and release-readiness checklists.
- 🤖 **Multi-Agent Collaboration:** Coordinate four specialized agents using CrewAI.
- 🧠 **Google Gemini Integration:** Use Gemini models to generate intelligent development recommendations.
- 🎨 **RGB Neon Dashboard:** Explore a modern dark-purple interface with neon purple, cyan, and pink styling.
- ⚙️ **Custom Project Configuration:** Enter a project idea, preferred technology stack, requirements, and desired output depth.
- 📑 **Organized Reports:** View the final report and individual task outputs in separate tabs.
- ⬇️ **Report Export:** Download the generated engineering report in Markdown format.
- 🔄 **Error Handling:** Display helpful guidance for temporary service errors, quota limits, authentication issues, and unavailable models.
- 🔐 **API Key Protection:** Read the Gemini API key from environment variables or Streamlit secrets instead of displaying it in the dashboard.

## 🧠 Multi-Agent Architecture

DevCrew AI uses four specialized AI agents to support different stages of software development.

### 🟣 1. Senior Software Architect and Project Planner

- 📌 Understands the user's software idea and requirements.
- 🏗️ Defines the project architecture and core modules.
- 🔄 Outlines the data flow and implementation milestones.
- 🎯 Establishes assumptions, risks, and acceptance criteria.

### 🔵 2. Senior Software Developer

- 💻 Creates the implementation blueprint.
- 📂 Suggests the project folder structure and key files.
- 🛠️ Provides setup instructions and starter code.
- 📋 Aligns implementation guidance with the project plan.

### 🩷 3. Code Reviewer and Security Analyst

- 🔍 Reviews the proposed implementation and code.
- 🐛 Identifies potential correctness and maintainability issues.
- 🔐 Checks for security risks and unsafe coding practices.
- 🧰 Recommends actionable corrections and improvements.

### 🟢 4. Quality Assurance and Test Engineer

- 🧪 Develops practical test scenarios.
- 📥 Defines test inputs and expected results.
- ⚠️ Covers invalid inputs, boundary cases, API failures, and security.
- ✅ Prepares a release-readiness checklist.

## 🔄 Workflow

1. 💡 **Submit an Idea:** Describe the software project you want to build.
2. ⚙️ **Configure Requirements:** Select the Gemini model, output depth, preferred technology stack, and optional constraints.
3. 🧭 **Plan:** The planner develops the requirements and architecture.
4. 💻 **Build:** The developer generates an implementation blueprint and starter code.
5. 🛡️ **Review:** The reviewer examines quality, security, and missing requirements.
6. 🧪 **Test:** The QA agent creates a test matrix and release checklist.
7. 📊 **Review Results:** Explore the final output and individual agent task results.
8. ⬇️ **Export:** Download the engineering report as a Markdown file.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core application programming language |
| 🖥️ Streamlit | Interactive web application and dashboard |
| 🤖 CrewAI | Multi-agent orchestration |
| ✨ Google Gemini API | AI-powered reasoning and generation |
| 🔗 LiteLLM integration through CrewAI | Model-provider communication |
| 🔑 Python dotenv | Loading environment variables |
| 🎨 HTML and CSS | Custom RGB neon interface |
| 🕒 Python datetime and time | Timestamps and retry delays |

## 📊 Dashboard Modules

- 🌌 **Mission Dashboard:** Displays the project introduction, agent squad, workflow, and runtime settings.
- 📝 **Project Input Form:** Collects the software idea, technology stack, and optional requirements.
- 🧭 **Mission Preview:** Explains the planning, building, reviewing, and testing stages.
- 📦 **Final Output:** Displays the complete generated engineering report.
- 💻 **Build Tab:** Shows the implementation blueprint and starter code when available.
- 🛡️ **Review Tab:** Presents the code-review output when available.
- 🧪 **QA Tab:** Presents testing recommendations and release-readiness guidance when available.
- ⬇️ **Report Download:** Exports the final report as `devcrew_report.md`.

## ⚙️ Configuration Options

- 🧠 **Gemini Model:** Choose from the model identifiers configured in the application. Actual availability depends on Google's API access.
- 📚 **Output Depth:** Select Advanced, Detailed, or Compact.
- 🧰 **Technology Stack:** Specify preferred technologies, such as Python, Streamlit, and SQLite.
- 📌 **Project Constraints:** Add optional requirements, limitations, or implementation preferences.
- 🔐 **API Authentication:** Configure a valid Google Gemini API key through environment variables or Streamlit secrets.

## 🔐 API Configuration and Error Handling

DevCrew AI uses the Google Gemini API and does not require an OpenAI API key.

- 🔑 The application checks `GEMINI_API_KEY` and `GOOGLE_API_KEY`.
- 🔒 API keys should be stored securely and never committed to a public repository.
- 🔄 Temporary HTTP 503 or service-unavailable errors trigger up to three total attempts.
- ⏳ HTTP 429 or quota errors display guidance to check usage and model limits.
- 🔑 Authentication errors provide guidance for checking the API key and access permissions.
- 🔎 Model-not-found errors direct users to verify the selected model identifier.

Useful resources:

- 🔐 [Google AI Studio — API Keys](https://aistudio.google.com/apikey)
- 📘 [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- 🧩 [Gemini API Models](https://ai.google.dev/gemini-api/docs/models)
- 🛠️ [Gemini API Troubleshooting](https://ai.google.dev/gemini-api/docs/troubleshooting)
- 🤖 [CrewAI Documentation](https://docs.crewai.com/)
- 🖥️ [Streamlit Documentation](https://docs.streamlit.io/)

## ⚠️ Important Limitations

- 📡 AI generation depends on Gemini API availability, account permissions, rate limits, and quota.
- 🧠 Generated plans and code are AI-produced suggestions and may require corrections.
- 🧪 The QA agent proposes test cases; the application does not automatically execute the generated code or prove that suggested tests pass.
- 🔍 Code reviews are AI-generated and should not replace professional security audits or manual testing.
- 🧩 Output quality depends on the clarity of the project idea, constraints, selected model, and available context.
- 🔑 The application requires a valid API key to generate results.

## 🚀 Future Enhancements

- 🧪 Automated execution of generated tests in an isolated environment.
- 📂 Export generated projects as downloadable ZIP files.
- 🧠 Support for additional AI providers and models.
- 📈 Agent execution monitoring and detailed progress tracking.
- 💾 Project history and report management.
- 🔍 Advanced static code analysis and automated linting.
- 🧑‍💻 GitHub integration for repository creation and pull-request workflows.
- 🌐 Collaborative project workspaces and team-based development.

## 🎯 Project Objective

The objective of DevCrew AI is to demonstrate how **agentic AI and multi-agent orchestration** can support software engineering workflows. By separating planning, implementation guidance, code review, and QA into specialized agents, the application helps users organize software ideas into a more structured development process.

## 🏁 Conclusion

DevCrew AI combines CrewAI, Google Gemini, and Streamlit to create an interactive AI-powered engineering studio.

- ⚡ Converts software ideas into structured development plans.
- 🤖 Coordinates four specialized AI agents.
- 💻 Generates implementation guidance and starter code.
- 🛡️ Encourages code quality and security review.
- 🧪 Supports test planning and release preparation.
- 🎨 Provides a modern RGB neon dashboard experience.



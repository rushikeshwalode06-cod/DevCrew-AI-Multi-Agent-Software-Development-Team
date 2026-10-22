# DevCrew AI — Multi-Agent Software Development Team

A Streamlit dashboard that uses CrewAI and Google Gemini to orchestrate four agents:
- Project Planner
- Software Developer
- Code Reviewer & Security Analyst
- QA Testing Engineer

## Requirements
- Python 3.10–3.13 recommended (use a version supported by your selected CrewAI release)
- Google AI Studio API key: https://aistudio.google.com/apikey
- VS Code

## Setup on Windows (VS Code)

1. Extract the project folder and open it in VS Code.
2. Open **Terminal → New Terminal**.
3. Create a virtual environment:

   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt terminal and run:

   ```bat
   .venv\Scripts\activate.bat
   ```

4. Install packages:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. Copy `.env.example` to `.env`, then replace the placeholder with your Gemini API key:

   ```env
   GEMINI_API_KEY=your_actual_key_here
   ```

6. Start the dashboard:

   ```powershell
   streamlit run app.py
   ```

7. Streamlit will print a local URL, usually `http://localhost:8501`.

## Notes
- The app explicitly configures a Gemini model through CrewAI's `LLM` interface. It does not require an OpenAI API key.
- If the selected Gemini model is unavailable to your account, select another supported model in the sidebar.
- API quotas and model availability depend on Google AI Studio account settings.
- Generated code is not automatically executed. Review it before using it.
- Never commit `.env` or publish your API key.

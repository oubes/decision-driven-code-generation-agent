# 🌀 Enterprise AI Data Intelligence Agent

<p align="center">
  <img src="https://img.shields.io/badge/Timeline-March%202026%20--%20Present-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active%20Development-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Architecture-LangGraph%20Agent-orange?style=for-the-badge" />
  <br/>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/LangGraph-🦜-white?style=for-the-badge" />
</p>

## 📖 Overview

An advanced **Agentic AI** system designed to bridge the gap between natural language and data science. By leveraging **LangGraph**, it autonomously decides whether to classify, reject, or analyze data requests, generating secure and executable Python code on the fly.

## 🚀 Key Features

* **⚡ Hybrid Reasoning**: Supports both Graph-based state machines (LangGraph) and deterministic decision loops for robust action selection.
* **🛡️ Multi-Layer Security**: Combines keyword-based authorization with **AST-based** static code analysis to prevent malicious execution.
* **📊 Dynamic Schema Injection**: Automatically interprets Excel structures, extracting `dtypes` and column names for the LLM context.
* **🌙 Dark-Themed UI**: A professional, high-contrast dashboard built with **FastAPI** for real-time data interaction.

## 🏗 System Workflow

The agent manages state transitions through a strictly defined hierarchy:

1. **Authorization**: Validates the query against forbidden keywords using `app/security`.
2. **Classification**: Categorizes the request state via `app/agent/decision`.
3. **LLM Analysis**: Generates Pandas code using the specialized client in `app/llm`.
4. **Validation & Execution**: Inspects code for safety before running it against the local `sales_dataset.xlsx`.

## 📂 Project Structure

The repository follows a strictly modular layout with all core components nested within the `app` package:

```text
├── app
│   ├── agent
│   │   ├── actions.py         # Graph node functions (classify, run_analysis)
│   │   ├── decision.py        # Logic for decide_action and loop-based execution
│   │   ├── graph.py           # LangGraph StateGraph definition
│   │   └── state.py           # AgentState TypedDict
│   ├── analysis
│   │   ├── code_extractor.py  # Markdown parsing for LLM output
│   │   ├── code_runner.py     # Secure execution environment
│   │   ├── code_validator.py  # AST security verification
│   │   └── prompt_builder.py  # Dynamic schema prompt engineering
│   ├── api
│   │   ├── routes.py          # FastAPI endpoints
│   │   └── schemas.py         # Pydantic request/response models
│   ├── data
│   │   └── sales_dataset.xlsx # Central enterprise dataset
│   ├── llm
│   │   └── llm_client.py      # OpenAI-compatible client configuration
│   ├── notebook
│   │   └── agent_walkthrough.ipynb # Step-by-step development guide
│   ├── security
│   │   └── authorization.py   # Keyword filtering and access control
│   ├── utils
│   │   ├── dataframe_loader.py # Excel processing and date parsing
│   │   └── result_formatter.py # Human-readable output formatting
│   ├── web
│   │   └── templates          # index.html (Dashboard)
│   ├── config.py              # Global settings & forbidden operation lists
│   └── main.py                # Application entry point
├── .env                       # API keys and environment secrets
└── requirements.txt           # Dependency list

```

## 🔒 Security & Guardrails

* **AST Validation**: Blocks `Import`, `With`, `While`, and `FunctionDef` nodes to prevent sandbox escapes.
* **Keyword Deny-List**: Prevents "export", "all records", or "entire dataset" requests via `app/security/authorization.py`.
* **Isolated LLM Scope**: The LLM only sees the schema (column names/types), never the raw data rows, ensuring privacy by design.

## 🛠 Installation & Setup

### 1. Environment Setup

```bash
git clone https://github.com/oubes/decision-driven-code-generation-agent.git
cd decision-driven-code-generation-agent
pip install -r requirements.txt

```

### 2. Run the Application

```bash
# Run from the root directory using the app module path
uvicorn app.main:app --reload

```

Navigate to `http://127.0.0.1:8000` to interact with the **Decision Driven Agent**.

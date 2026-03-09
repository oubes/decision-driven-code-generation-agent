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

* **⚡ Autonomous Reasoning**: Powered by a Directed Acyclic Graph (DAG) for multi-step decision-making and state management.
* **🛡️ AST-Based Security**: Real-time static analysis of LLM-generated code using Python's `ast` module to prevent malicious execution or data leaks.
* **📊 Dynamic Schema Injection**: Automatically interprets Excel/CSV structures, extracting `dtypes` and column names to provide precise context to the LLM.
* **🌙 Modern Analytics UI**: A high-contrast, dark-themed dashboard built with **FastAPI** and **Plus Jakarta Sans** for a premium analytical experience.

## 🏗 System Workflow

The agent manages state transitions through a strictly defined graph:

1. **Classify**: Validates the user question against `DENY_KEYWORDS` and authorization rules.
2. **Analyze**: Constructs a system prompt with the dataset's live schema and generates optimized Pandas code.
3. **Validate & Execute**: Inspects the code for forbidden nodes (imports, loops, functions) and runs it in a restricted global/local scope.
4. **Answer**: Formats the technical DataFrame/Series results into human-readable business insights.

## 📂 Project Structure

The repository follows a modular layout designed for enterprise maintainability:

```text
├── app
│   ├── agent
│   │   ├── actions.py      # Core node logic (classify_request, run_analysis)
│   │   ├── graph.py        # LangGraph StateGraph definition & compilation
│   │   └── state.py        # AgentState TypedDict definition
│   ├── analysis
│   │   ├── code_extractor.py  # Cleans and extracts Python code from LLM responses
│   │   ├── code_runner.py     # Secure execution environment for generated code
│   │   ├── code_validator.py  # AST-based safety verification (Security Layer)
│   │   └── prompt_builder.py  # Injects DF schema into the system prompt
│   ├── api
│   │   ├── routes.py       # FastAPI router for the Web UI and API
│   │   └── schemas.py      # Pydantic models for validation
│   ├── utils
│   │   ├── dataframe_loader.py # Handles data ingestion and date parsing
│   │   └── result_formatter.py # Formats pandas objects for user display
│   └── web
│       └── templates       # index.html (Dark-themed Dashboard)
├── data                    # Storage for sales_dataset.xlsx
├── config.py               # Security rules, forbidden nodes, and model settings
└── main.py                 # Application entry point

```

## 🔒 Security & Guardrails

To ensure data integrity and system safety, the agent enforces the following:

* **Node Blocking**: Using `ast.walk`, the system blocks nodes like `Import`, `With`, `While`, and `FunctionDef`.
* **Namespace Isolation**: The execution environment is restricted to a dictionary containing only the target `df` and no built-ins like `eval` or `open`.
* **Keyword Filtering**: Rejects queries containing keywords like "entire dataset", "all records", or "export".

## 🛠 Installation & Setup

### 1. Clone & Install

```bash
git clone https://github.com/your-username/agentic-data-intelligence.git
cd agentic-data-intelligence
pip install -r requirements.txt

```

### 2. Environment Configuration

Create a `.env` file in the root directory:

```env
DASHSCOPE_API_KEY=your_api_key_here

```

### 3. Launch the Application

```bash
uvicorn main:app --reload

```

Navigate to `http://127.0.0.1:8000` to access the dashboard.

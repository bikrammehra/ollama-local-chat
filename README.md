# 🚀 Local AI Chat App with Ollama & Streamlit

🤖 A complete guide to setting up and running your own local ChatGPT-style interface using open-source technology.

![Project Demo](https://img.shields.io/badge/Demo-Local_AI_Chat-blue) 
![Python Version](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running
- At least one Ollama model downloaded (e.g., `ollama pull llama2`)

## 🛠️ Installation

1. Clone the repository:
```bash
   git clone https://github.com/yourusername/ollama-streamlit-chat.git
```
Navigate to project directory:

```bash
   cd ollama-streamlit-chat
```
Install dependencies:

```bash
   pip install -r requirements.txt
```

🚀 Usage
Running the Application
Start Ollama in a separate terminal:

```bash
   ollama serve
```
Launch the Streamlit app:

```bash
   streamlit run app.py
```
Open your browser to http://localhost:8501

📂 Project Structure
```
├── app.py             # Main application logic
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```
🔧 Customization
Model Management
Add new models: ollama pull <model-name>

List installed models: ollama list

UI Customization
Edit app.py to modify:

Page title/icon (st.set_page_config)

Color scheme (using Streamlit themes)

Chat interface layout

Model Parameters
Modify the API request in app.py to adjust:

temperature

max_tokens

top_p

🚨 Troubleshooting
Common Issues
🔌 Connection Errors: Ensure Ollama is running in background

```bash
   ps aux | grep ollama
```
📦 Missing Models: Verify installed models

```bash
   ollama list
```
🐍 Python Dependencies: Confirm package versions

```bash
   pip freeze | grep -E 'streamlit|requests'
```
🤖 Supported Models
|Model Name	|Description|
|-----------|:-----------------------------:|
|llama2	|Meta's versatile LLM|
|mistral	|High-quality English/French model|
|codellama	|Specialized for programming tasks|
|phi3	|Lightweight Microsoft model|

📚 Explore more models at Ollama Library

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

💡 Pro Tip: Add export OLLAMA_HOST=127.0.0.1:11434 to your .bashrc for persistent Ollama configuration!

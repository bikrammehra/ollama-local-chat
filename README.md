# 🚀 Local AI Chat App with Ollama & Streamlit

🤖 A complete guide to setting up and running your own local ChatGPT-style interface using open-source technology.

## 📋 Prerequisites

- Python 3.8+
- Ollama installed and running ([Installation Guide](https://ollama.ai/))
- At least one Ollama model downloaded (e.g., \`ollama pull llama2\`)

## 🛠️ Installation

1. Clone this repository
   \`\`\`bash
   git clone https://github.com/yourusername/ollama-streamlit-chat.git
   \`\`\`
   
2. Navigate to project directory
   \`\`\`bash
   cd ollama-streamlit-chat
   \`\`\`
   
3. Install dependencies
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

## 🚦 Running the Application

1. Start Ollama in a separate terminal
   \`\`\`bash
   ollama serve
   \`\`\`
   
2. Run the Streamlit app
   \`\`\`bash
   streamlit run app.py
   \`\`\`
   
3. Open browser to \`http://localhost:8501\`

## 🧠 Project Structure

\`\`\`
.
├── app.py             # Main application logic
├── requirements.txt   # Python dependencies
└── README.md          # This documentation
\`\`\`

## 🔧 Customization

- **Add Models**: Use \`ollama pull <model-name>\` to add more models
- **UI Modifications**: Edit \`app.py\` to change:
  - Page title/icon
  - Color scheme
  - Chat interface layout
- **Model Parameters**: Modify temperature/max_tokens in API request

## 🚨 Troubleshooting

**Common Issues:**
- 🔌 Connection Errors: Ensure Ollama is running in background
- 📦 Missing Models: Use \`ollama list\` to verify installed models
- 🐍 Python Dependencies: Verify with \`pip freeze | grep streamlit\`

## 🤖 Available Models

Popular options:
- llama2
- mistral
- codellama
- phi3

Find more at [Ollama Library](https://ollama.ai/library)

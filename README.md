#!/bin/bash

# Create project structure
mkdir ollama-streamlit-chat
cd ollama-streamlit-chat

# Create Python script
cat > app.py <<EOF
import streamlit as st
import requests
import json

OLLAMA_URL = "http://localhost:11434/api/"

st.set_page_config(page_title="Ollama Chat", page_icon="🤖")
st.title("Ollama Chat App using local models")

def get_models():
    try:
        response = requests.get(f"{OLLAMA_URL}tags")
        return [model["name"] for model in response.json()["models"]]
    except Exception as e:
        st.error(f"Could not load models. Error: {e}")
        return []

with st.sidebar:
    st.header("Settings")
    models = get_models()
    if not models:
        st.error("No models found! Start Ollama and download models first.")
        st.stop()
    selected_model = st.selectbox("Choose Model", models)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    data = {
        "model": selected_model,
        "messages": st.session_state.messages,
        "stream": True
    }

    try:
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""
            
            with requests.post(
                f"{OLLAMA_URL}chat",
                json=data,
                stream=True
            ) as response:
                response.raise_for_status()
                
                for line in response.iter_lines():
                    if line:
                        chunk = json.loads(line.decode("utf-8"))
                        if content := chunk.get("message", {}).get("content", ""):
                            full_response += content
                            response_placeholder.markdown(full_response + "▌")
            
            response_placeholder.markdown(full_response)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})

    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {str(e)}")
    except json.JSONDecodeError:
        st.error("Failed to parse API response")
EOF

# Create requirements file
cat > requirements.txt <<EOF
streamlit==1.32.0
requests==2.31.0
EOF

# Create documentation
cat > README.md <<EOF
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
EOF

echo -e "\n\033[1;32m✅ Setup complete!\033[0m"
echo -e "Run these commands to start:\n"
echo -e "1. Start Ollama: \033[1;34mollama serve\033[0m"
echo -e "2. Install dependencies: \033[1;34mpip install -r requirements.txt\033[0m"
echo -e "3. Launch app: \033[1;34mstreamlit run app.py\033[0m\n"

import streamlit as st
import requests
import json

OLLAMA_URL = "http://localhost:11434/api/"

st.set_page_config(page_title="Ollama Chat")
st.title("Ollama Chat App using Local Models")

def get_models():
    try:
        response = requests.get(f"{OLLAMA_URL}tags")
        return [model['name'] for model in response.json()["models"]]
    except Exception as e:
        st.error(f"Could not load models. Error: {e}")
        return []

with st.sidebar:
    st.header("Settings")
    models = get_models()
    if not models:
        st.error("No Models found! Start Ollama and download models first.")
        st.stop()
    selected_model = st.selectbox("Choose Model", models)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role":"user", "content":prompt})

    with st.chat_message("user"):
        st.markdown(prompt)
    
    #Prepare the API request
    data = {
        "model" : selected_model,
        "messages": st.session_state.messages,
        "steam": True
    }

    try:
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""

            with requests.post(f"{OLLAMA_URL}chat", json=data, stream=True) as response: 
                response.raise_for_status()
                for line in response.iter_lines():
                    if line:
                        chunk = json.loads(line.decode("utf-8"))
                        if content := chunk.get("message", {}).get("content", ""):
                            full_response += content
                            response_placeholder.markdown(full_response + "▌")
            response_placeholder.markdown(full_response)
        st.session_state.messages.append({"role":"assistant", "content":full_response})
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed : {e}")
    except json.JSONDecodeError:
        st.error("Faield to parse API response")
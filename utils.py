
import os
import openai 
from datetime import datetime
import streamlit as st 




def configure_openai():
    openai_key = st.sidebar.text_input(label="OpenAI API Key",type="password", value=st.session_state["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.session_state else "", placeholder="sk...")
    
    if openai_key:
        st.session_state["OPENAI_API_KEY"] = openai_key 
        os.environ["OPENAI_API_KEY"] = openai_key
    else:
        st.error("Please add your OpenAI API Key")
        st.info("Obtain your key from this link: https://platform.openai.com/account/api-keys")
        st.stop()
    model = "gpt-3.5-turbo" #default model
    try:
        client = openai.Client()
        available_models = [{"id":i.id, "created": datetime.fromtimestamp(i.created)} for i in client.models.list() if str(i.id).startswith("gpt")]
        available_models = sorted(available_models, key = lambda x: x["created"])
        
        available_models = [i["id"] for i in available_models]
        
        model = st.sidebar.selectbox(label="Model",options=available_models,index=available_models.index(st.session_state["OPENAI_MODEL"]) if "OPENAI_MODEL" in st.session_state else 0)
        
        st.session_state["OPENAI_MODEL"] = model
    except openai.AuthenticationError as e:
        st.error(e.body["message"])
        st.stop()
    except Exception as e:
        print(e)
        st.error("Something is broken, please try again")
        st.stop()
    return model

def enable_chat_history(func):
    if os.environ.get("OPENAI_API_KEY"):
        
        if "messages" not in st.session_state:
           st.session_state["messages"]=[{"role":"assistant","content":"Hello, I am a bot from Tech Army 🇮🇳, how can I help you today?"}]
        
        for message in st.session_state["messages"]:
            st.chat_message(message["role"]).write(message["content"])
            
        def execute(*args, **kwargs):
            func(*args, **kwargs)
        return execute 
def display_message(author:str, message:str):
    st.session_state["messages"].append({"role":author,"content":message})
    st.chat_message(author).write(message)


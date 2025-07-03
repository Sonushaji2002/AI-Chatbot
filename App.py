import streamlit as st
import time
from Agent import call_agent

st.set_page_config(page_title="NeuroNet",layout="wide")
#TYPEWRITER EFFECT
def typewriter_display(text,delay=0.02):
    placeholder=st.empty()
    typed=""
    for char in text:
        typed+=char
        placeholder.markdown(typed + "▌")
        time.sleep(delay)
    placeholder.markdown(typed)
#STYLING
st.markdown("""
    <style>
    footer {visibility:hidden;}
    .block-container { max-width:800px;margin:auto;}
    .center-input {max-width:450px;margin:auto;}/* Narrow input box */
    div[data-testid="stButton"]button {
        position:fixed;
        bottom:20px;
        left:20px;
        border-radius:50%;
        width:50px;
        height:50px;
        font-size:28px;
        padding: 0;
        z-index: 999;
    }
    </style>
""",unsafe_allow_html=True)
#SESSION STATE
if "messages" not in st.session_state:
    st.session_state.messages = []
#CLEAR CHAT BUTTON
plus_clicked = st.button("🗘",key="clear_chat",help="New Chat",type="primary")
if plus_clicked:
    st.session_state.messages.clear()
#TITLE
st.markdown("<h1 style='text-align:center;color:#4CAF50;'>NeuroNet</h1>",unsafe_allow_html=True)
#DISPLAY OLD CHAT HISTORY
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
#CHAT INPUT
st.markdown('<div class="center-input">',unsafe_allow_html=True)
prompt = st.chat_input("Ask me anything")
st.markdown('</div>',unsafe_allow_html=True)
#HANDLE PROMPT
if prompt and prompt.strip():
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):
        try:
            response = call_agent(prompt)
        except Exception:
            response = "Sorry,something went wrong while generating a response."

    st.session_state.messages.append({"role":"assistant","content":response})
    with st.chat_message("assistant"):
        typewriter_display(response)



"""
#!/usr/bin/python3
-*- coding: utf-8 -*-
@Time    : 2023/2/23
@Author  : bleakie
@Email   : yangsai1991@163.com

"""
import time
import streamlit as st
from utils import CHATBOT

# Streamlit App
st.set_page_config(layout="wide",
                   page_title="智能客服",
                   page_icon='data/logo.jpg'
                   )

st.title("智能客服")
charbot = CHATBOT()


if 'history' not in st.session_state:
    st.session_state.history = []

if 'history' in st.session_state:
    for i, (query, response) in enumerate(st.session_state.history):
        with st.chat_message(name="user", avatar="user"):
            st.markdown(query)
        with st.chat_message(name="assistant", avatar="assistant"):
            st.markdown(response)
with st.chat_message(name="user", avatar="user"):
    input_placeholder = st.empty()
with st.chat_message(name="assistant", avatar="assistant"):
    message_placeholder = st.empty()

delay_time = 0.2
prompt_text = st.text_area(label="用户命令输入",
                           height=100,
                           placeholder="请在这儿输入您的命令")

button = st.button("发送", key="predict")

try:
    if button:
        input_placeholder.markdown(prompt_text)
        history = st.session_state.history
        start_time = time.time()
        response = charbot.output_content(prompt_text)
        answer = ''
        for event in response:
            message_placeholder.markdown(answer)
            event_time = time.time() - start_time
            event_text = event["choices"][0]["delta"]
            answer += event_text.get('content', '')
            time.sleep(delay_time)
        history.append((prompt_text, answer))
        st.session_state.history = history

except BaseException as e:
    with st.chat_message(name="assistant", avatar="assistant"):
        st.markdown(e)

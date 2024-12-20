#pip install python-dotenv
#pip install langchain-openai
#pip install streamlit

import openai
openai.api_key= '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'

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

#subject = "AI"
#result = chat_model.invoke(subject + "에 대한 시를써줘")
#print(result.content)

import streamlit as st

st.title("인공지능 시인")
subject = st.text_input("시의 주제을 입력해주세요.")
st.write(subject)

if st.button("시 작성"):
    with st.spinner("시 작성중 ..."):
        result = chat_model.invoke(subject + "에 대한 시를 써줘")
        st.write(result.content)
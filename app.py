import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    api_key = os.environ["OPENAI_API_KEY"],
    model_name = "gpt-4o-mini",
    temperature = 0.5
)

st.title("Streamlit LLM App!")
st.write("##### このアプリについての説明")
st.write("選択した専門家に対して質問を行うことができるアプリです")
st.write("##### 使い方")
st.write("質問したい専門家と質問内容を入力し、「回答を生成」ボタンを押すことで回答を生成できます。")
st.write("回答にはすこし時間がかかります")

st.divider()

selected_item = st.radio(
    "専門家を選択してください。",
    ["健康の専門家", "教育の専門家"]
)

if selected_item == "健康の専門家":
    input_text = st.text_input(label="健康の専門家への問いかけを入力してください。", placeholder="例: 健康について教えてください。")
    system_message = "あなたは健康に関するアドバイザーです。安全なアドバイスを提供してください。健康に関わる内容以外の問いかけには答えられない旨を説明してください。"
elif selected_item == "教育の専門家":
    input_text = st.text_input(label="教育の専門家への問いかけを入力してください。", placeholder="例: 教育について教えてください。")
    system_message = "あなたは教育に関するアドバイザーです。実用的なアドバイスを提供してください。教育に関わる内容以外の問いかけには答えられない旨を説明してください。"


# 回答生成ボタン
if st.button(label="回答を生成"):
    st.divider()
    
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_text),
    ]

    with st.spinner("回答を生成中..."):
        response = llm(messages)
        st.write(response.content)
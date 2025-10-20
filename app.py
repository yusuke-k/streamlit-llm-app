from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.title("Streamlit LLM App!")
st.write("##### このアプリについての説明")
st.write("選択した専門家に対して質問を行うことができるアプリです")
st.write("##### 使い方")
st.write("質問したい専門家と質問内容を入力し、「回答を生成」ボタンを押すことで回答を生成できます。")

st.divider()

selected_item = st.radio(
    "専門家を選択してください。",
    ["健康の専門家", "教育の専門家"]
)

if selected_item == "健康の専門家":
    input_text = st.text_input(label="健康の専門家への問いかけを入力してください。", placeholder="例: 健康について教えてください。")
elif selected_item == "教育の専門家":
    input_text = st.text_input(label="教育の専門家への問いかけを入力してください。", placeholder="例: 教育について教えてください。")


if st.button(label="回答を生成"):
    st.divider()
    st.write(f"回答: {input_text}")
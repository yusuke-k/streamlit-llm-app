from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.title(”Streamlit LLM App!”)

selected_item = st.radio(
    "専門家を選択してください。",
    ["健康の専門家", "教育の専門家"]
)

st.divider()

if selected_item == "健康の専門家":
    input_text = st.text_input(label="健康の専門家への問いかけを入力してください。", placeholder="例: 健康について教えてください。")
    if st.button(label="回答を生成"):
        st.write(f"回答: {input_text}")
elif selected_item == "教育の専門家":
    input_text = st.text_input(label="教育の専門家への問いかけを入力してください。", placeholder="例: 教育について教えてください。")
    if st.button(label="回答を生成"):
        st.write(f"回答: {input_text}")


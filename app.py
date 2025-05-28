import streamlit as st
from src.llm import get_llm_response
from src.api import get_stock_price

st.set_page_config(page_title="AI Financial Chatbot", layout="centered")

st.title("💬 AI-Powered Financial Chatbot")
st.markdown("Ask me anything about finance or investments.")

query = st.text_input("Type your question here 👇")

if query:
    with st.spinner("Thinking..."):
        if "stock price" in query.lower():
            response = get_stock_price(query)
        else:
            response = get_llm_response(query)

        st.success(response)

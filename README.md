# 💬 AI-Powered Financial Chatbot

An advanced chatbot that uses OpenAI's GPT and real-time stock data to answer finance-related queries.

## 🚀 Features
- Ask financial and investment-related questions
- Get real-time stock prices (e.g., AAPL, GOOGL)
- Built with Streamlit for a smooth web experience
- Modular code with separate LLM and API logic

## 🧠 Technologies Used
- [OpenAI GPT-3.5](https://platform.openai.com/docs/guides/gpt)
- [Streamlit](https://streamlit.io/)
- [Yahoo Finance API](https://pypi.org/project/yfinance/)
- [Python](https://www.python.org/)

## 📁 Folder Structure
```
financial-chatbot/
├── app.py                 # Streamlit app UI
├── requirements.txt       # Dependencies
├── src/
│   ├── llm.py             # Handles GPT-based queries
│   └── api.py             # Handles real-time stock data fetch
```

## ⚙️ Setup Instructions
1. **Clone the repo**:
```bash
git clone https://github.com/your-username/financial-chatbot.git
cd financial-chatbot
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Add OpenAI API key**:
Create a file called `.env`:
```
OPENAI_API_KEY=your-openai-api-key-here
```

4. **Run the app**:
```bash
streamlit run app.py
```

## 🌐 Example Questions
- "What's the current stock price of AAPL?"
- "Explain the difference between mutual funds and ETFs."
- "How should I start investing as a student?"

## 📌 Note
- You can deploy this app using [Streamlit Cloud](https://streamlit.io/cloud) for free.

## 👤 Author
Monish Sai — [GitHub](https://github.com/your-username)

---

> Built as part of a GenAI Job Simulation for BCG x Forage and enhanced to professional standards for use in technical hiring portfolios.

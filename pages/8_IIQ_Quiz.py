import streamlit as st
st.set_page_config(page_title="IIQ Testing Quiz", layout="wide")

# Define the questions, choices, and correct answers
questions = [
    {"question": "What is the main purpose of a Stock Market Analytics Table?", 
     "choices": ["To visualize stock prices", "To predict future stock prices", "To summarize financial data", "To manage stock portfolios"], 
     "answer": "To summarize financial data"},

    {"question": "What is Time Series Analysis primarily used for in stock market analytics?", 
     "choices": ["Predict future prices", "Analyze stock prices over time", "Track stock volume", "Understand risk metrics"], 
     "answer": "Analyze stock prices over time"},

    {"question": "Which chart is used to represent opening, closing, high, and low prices in stock market analysis?", 
     "choices": ["OHLC Chart", "Candlestick Chart", "Bar Chart", "Pie Chart"], 
     "answer": "Candlestick Chart"},

    {"question": "What does the Exponential Moving Average (EMA) give more weight to?", 
     "choices": ["Recent prices", "Old prices", "Volume", "Market news"], 
     "answer": "Recent prices"},

    {"question": "What does the MACD (Moving Average Convergence Divergence) Indicator measure?", 
     "choices": ["Price trends", "Momentum and trend", "Risk levels", "Stock volume"], 
     "answer": "Momentum and trend"},

    {"question": "What is the purpose of the Relative Strength Index (RSI) in technical analysis?", 
     "choices": ["Measure stock volume", "Identify overbought or oversold conditions", "Track stock prices", "Calculate volatility"], 
     "answer": "Identify overbought or oversold conditions"},

    {"question": "Which of the following is a volatility indicator?", 
     "choices": ["RSI", "VWAP", "Average True Range (ATR)", "MACD"], 
     "answer": "Average True Range (ATR)"},

    {"question": "What does the On-Balance Volume (OBV) indicator track?", 
     "choices": ["Price trends", "Volume flow", "Market sentiment", "Moving averages"], 
     "answer": "Volume flow"},

    {"question": "Which indicator is used to measure risk in the stock market?", 
     "choices": ["Ulcer Index", "RSI", "VWAP", "EMA"], 
     "answer": "Ulcer Index"},

    {"question": "Which technical analysis tool is used to identify price channels and support/resistance levels?", 
     "choices": ["Bollinger Bands", "RSI", "Candlestick Chart", "MACD"], 
     "answer": "Bollinger Bands"},

    {"question": "Which of these indicators is based on price and volume to calculate momentum?", 
     "choices": ["Stochastic Oscillator", "MACD", "Chaikin Money Flow (CMF)", "Fisher Transform"], 
     "answer": "Chaikin Money Flow (CMF)"},

    {"question": "Which of these indicators is used for momentum analysis?", 
     "choices": ["Stochastic Oscillator", "Volume Traded", "Cumulative Return", "Candlestick Patterns"], 
     "answer": "Stochastic Oscillator"},

    {"question": "Which analysis is used to understand the relationship between two stocks in the market?", 
     "choices": ["Relative Performance Comparison", "Cumulative Return", "Time Series Decomposition", "Volume Traded Analysis"], 
     "answer": "Relative Performance Comparison"},

    {"question": "What is the main goal of using the VWAP (Volume-Weighted Average Price)?", 
     "choices": ["Track stock price trends", "Determine average price weighted by volume", "Measure stock volatility", "Track moving averages"], 
     "answer": "Determine average price weighted by volume"},

    {"question": "What is a key feature of Time Series Decomposition?", 
     "choices": ["Identifying seasonal trends", "Predicting future stock prices", "Identifying overbought conditions", "Tracking price changes"], 
     "answer": "Identifying seasonal trends"},

    {"question": "Which of the following is a predictive modeling technique for stock market analysis?", 
     "choices": ["Random Forest Regressor", "Moving Averages", "RSI", "Bollinger Bands"], 
     "answer": "Random Forest Regressor"},

    {"question": "Which chart is typically used to analyze trading volume over time?", 
     "choices": ["OHLC Chart", "Volume Traded Over Time Chart", "Candlestick Chart", "SMA Chart"], 
     "answer": "Volume Traded Over Time Chart"},

    {"question": "Which of these tools is used to track the cumulative return of an investment?", 
     "choices": ["Cumulative Return Plot", "On-Balance Volume", "MACD", "Fisher Transform"], 
     "answer": "Cumulative Return Plot"},

    {"question": "What does the Fisher Transform indicator identify?", 
     "choices": ["Volatility", "Overbought conditions", "Momentum", "Stock volume"], 
     "answer": "Momentum"},

    {"question": "What term represents a price level at which a stock tends to stop falling and may even bounce back upwards?", 
     "choices": ["Support", "Resistance", "Breakout", "Trendline"], 
     "answer": "Support"}
]

# Initialize the session state if not already done
if "score" not in st.session_state:
    st.session_state.score = 0

# Display the quiz title
st.title("Quiz Time!")
st.write("Let's test your knowledge about stocks and stock indicators!")
# Display each question
user_answers = {}
for i, q in enumerate(questions):
    st.subheader(f"{i + 1}. {q['question']}")
    
    # Create radio buttons for choices
    user_answer = st.radio(f"Choose an answer:", q['choices'], key=f"q{i}")
    
    # Save the user's answer in the dictionary
    user_answers[f"q{i}"] = user_answer

# Function to check answers and calculate score
def check_answers():
    score = 0
    for i, q in enumerate(questions):
        if user_answers[f"q{i}"] == q["answer"]:
            score += 1
    return score

# Submit button to calculate the score
if st.button("Submit"):
    score = check_answers()
    st.session_state.score = score  # Store the score in session state
    st.success(f"Your score is: {score}/{len(questions)}")

# Display previous score
if st.session_state.score > 0:
    st.info(f"Previous Score: {st.session_state.score}/{len(questions)}")

st.sidebar.success("Select a page from the sidebar.")

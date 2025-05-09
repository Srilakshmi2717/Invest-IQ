import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Simulate Your Portfolio", layout="wide")
st.title("📊 Simulate Your Portfolio")

st.markdown("### Learn portfolio building with ₹1,00,000 virtual funds. Choose stocks, allocate amounts, and track simulated growth!")

st.sidebar.header("🧩 Simulation Controls")
num_stocks = st.sidebar.slider("How many stocks do you want to simulate?", 2, 10, 3)

stock_inputs = {}
total_amount = 0
virtual_fund = 100000

for i in range(num_stocks):
    symbol = st.sidebar.text_input(f"Stock {i+1} Symbol (e.g., INFY.NS)", key=f"symbol_{i}")
    allocation = st.sidebar.number_input(f"Allocation for {symbol}", min_value=0, max_value=virtual_fund, step=1000, key=f"alloc_{i}")
    
    if symbol:
        stock_inputs[symbol] = allocation
        total_amount += allocation

# Validation
if total_amount > virtual_fund:
    st.sidebar.error("🚫 Allocated amount exceeds ₹1,00,000!")
elif total_amount < virtual_fund:
    st.sidebar.warning(f"⚠️ ₹{virtual_fund - total_amount:,} unallocated.")
else:
    st.sidebar.success("✅ All funds allocated!")

# Date range
start_date = st.sidebar.date_input("From", pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("To", pd.to_datetime("today"))

# Run Simulation
if st.button("🚀 Run Simulation") and total_amount <= virtual_fund and stock_inputs:
    portfolio_df = pd.DataFrame()
    returns_data = pd.DataFrame()

    for symbol, investment in stock_inputs.items():
        try:
            stock_data = yf.download(symbol, start=start_date, end=end_date)
            close_price = stock_data.get("Close")
            if close_price is None:
                st.warning(f"⚠️ 'Close' price not available for {symbol}. Skipping.")
                continue

            stock_data["Daily Return"] = close_price.pct_change()
            stock_data["Investment Value"] = (stock_data["Daily Return"] + 1).cumprod() * investment
            portfolio_df[symbol] = stock_data["Investment Value"]
            returns_data[symbol] = stock_data["Daily Return"]

        except Exception as e:
            st.error(f"Failed to fetch data for {symbol}: {e}")

    if not portfolio_df.empty:
        portfolio_df["Total"] = portfolio_df.sum(axis=1)
        
        st.subheader("📈 Portfolio Value Over Time")
        st.line_chart(portfolio_df["Total"])

        st.subheader("📊 Final Investment Distribution")
        final_values = portfolio_df.iloc[-1][:-1]
        pie_df = pd.DataFrame({"Stock": final_values.index, "Value": final_values.values})
        fig = px.pie(pie_df, names='Stock', values='Value', title="End Value Distribution")
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("📉 Cumulative Return of Each Stock")
        cum_return = ((portfolio_df.iloc[-1][:-1] / list(stock_inputs.values())) - 1) * 100
        st.dataframe(cum_return.round(2).to_frame(name="Cumulative Return (%)"))

        st.success("💡 Tip: Diversifying your investments reduces risk. Try reallocating and rerunning the simulation!")

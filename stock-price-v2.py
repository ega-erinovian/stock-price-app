import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
    # Simple Stock Price App V2

    Shown are stock **closing price** and **volume** of Apple
""")

# get date input from user
st.sidebar.header("Input Date")
startDate = str(st.sidebar.date_input("Enter start date"))
endDate = str(st.sidebar.date_input("Enter end date"))

# define the ticker symbol
tickerSymbol = 'APPL'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices of this ticker
tickerDf = tickerData.history(period='id', start=startDate, end=endDate)

# Closing price
st.write(""" ## Closing Price """)
st.line_chart(tickerDf.Close)
# Volume price
st.write(""" ## Volume Price """)
st.line_chart(tickerDf.Volume)

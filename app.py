import yfinance as yf
import datetime
import plotly.graph_objects as go
import streamlit as st

st.write("# 주식 데이터 시각화 결과 보기")

ticker = st.text_input("티커 입력 >> ") #검색했을때 나오는거. ex. 테슬라 = TSLA
data = yf.Ticker(ticker)
today = datetime.datetime.today().strftime("%Y-%m-%d")
df = data.history(period="1d", start="2015-01-01", end=today) #1d = 하루 end = today : 오늘 날짜를 가져오는 방법
st.write(df)

candle = go.Candlestick(x=df.index, open=df["Open"], close=df["Close"], high=df["High"], low=df["Low"])
layout = go.Layout(yaxis={"fixedrange":False})
fig = go.Figure(data=[candle], layout=layout)
st.plotly_chart(fig) #streamlit 에서 이 기능을 제공해 줘서 좋음

st.write("### 거래량")
st.bar_chart(df["Volume"]) #005930.KS 국내는 이런식으로

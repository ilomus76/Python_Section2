#pip install yfinance

import yfinance as yf

#주식종목명(회사명)을 ticker 티커라고 부름 (회사명에 부여된 명칭)
ticker= "AAPL" # Apple Inc. 의 주식 티커 명칭
ticker= "005930.KS" #한국 주식의 경우 KS 또는 KQ 접미사 필요
stock= yf.Ticker(ticker=ticker)
print(stock)

info= stock.info
print('회사명:', info['longName'])
print('업종:', info['sector'])
print('사업요약:', info['longBusinessSummary'])
print('현재주가:', info['regularMarketPrice'], 'USD')
print("="*30)

#회사명을 넣으면 주식 티커를 반환해주는 기능 사용!
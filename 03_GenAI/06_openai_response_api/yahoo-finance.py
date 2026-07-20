# pip install yfinance 

import yfinance as yf

#주식종목명(회사명)을 ticker 티커라고 부름 (회사명에 부여된 명칭)
# ticker = "AAPL" # Applie Inc. 의 주식 티커 명칭
ticker = "005930.KS" # 한국 주식의 경우 KS 또는 KQ 접미사 필요
# ticker = "005930.ks" #소문자도 동작함. 
# ticker = "042660.KS" # 한국 주식의 경우 KS 또는 KQ 접미사 필요
# 삼성전자 ticker 구글 검색 : KRX: 005930
# 테슬라 ticker 구글 검색  : NASDAQ: TSLA
# 한화오션 ticker 구글 검색 : KRX: 042660
# 티커(Ticker)는 주식이나 ETF 등 금융 자산을 거래소에서 식별하기 위해 사용하는 고유한 종목 코드(약어)를 뜻합니다.
# 긴 회사 이름 대신 영문 알파벳 1~5글자를 사용하여 빠르게 종목을 검색하고 거래할 수 있습니다. (예: 애플은 AAPL, 테슬라는 TSLA)

stock = yf.Ticker(ticker=ticker) 

print(stock)  
#yfinance.Ticker object <AAPL>

info=stock.info
print('회사명:',info['longName'])
print('업종:',info['sector'])
print('사업요약:',info['longBusinessSummary'])
print('현재주가:',info['regularMarketPrice'],'USD')
print("="*30)



#회사명을 넣으면 주식 티커를 반환해주는 기능 사용.
from yfinance import Search
search = Search('Apple') 
# search = Search('삼성전자') # 한글 회사명은 검색안됨
for q in search.quotes:
    print('ticker:',q['symbol'])
print('-'*10)
# ==============================
# ticker: AAPL
# ticker: APLE
# ticker: AAPL.SW
# ticker: APC.F
# ticker: D90.F
# ----------


search = Search('Samsung') 
for q in search.quotes:
    print('ticker:',q['symbol'])
print('-'*10)
# ----------
# ticker: 005930.KS
# ticker: 7347.HK
# ticker: 001360.KS
# ticker: 489250.KS
# ticker: 439860.KS
# ----------


#과거 주가 데이터 조회 가능 ( 결과를 표형태인 판다스의 DataFrameFrame으로 반환)
# history = stock.history(period='1d',interval='1h') # 1d : 1 day , 1h : 1 hour
#                                Open      High       Low     Close   Volume  Dividends  Stock Splits
# Datetime                                                                                           
# 2026-07-20 09:00:00+09:00  241000.0  257500.0  240000.0  250500.0  6954762        0.0           0.0
# 2026-07-20 10:00:00+09:00  250500.0  252500.0  243500.0  245500.0  3476124        0.0           0.0
# 2026-07-20 11:00:00+09:00  245000.0  249000.0  242500.0  245500.0  2522181        0.0           0.0
# 2026-07-20 12:00:00+09:00  245750.0  246500.0  243000.0  243750.0   490869        0.0           0.0



history = stock.history(period='5d',interval='1d') # 5d : 5 day , 1d : 1 day
print(history)



#                                Open      High       Low     Close    Volume  Dividends  Stock Splits
# Date                                                                                                
# 2026-07-13 00:00:00+09:00  285000.0  292500.0  253000.0  254500.0  31882652        0.0           0.0
# 2026-07-14 00:00:00+09:00  255000.0  270000.0  247000.0  263000.0  40086496        0.0           0.0
# 2026-07-15 00:00:00+09:00  283500.0  284500.0  273000.0  279500.0  24873414        0.0           0.0
# 2026-07-16 00:00:00+09:00  264500.0  265500.0  252500.0  255000.0  27001478        0.0           0.0
# 2026-07-20 00:00:00+09:00  241000.0  257500.0  240000.0  243500.0  14932972        0.0           0.0

#이제 04-open-api-tools-function-call-stock.py 로 가자.
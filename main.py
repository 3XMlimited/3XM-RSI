from __future__ import (absolute_import, division, print_function, unicode_literals)
import backtrader

from datetime import datetime



# step1: 選擇交易所使用的技術指標-RSI
class RSI(backtrader.Strategy):  # 可自行調整參數/判斷買賣時機

   params = (('short', 30),  # 買入點
             ('long', 70),)  # 賣出點

   def __init__(self):
      self.rsi = backtrader.indicators.RSI_SMA(self.data.close, period=14)

   def next(self):
      if not self.position:
         if self.rsi < self.params.short:
            self.buy()
      else:
         if self.rsi > self.params.long:
            self.sell()

            
            
# step2: 實際模擬測試
def main():
   startcash = 10000 # 設定你的初始資金

   data = backtrader.feeds.YahooFinanceCSVData(dataname = './ETH-USD.csv') #從Yahoo財經網站或交易平台下載想了解的股票/虛擬貨幣

   cerebro = backtrader.Cerebro()    # 初始化系統設置

   cerebro.adddata(data)             # 加入數據

   cerebro.addstrategy(RSI)          # 加入一開始寫好的策略/以後有新的策略時也可直接套入

   cerebro.broker.setcash(startcash) # 加入你設定好的初始資金做交易
  
   cerebro.addsizer(backtrader.sizers.FixedSize, stake =100) # 選擇你要買賣的個股數量
    
   cerebro.broker.setcommission(commission = 0.007) # 加入交易手續費，貼近真實



   cerebro.run()                     # 準備好讓電腦幫你交易了嗎




  # step3: 結果呈現（圖片）
   portvalue = cerebro.broker.getvalue()
   print('Final Portfolio Value: ${}'.format(portvalue))
   cerebro.plot(style = "candlestick")


if __name__ == '__main__':
   main()



# News RSS Crawler

本程式將透過多個 RSS Feed 來源自動擷取最新的新聞內容，包括 BBC、Bloomberg、Nasdaq 等多個來源，並將抓取到的新聞內容輸出至 `allnews.txt`。

## 功能特色

- 支援多個新聞來源的 RSS 爬取（BBC、Bloomberg、Nasdaq 等）。
- 可透過修改變數 (scrape_xxx) 來決定是否要啟用或停用特定新聞來源的爬取行為。
- 將所有結果以追加 (append) 方式寫入 `allnews.txt`，方便後續分析或匯入。
- 具備簡單的日誌紀錄功能 (scraper.log)，幫助追蹤程式運行狀況及錯誤資訊。

## 使用方法

1. **下載程式碼**  
   將本程式碼下載或 clone 到本地環境：
   ```bash
   git clone https://github.com/tbdavid2019/crawler-news.git

2.	安裝依賴套件
確保您已安裝 Python 3 和 pip。在專案目錄下執行：

pip install -r requirements.txt

若您環境中未有該檔案，可自行透過以下指令安裝本程式所需套件：

pip install requests beautifulsoup4 lxml


3.	設定爬取來源
在程式碼開頭的參數區域中，可透過改變 1 或 0 來控制爬取特定來源：

1 表示爬取，0 表示略過

```
scrape_bbc_business = 1
scrape_bbc_technology = 1
scrape_bloomberg_markets = 1
scrape_bloomberg_tech = 1
scrape_nasdaq_stocks = 1
scrape_nasdaq_etfs = 1
scrape_nasdaq_technology = 1
scrape_nasdaq_insight = 1
scrape_nasdaq_innovation = 1
scrape_nasdaq_financial_advisors = 1
```

4.	執行程式
在專案目錄下執行：

python news_crawler.py

程式會開始爬取指定的 RSS 新聞來源並將結果輸出到 allnews.txt。

5.	查看結果
爬取結束後，可查看 allnews.txt 檔案，其中包含各篇新聞的 URL 及內容。亦可查看 scraper.log 檔案取得爬取過程中的詳細日誌紀錄與錯誤資訊。

常見問題
•	為什麼有些新聞內容很短或沒有內容？
有些新聞頁面可能結構特殊或無法正常解析出文章內容。程式中設有簡單判斷機制，若內容太短 (例如少於 50 字) 將自動跳過，避免紀錄垃圾內容。
•	可以新增更多 RSS 來源嗎？
可以，您只需在程式中新增對應的 RSS Feed URL 及控制變數，即可輕鬆擴充。


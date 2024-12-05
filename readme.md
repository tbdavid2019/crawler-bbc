
# Web Scraper

This Python script is a versatile and customizable web scraper designed for extracting articles or specific content from websites. It includes robust logging and handles potential issues such as rate-limiting and incomplete data gracefully.

## Features

- **Custom Logging**: Logs scraping progress and issues to both the console and a log file (`scraper.log`).
- **HTML Parsing**: Utilizes `BeautifulSoup` for efficient HTML parsing and content extraction.
- **Throttling**: Implements random delays between requests to reduce the risk of getting blocked.
- **Error Handling**: Handles common issues such as HTTP errors, timeouts, and short/incomplete content gracefully.
- **Configurable Selectors**: Easily customize the link and content selectors for different websites.

## Requirements

To run the script, ensure you have the following Python packages installed:

- `requests`
- `beautifulsoup4`

Install them using pip:

```bash
pip install requests beautifulsoup4
```

How to Use

1.	Modify Scraping Configuration
Update the following parameters in the script based on your target website:
	•	base_url: The root URL of the website to scrape.
	•	link_selector: CSS selector for identifying links to the articles.
	•	content_selector: CSS selector for extracting the desired content.

2.	Run the Script
Execute the script in your Python environment:
```
python scraper.py
```

3.	View Results
	•	The scraped data will be saved in a text file (e.g., BBC_file.txt).
	•	Logs of the scraping process will be stored in scraper.log.


---
Example Configuration

The script includes a pre-configured example for scraping articles from BBC News:
	•	Base URL: https://www.bbc.com
	•	Link Selector: a[href^='/news/articles/']
	•	Content Selector: p
	•	Output File: BBC_file.txt

Logging

The script outputs logs to both the console and a file (scraper.log):
	•	Console: Ensures logs are visible in interactive environments like Google Colab.
	•	Log File: Contains detailed information for debugging and reference.

Notes

•	Ensure you comply with the terms of service of the websites you scrape.
•	Use this script responsibly and avoid overloading servers.


License

This project is licensed under the MIT License. Feel free to modify and use it as needed.

---
網頁爬蟲工具

此 Python 腳本是一個多功能且可自定義的網頁爬蟲，專為從網站中提取文章或特定內容而設計。它包括穩健的日誌記錄功能，並能有效處理速率限制和資料不完整等潛在問題。

功能特點

•	自定義日誌：將爬取進度和問題記錄到控制台與日誌文件（scraper.log）。
•	HTML 解析：使用 BeautifulSoup 進行高效的 HTML 解析和內容提取。
•	請求節流：在請求間隨機延遲，降低被封鎖的風險。
•	錯誤處理：妥善處理 HTTP 錯誤、超時及過短/不完整的內容。
•	可配置選擇器：輕鬆自定義不同網站的連結與內容選擇器。



環境需求

執行此腳本需要安裝以下 Python 套件：
	•	requests
	•	beautifulsoup4

使用 pip 安裝：

pip install requests beautifulsoup4

使用方法

1.	修改爬取配置
根據目標網站更新腳本中的以下參數：
	•	base_url：要爬取的網站根網址。
	•	link_selector：用於識別文章連結的 CSS 選擇器。
	•	content_selector：用於提取內容的 CSS 選擇器。

2.	執行腳本
在 Python 環境中執行腳本：
```
python scraper.py
```

3.	查看結果
	•	爬取的資料將儲存在文本文件中（例如：BBC_file.txt）。
	•	爬取過程的日誌記錄在 scraper.log 文件中。


示例配置

腳本中包含預設配置，用於從 BBC News 爬取文章：
	•	根網址：https://www.bbc.com
	•	連結選擇器：a[href^='/news/articles/']
	•	內容選擇器：p
	•	輸出文件：BBC_file.txt

日誌記錄

腳本將日誌輸出至控制台與文件（scraper.log）：
	•	控制台：確保在互動環境（如 Google Colab）中可見日誌。
	•	日誌文件：詳細記錄調試與參考資訊。

注意事項
•	請確保遵守目標網站的服務條款。
•	負責任地使用此腳本，避免過度請求伺服器。


授權

此項目基於 MIT 授權。您可自由修改並使用此腳本。

Happy scraping! 🕸️ 爬取愉快！


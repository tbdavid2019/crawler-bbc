import os
import logging
import requests
from bs4 import BeautifulSoup
import time
import random
from datetime import datetime
import sys

# ============ 參數開關 (1: 爬取, 0: 不爬取) ============
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

# 自定义处理器，确保日志显示在 Console
class ColabStreamHandler(logging.StreamHandler):
    def emit(self, record):
        msg = self.format(record)
        print(msg, file=sys.stdout)
        sys.stdout.flush()

# 日志配置
logger = logging.getLogger("WebScraper")
logger.setLevel(logging.INFO)
logger.handlers.clear()

# Console 处理器
colab_handler = ColabStreamHandler()
colab_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(colab_handler)

# 文件处理器
file_handler = logging.FileHandler("scraper.log", encoding="utf-8")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(file_handler)

# 浏览器 User-Agent
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# 清空指定文件内容
def clear_file(file_name):
    try:
        if os.path.exists(file_name):
            with open(file_name, 'w', encoding='utf-8') as file:
                file.truncate(0)
            logger.info(f"File '{file_name}' cleared.")
        else:
            logger.info(f"File '{file_name}' does not exist. No need to clear.")
    except Exception as e:
        logger.error(f"Error clearing file '{file_name}': {e}")

def scrape_articles(article_urls, content_selector, file_name):
    articles = []
    for index, full_url in enumerate(article_urls, 1):
        logger.info(f"Processing article {index}/{len(article_urls)}: {full_url}")
        try:
            article_response = requests.get(full_url, headers=HEADERS, timeout=30)
            if article_response.status_code != 200:
                logger.warning(f"Failed to fetch {full_url}. HTTP Status Code: {article_response.status_code}")
                continue

            article_soup = BeautifulSoup(article_response.text, "html.parser")
            paragraphs = article_soup.select(content_selector)
            content = "\n".join([p.get_text(strip=True) for p in paragraphs])
            if len(content.strip()) < 50:
                logger.warning(f"Content too short for article: {full_url}")
                continue

            articles.append({"URL": full_url, "Content": content})
            logger.info(f"Successfully scraped article: {full_url}")

            delay = random.uniform(1, 3)
            logger.info(f"Waiting {delay:.2f} seconds before next request...")
            time.sleep(delay)
        except Exception as e:
            logger.error(f"Error processing {full_url}: {e}")

    # 寫入 allnews.txt (使用 append 模式)
    if articles:
        logger.info(f"Appending {len(articles)} articles to {file_name}")
        with open(file_name, "a", encoding="utf-8") as fin:
            for article in articles:
                fin.write(f"URL: {article['URL']}\n")
                fin.write(f"Content: {article['Content']}\n\n")

# 爬取 RSS 的方法
def scrape_rss_feed(rss_url, content_selector, file_name):
    logger.info(f"Starting to scrape RSS feed: {rss_url}")
    start_time = datetime.now()
    try:
        response = requests.get(rss_url, headers=HEADERS, timeout=30)
        if response.status_code != 200:
            logger.error(f"Failed to fetch RSS {rss_url}. HTTP Status Code: {response.status_code}")
            return
        
        soup = BeautifulSoup(response.text, "xml")
        items = soup.find_all("item")
        article_urls = [item.link.get_text(strip=True) for item in items if item.link]

        logger.info(f"Found {len(article_urls)} articles from RSS: {rss_url}")
        scrape_articles(article_urls, content_selector, file_name)

        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        logger.info(f"RSS scraping completed. Total time: {duration:.2f} seconds for {rss_url}")
    except Exception as e:
        logger.error(f"Error during RSS scraping: {e}")

try:
    # 清空檔案內容
    clear_file("scraper.log")
    clear_file("allnews.txt")

    # BBC Feeds
    if scrape_bbc_business == 1:
        logger.info("Scraping BBC Business RSS...")
        scrape_rss_feed(
            rss_url="https://feeds.bbci.co.uk/news/business/rss.xml",
            content_selector="p",
            file_name="allnews.txt"
        )

    if scrape_bbc_technology == 1:
        logger.info("Scraping BBC Technology RSS...")
        scrape_rss_feed(
            rss_url="https://feeds.bbci.co.uk/news/technology/rss.xml",
            content_selector="p",
            file_name="allnews.txt"
        )

    # Bloomberg Feeds
    if scrape_bloomberg_markets == 1:
        logger.info("Scraping Bloomberg Markets RSS...")
        scrape_rss_feed(
            rss_url="https://feeds.bloomberg.com/markets/news.rss",
            content_selector="p",
            file_name="allnews.txt"
        )

    if scrape_bloomberg_tech == 1:
        logger.info("Scraping Bloomberg Technology RSS...")
        scrape_rss_feed(
            rss_url="https://feeds.bloomberg.com/technology/news.rss",
            content_selector="p",
            file_name="allnews.txt"
        )

    # Nasdaq Feeds
    if scrape_nasdaq_stocks == 1:
        logger.info("Scraping Nasdaq Stocks RSS...")
        scrape_rss_feed(
            rss_url="https://www.nasdaq.com/feed/rssoutbound?category=Stocks",
            content_selector="p",
            file_name="allnews.txt"
        )

    if scrape_nasdaq_etfs == 1:
        logger.info("Scraping Nasdaq ETFs RSS...")
        scrape_rss_feed(
            rss_url="https://www.nasdaq.com/feed/rssoutbound?category=ETFs",
            content_selector="p",
            file_name="allnews.txt"
        )

    if scrape_nasdaq_technology == 1:
        logger.info("Scraping Nasdaq Technology RSS...")
        scrape_rss_feed(
            rss_url="https://www.nasdaq.com/feed/rssoutbound?category=Technology",
            content_selector="p",
            file_name="allnews.txt"
        )

    if scrape_nasdaq_insight == 1:
        logger.info("Scraping Nasdaq Insight RSS...")
        scrape_rss_feed(
            rss_url="https://www.nasdaq.com/feed/rssoutbound?category=Nasdaq",
            content_selector="p",
            file_name="allnews.txt"
        )

    if scrape_nasdaq_innovation == 1:
        logger.info("Scraping Nasdaq Innovation RSS...")
        scrape_rss_feed(
            rss_url="https://www.nasdaq.com/feed/rssoutbound?category=Innovation",
            content_selector="p",
            file_name="allnews.txt"
        )

    if scrape_nasdaq_financial_advisors == 1:
        logger.info("Scraping Nasdaq Financial Advisors RSS...")
        scrape_rss_feed(
            rss_url="https://www.nasdaq.com/feed/rssoutbound?category=Financial+Advisors",
            content_selector="p",
            file_name="allnews.txt"
        )

except Exception as e:
    logger.error(f"Error in main scraping process: {e}")

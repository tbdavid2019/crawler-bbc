import logging
import requests
from bs4 import BeautifulSoup
import time
import random
from datetime import datetime
import sys

# 自定义处理器，确保日志显示在 Colab Console
class ColabStreamHandler(logging.StreamHandler):
    def emit(self, record):
        msg = self.format(record)
        print(msg, file=sys.stdout)
        sys.stdout.flush()

# 日志配置
logger = logging.getLogger("WebScraper")
logger.setLevel(logging.INFO)
logger.handlers.clear()

# Colab Console 处理器
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

# 通用爬取函数
def scrape_articles(base_url, link_selector, content_selector, file_name):
    logger.info(f"Starting scraping for {base_url}")
    start_time = datetime.now()
    try:
        response = requests.get(base_url, headers=HEADERS)
        if response.status_code != 200:
            logger.error(f"Failed to fetch {base_url}. HTTP Status Code: {response.status_code}")
            return

        soup = BeautifulSoup(response.text, "html.parser")
        logger.info("Extracting article links...")
        links = soup.select(link_selector)
        results = [link['href'] for link in links if link.has_attr('href')]
        logger.info(f"Found {len(results)} articles")

        articles = []
        for index, result in enumerate(results, 1):
            full_url = f"{base_url.rstrip('/')}{result}" if result.startswith("/") else result
            logger.info(f"Processing article {index}/{len(results)}: {full_url}")
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

        logger.info(f"Writing {len(articles)} articles to {file_name}")
        with open(file_name, "w", encoding="utf-8") as fin:
            for article in articles:
                fin.write(f"URL: {article['URL']}\n")
                fin.write(f"Content: {article['Content']}\n\n")

        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        logger.info(f"Scraping completed. Total time: {duration:.2f} seconds")
    except Exception as e:
        logger.error(f"Error during scraping: {e}")

try:
    logger.info("Scraping BBC...")
    scrape_articles(
        base_url="https://www.bbc.com",
        link_selector="a[href^='/news/articles/']",
        content_selector="p",
        file_name="BBC_file.txt"
    )
except Exception as e:
    logger.error(f"Error scraping BBC: {e}")


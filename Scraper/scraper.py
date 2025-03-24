from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from tqdm import tqdm
import concurrent.futures

class News_Scraper: 
    def __init__(self, urls):
        self.urls = urls
        self.length = {}
        self.texts = {}

    def scrape_news(self, url):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
            }

            req = Request(url, headers=headers)
            html_page = urlopen(req, timeout=5).read()

            soup = BeautifulSoup(html_page, 'html.parser')

            paragraphs = [paragraph.get_text() for paragraph in soup.findAll('p') if paragraph.get_text()]
            combined_text = ' '.join(paragraphs)

            return combined_text, paragraphs

        except Exception as e:
            print(f"Failed to scrape {url} due to error: {e}")
            return "", []
        
    def parallel_news_scraping(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(tqdm(executor.map(self.scrape_news, self.urls), total=len(self.urls), desc="Scraping News URLs"))

            for url, (combined_text, paragraphs) in zip(self.urls, results):
                self.texts[url] = combined_text
                self.length[url] = len(paragraphs)
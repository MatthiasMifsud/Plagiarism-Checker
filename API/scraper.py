from tqdm import tqdm
from newsapi import NewsApiClient
import concurrent.futures

class News_API: 
    def __init__(self, api_key, source_list):
        self.api_key = api_key
        self.source_list = source_list
        self.articles = []
        self.newsapi = NewsApiClient(api_key=self.api_key)

    def fetch_articles(self, source):
        try:
            response = self.newsapi.get_everything(
                q=source,
                language='en',
                sort_by='relevancy'
            )

            articles = response.get('articles', [])
            self.articles.extend(articles)
        
        except Exception as e:
            print(f"Failed to scrape {source} due to error: {e}")
             
    def parallel_news_fetching(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            list(tqdm(executor.map(self.fetch_articles, self.source_list), total=len(self.source_list), desc="Comparing News Articles"))

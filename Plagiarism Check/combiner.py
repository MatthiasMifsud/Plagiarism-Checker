from scraper import News_Scraper
from processing import Text_Processor
from tfidsimilarity import Text_Similarity

class Combiner:
    def __init__(self, urls, user_file_name):
        self.scraper = News_Scraper(urls)
        self.processor = Text_Processor()
        self.similarity = Text_Similarity()

        with open(user_file_name, 'r', encoding='utf-8') as file:
            self.user_text = file.read()
    
    def runner(self):
        self.scraper.parallel_news_scraping()
        user_text_processed = self.processor.preprocessing(self.user_text)
        url_processed = {url: self.processor.preprocessing(text) for url, text in self.scraper.texts.items()}

        print(f"Extracted {sum(self.scraper.length.values())} paragraphs. {self.scraper.length}")

        self.similarity.tfid_calc(url_processed, user_text_processed)

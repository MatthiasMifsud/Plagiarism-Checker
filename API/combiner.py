from fetcher import News_API
from processing import Text_Processor
from tfidsimilarity import Text_Similarity

class Combiner:
    def __init__(self, api_key, source_list, user_file_name):
        self.api_key = api_key
        self.source_list = source_list
        self.user_file_name = user_file_name
        self.news_api = News_API(api_key, source_list)
        self.text_processor = Text_Processor()
        self.text_similarity = Text_Similarity()
    
    def runner(self):
        self.news_api.parallel_news_fetching()

        try: 
            with open(self.user_file_name, 'r') as file:
                user_text = file.read()
            processed_user_text = self.text_processor.preprocessing(user_text)

        except Exception as e:
            print(f"Failed to load/process the file {self.user_file_name}.")
            return
        
        processed_texts = {}

        for article in self.news_api.articles:
            title = article.get('title', '')
            description = article.get('description', '')
            combined_text = f"{title} {description}"

            processed_texts[article['url']] = self.text_processor.preprocessing(combined_text)

        if not processed_texts:
            print("No articles were fetched to compare with user text.")
            return
        
        print(f"Extracted {len(processed_texts)} articles.")
        
        self.text_similarity.tfid_calc(processed_texts, processed_user_text)

from combiner import Combiner

if __name__ == "__main__":

    english_news_links = [
        "https://bbc.com","https://nytimes.com","https://msn.com",
        "https://cnn.com","https://news.google.com","https://theguardian.com",
        "https://foxnews.com","https://dailymail.co.uk","https://finance.yahoo.com",
        "https://people.com","https://usatoday.com","https://apnews.com",
        "https://forbes.com","https://nypost.com","https://hindustantimes.com",
        "https://substack.com","https://reuters.com","https://cnbc.com",
        "https://washingtonpost.com","https://nbcnews.com","https://newsweek.com",
        "https://independent.co.uk","https://cbsnews.com","https://wsj.com",
        "https://buzzfeed.com","https://cbc.ca","https://telegraph.co.uk",
        "https://businessinsider.com","https://news.com.au","https://abcnews.go.com",
        "https://abc.net.au","https://thehindu.com","https://express.co.uk",
        "https://thesun.co.uk","https://news.sky.com","https://huffpost.com",
        "https://mirror.co.uk","https://drudgereport.com","https://thehill.com"
        ]
    
    user_file_name = 'Plagiarism Check/text.txt'

    combiner = Combiner(english_news_links, user_file_name)
    combiner.runner()
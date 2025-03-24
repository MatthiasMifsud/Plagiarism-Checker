from combiner import Combiner

if __name__ == "__main__":
    api_key = 'YOUR_API_KEY'
    source_list = [
        "bbc", "cnn", "nytimes", "theguardian", "reuters", "foxnews",
        "bbc-news", "cbs-news", "abc-news", "huffpost"
        ]
    user_file_name = 'API/text.txt'

    combiner = Combiner(api_key, source_list, user_file_name)
    combiner.runner()
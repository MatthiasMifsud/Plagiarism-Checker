# News Plagiarism Checker API Edition

This enhanced version integrates with NewsAPI to detect similarities between user-provided text and current news articles using TF-IDF and cosine similarity analysis.

## Enhanced Features

- **API Integration**: Fetches real-time news articles from 10+ major publishers via NewsAPI
- **Parallel Processing**: Uses multithreaded requests for efficient article collection
- **Dynamic Thresholding**: Automatically calculates similarity thresholds using 90th percentile analysis
- **Source Flexibility**: Easily configurable list of news sources (BBC, CNN, NYTimes, etc.)
- **Content Enrichment**: Combines article titles and descriptions for comprehensive analysis

---

## Updated File Structure

### 1. `fetcher.py`
- Contains `News_API` class handling NewsAPI integration
- Implements parallel API requests with progress tracking
- Error handling for API response validation

### 2. `processing.py`
- Enhanced text preprocessing with:
  - Advanced special character removal
  - Lemmmatization with WordNet
  - Custom stopword filtering

### 3. `tfidsimilarity.py`
- Implements dynamic threshold calculation (90th percentile + 0.15 fallback)
- Generates similarity reports with source URLs

### 4. `combiner.py`
- Orchestrates API fetching, text processing, and similarity analysis
- Handles file I/O for user text input

### 5. `main.py`
- Configuration hub for API keys and news sources
- Example implementation with 10 major news outlets

---

## API Configuration

1. Get free API key from [NewsAPI](https://newsapi.org/)
2. Replace placeholder in `main.py`:

```
api_key = 'your_actual_api_key_here' # Replace with your NewsAPI key
```

3. Customize news sources in `source_list`:

```
source_list = ["bbc", "cnn", "nytimes", "reuters", "foxnews", ...]
```


---

## Usage Instructions

1. Prepare your text in `API/text.txt`
2. Run with enhanced progress tracking:

```
python main.py
```

3. Interpret output:

```
Comparing News Articles: 100%|████| 10/10 [00:02<00:00, 4.97it/s]
Extracted 850 articles
Threshold: 0.2750
Similarity detected with https://bbc.com/news/uk-12345: 0.3245
```

# Plagiarism Checker

This repository contains Python scripts designed to scrape news articles, preprocess text, and calculate text similarity using TF-IDF and cosine similarity. The primary goal is to identify significant similarities between a user-provided text and content from various news sources. (Note: can be altered to work for things other than news sources e.g: journals)

---

## Features

- **Scraping**: Extracts textual content from multiple news websites using web scraping.
- **Text Preprocessing**: Cleans and processes text by removing stopwords, lemmatizing words, and tokenizing sentences.
- **Similarity Calculation**: Computes TF-IDF vectors and evaluates cosine similarity between the user-provided text and scraped news articles.
- **Threshold-Based Analysis**: Identifies significant similarities based on a calculated threshold.

---

## File Structure

### 1. `main.py`
- Entry point of the application.
- Initializes the `Combiner` class with a list of news URLs and the path to a user-provided text file.
- Executes the scraping, preprocessing, and similarity checking workflow.

### 2. `combiner.py`
- Coordinates the workflow by integrating scraping, preprocessing, and similarity calculation modules.
- Reads user-provided text and processes it for comparison.

### 3. `scraper.py`
- Implements the `News_Scraper` class for extracting textual data from news websites.
- Utilizes multithreading for efficient parallel scraping.
- Handles errors gracefully during scraping.

### 4. `processing.py`
- Contains the `Text_Processor` class for cleaning and preprocessing text data.
- Removes special characters, stopwords, and performs lemmatization.

### 5. `tfidsimilarity.py`
- Defines the `Text_Similarity` class for calculating TF-IDF vectors and cosine similarity.
- Compares user-provided text with scraped articles to detect significant matches.

### 6. `text.txt`
- Example file containing user-provided text for plagiarism or similarity checking.

---

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/news-similarity-checker.git
cd news-similarity-checker
```

2. Install required dependencies:

```
pip install -r requirements.txt
```

3. Ensure NLTK resources are downloaded:

```
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
```

---

## Usage

1. Prepare your input file (`text.txt`) containing the text you want to check for similarity.
2. Run the application:
   ```
   python main.py
   ```
3. Review the output in the console for similarity results.

---

## Example Output

```
Scraping News URLs: 100%|███████████████████████████████████| 40/40 [00:30<00:00, 1.32it/s]
Extracted 500 paragraphs from news articles.
Threshold: 0.2500
Similarity with https://bbc.com: 0.3200
Similarity detected between provided text and https://bbc.com with similarity of 0.3200
Similarity with https://cnn.com: 0.1500
No significant similarity found between provided text and https://cnn.com with similarity of 0.1500
```

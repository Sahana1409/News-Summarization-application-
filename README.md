# Documentation for News Summarization and Text-to-Speech Application

## Project Setup
### Prerequisites
Ensure you have Python installed (preferably Python 3.8 or above). Install the required dependencies using the following command:
```bash
pip install -r requirements.txt
```

### Running the Application
1. Start the API server:
   ```bash
   python api.py
   ```
2. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
3. Open the browser and navigate to the provided Streamlit app URL to input a company name and analyze news sentiment.

---

## Model Details
### Sentiment Analysis Model
- **Algorithm**: Naïve Bayes (MultinomialNB)
- **Feature Extraction**: TF-IDF vectorizer
- **Training Data**: Sample dataset with stock-related sentiment labels
- **Implementation**: Trained in `train_model.py` and stored as `sentiment_model.pkl` and `vectorizer.pkl`

### Summarization
- **Method**: Extracts summaries directly from stored news articles (CSV dataset)

### Text-to-Speech (TTS)
- **Library Used**: gTTS (Google Text-to-Speech)
- **Language**: Hindi
- **Functionality**: Converts summarized text and sentiment analysis into spoken Hindi output

---

## API Development
### Endpoints
#### `/analyze` (POST)
- **Description**: Fetches company news, analyzes sentiment, translates results to Hindi, and generates TTS output.
- **Request Format**:
  ```json
  {
    "company": "Tesla, Rivian, BMW, Ford, Toyota, GM"
  }
  ```
- **Response Format**:
  ```json
  {
    "Company": "Company Name",
    "Articles": [
      {
        "Title": "News Title Here",
        "Summary": "Brief news summary...",
        "Sentiment": "Positive",
        "Topics": ["Topic1", "Topic2"],
        "URL": "https://example.com",
        "TTS_File": "output/CompanyName_article1.mp3"
      }
    ],
    "Sentiment Distribution": {
      "Positive": 1,
      "Negative": 1,
      "Neutral": 0
    },
    "Final Sentiment Analysis": "Company Name की नवीनतम समाचार कवरेज मुख्य रूप से Positive है।",
    "Audio": "output/CompanyName_final_summary.mp3"
  }
  ```

### Accessing the API via Postman
1. Open Postman.
2. Create a new `POST` request to `http://127.0.0.1:5000/analyze`.
3. Add JSON body: `{ "company": "Tesla" }` (or any company from the list).
4. Click "Send" to receive analysis results.

---

## API Usage
### Third-Party APIs
- **Google Translate API (googletrans)**: Used for translating text into Hindi.
- **gTTS**: Used for generating Hindi speech from text.
- **BeautifulSoup (bs4)**: Used for web scraping to extract news articles.
- **TextBlob**: Used for additional sentiment analysis.

---

## Assumptions & Limitations
### Assumptions
- News articles are pre-stored in a CSV file (`company_articles_final.csv`).
- Sentiment analysis model is trained on a limited dataset.
- Hindi translations are automated using Google Translate and may not be fully accurate.

### Limitations
- Application does not scrape live news; it relies on stored articles.
- Sentiment classification is based on limited training data and may not generalize well.
- gTTS relies on an internet connection to generate speech output.

---

## Conclusion
This application provides a structured news summarization and sentiment analysis tool with Hindi text-to-speech support. It efficiently processes company-related news, analyzes sentiment trends, and presents results in an easy-to-use interface.


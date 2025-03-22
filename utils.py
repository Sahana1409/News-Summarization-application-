import os
import pandas as pd
import joblib
from gtts import gTTS
from googletrans import Translator

translator = Translator()

# Load trained sentiment model
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Function to load articles for a specific company from CSV
def load_company_articles(company):
    df = pd.read_csv("company_articles_final.csv")
    df_filtered = df[df["title"].str.contains(company, case=False, na=False)]
    
    articles = []
    for _, row in df_filtered.iterrows():
        articles.append({
            "title": row["title"],
            "summary": row["summary"],
            "topics": row["topics"].split(", "),
            "url": row["url"]
        })
    
    return articles if articles else None

# Function to analyze sentiment using a trained model
def analyze_sentiment(text):
    text_vec = vectorizer.transform([text])
    sentiment = model.predict(text_vec)[0]
    return sentiment

# Function to translate text into Hindi
def translate_to_hindi(text):
    translation = translator.translate(text, dest="hi")
    return translation.text

# Function to generate Hindi TTS
def generate_hindi_tts(text, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    tts = gTTS(text, lang="hi")
    tts.save(filename)
    return filename
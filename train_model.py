import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Sample dataset for training
data = {
    "text": [
        "Stock prices are rising rapidly.",
        "The company is facing legal issues.",
        "New product launch boosts investor confidence.",
        "Market uncertainty leads to stock drop."
    ],
    "sentiment": ["Positive", "Negative", "Positive", "Negative"]
}

df = pd.DataFrame(data)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df["text"], df["sentiment"], test_size=0.2, random_state=42)

# Train model
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Save model and vectorizer
joblib.dump(model, "sentiment_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained and saved successfully!")
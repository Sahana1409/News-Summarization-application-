from flask import Flask, request, jsonify
from utils import load_company_articles, analyze_sentiment, generate_hindi_tts, translate_to_hindi

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    company = data.get('company', '')

    if not company:
        return jsonify({"error": "Please enter a company name"}), 400

    articles = load_company_articles(company)
    if not articles:
        return jsonify({"error": f"No articles found for {company}"}), 404

    sentiment_results = []
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    topic_sentiment = {}

    for idx, article in enumerate(articles):
        sentiment = analyze_sentiment(article["summary"])
        sentiment_counts[sentiment] += 1

        # Categorize sentiment by topic
        for topic in article["topics"]:
            if topic not in topic_sentiment:
                topic_sentiment[topic] = {"Positive": 0, "Negative": 0, "Neutral": 0}
            topic_sentiment[topic][sentiment] += 1

        # Translate summary into Hindi
        summary_hindi = translate_to_hindi(article["summary"])
        sentiment_hindi = translate_to_hindi(sentiment)

        # Generate Hindi TTS for each article
        tts_filename = f"output/{company}article{idx + 1}.mp3"
        generate_hindi_tts(summary_hindi, tts_filename)

        sentiment_results.append({
            "Title": article["title"],
            "Summary": article["summary"],
            "Sentiment": sentiment,
            "Topics": article["topics"],
            "URL": article["url"],
            "TTS_File": tts_filename
        })

    # Generate overall Hindi sentiment summary
    dominant_sentiment = max(sentiment_counts, key=sentiment_counts.get)
    final_summary = f"{company} की नवीनतम समाचार कवरेज मुख्य रूप से {dominant_sentiment} है।"

    # Generate Hindi TTS for final summary
    final_tts_file = f"output/{company}_final_summary.mp3"
    generate_hindi_tts(final_summary, final_tts_file)

    response_data = {
        "Company": company,
        "Articles": sentiment_results,
        "Sentiment Distribution": sentiment_counts,
        "Final Sentiment Analysis": final_summary,
        "Audio": final_tts_file
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
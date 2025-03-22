import streamlit as st
import requests

st.title("📢 Company News Summarization & Sentiment Analysis in Hindi")

company_input = st.text_input("🔎 Enter a Company Name (Tesla,Rivian,BMW,Ford,Toyota,GM):")

if st.button("Analyze News"):
    st.info(f"Fetching {company_input} news and analyzing sentiment... ⏳")

    response = requests.post("http://127.0.0.1:5000/analyze", json={"company": company_input})

    if response.status_code != 200:
        st.error(f"⚠ Error: {response.status_code} - {response.text}")
    else:
        result = response.json()
        st.success(f"✅ Sentiment Analysis for {result['Company']}")

        for article in result.get('Articles', []):
            st.write(f"*📰 Title:* [{article['Title']}]({article['URL']})")
            st.write(f"*📃 Summary:* {article['Summary']}")
            st.write(f"*📈 Sentiment:* {article['Sentiment']}")
            st.write(f"*🏷 Topics:* {', '.join(article['Topics'])}")

            # Play Hindi TTS for each article
            st.subheader("🎙 Hindi Speech Summary")
            st.audio(article["TTS_File"])

            st.write("---")

        # Play the Final Sentiment Hindi TTS
        st.subheader("🎙 Overall Hindi Sentiment Summary")
        st.audio(result["Audio"])
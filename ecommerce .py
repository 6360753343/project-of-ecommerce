import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt


data = pd.read_csv("Flipkart_Reviews - Electronics.csv")

def get_sentiment(text):
    try:
        analysis = TextBlob(str(text))
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            return 'Positive'
        elif polarity < 0:
            return 'Negative'
        else:
            return 'Neutral'
    except:
        return 'Neutral'


data['Sentiment'] = data['review'].apply(get_sentiment)


sentiment_counts = data['Sentiment'].value_counts()

plt.figure(figsize=(6,4))
sentiment_counts.plot(kind='bar', color=['green', 'red', 'blue'])
plt.title('Sentiment Analysis of E-commerce Reviews')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


plt.figure(figsize=(5,5))
sentiment_counts.plot(kind='pie', autopct='%1.1f%%', colors=['green', 'red', 'blue'])
plt.title('Sentiment Distribution')
plt.ylabel('')
plt.tight_layout()
plt.show()


data.to_csv('ecommerce_reviews_with_sentiment.csv', index=False)
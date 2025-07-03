import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
import nltk


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


df = pd.read_csv("Flipkart_Reviews - Electronics.csv")

print("Available columns:", df.columns)


review_col = 'review'


df = df.dropna(subset=[review_col])


def get_sentiment(text):
    return TextBlob(str(text)).sentiment.polarity

df['polarity'] = df[review_col].apply(get_sentiment)


def classify_sentiment(p):
    if p > 0.1:
        return "Positive"
    elif p < -0.1:
        return "Negative"
    else:
        return "Neutral"

df['sentiment'] = df['polarity'].apply(classify_sentiment)


df.to_csv("sentiment_analyzed_reviews.csv", index=False)


print(df[[review_col, 'polarity', 'sentiment']].head())


plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='sentiment', palette='Set2', order=['Positive', 'Neutral', 'Negative'])
plt.title('Sentiment Distribution of Flipkart Electronics Reviews')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.tight_layout()
plt.savefig("sentiment_distribution.png")
plt.show()
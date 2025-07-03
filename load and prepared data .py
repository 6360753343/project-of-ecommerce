import pandas as pd


df = pd.read_csv("Flipkart_Reviews - Electronics.csv")


df['location'] = df['location'].fillna('Unknown')


df['full_review'] = df['summary'].astype(str) + ". " + df['review'].astype(str)


print(df[['summary', 'review', 'full_review']].head())

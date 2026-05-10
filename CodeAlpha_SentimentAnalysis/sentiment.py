# Import libraries
import pandas as pd
from textblob import TextBlob

# Load data
df = pd.read_csv("reviews.csv")

# Empty sentiment list
sentiments = []

# Analyze sentiment
for review in df["Review"]:
    analysis = TextBlob(review)

    # Sentiment polarity
    polarity = analysis.sentiment.polarity

    # Classification
    if polarity > 0:
        sentiments.append("Positive")
    elif polarity < 0:
        sentiments.append("Negative")
    else:
        sentiments.append("Neutral")

# Add new column
df["Sentiment"] = sentiments

# Print results
print(df)

# Save results
df.to_csv("sentiment_results.csv", index=False)

print("Sentiment Analysis Completed!")
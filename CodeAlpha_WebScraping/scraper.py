# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://quotes.toscrape.com/"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all quotes
quotes = soup.find_all("div", class_="quote")

# Empty lists
quote_text = []
authors = []

# Loop through quotes
for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    quote_text.append(text)
    authors.append(author)

# Create DataFrame
df = pd.DataFrame({
    "Quote": quote_text,
    "Author": authors
})

# Save CSV
df.to_csv("quotes.csv", index=False)

print("Data Scraped Successfully!")
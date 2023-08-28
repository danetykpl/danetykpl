import wikipediaapi
import nltk
from nltk.tokenize import word_tokenize
import pandas as pd

# Define a custom user agent as per Wikipedia's guidelines
ua_client= "Mozilla/5.0"
ua_contact = "johnsmith@gmail.com"
ua_library = "wikipedia-api/0.6.0"
user_agent = f"{ua_client} ({ua_contact}) {ua_library}"

# Define the language and user agent
lang = wikipediaapi.Wikipedia(language="en", user_agent=user_agent)

# Define the title of the Wikipedia article
article_title = "Data science"

# Get the Wikipedia page for the specified article
page = lang.page(article_title)

# Get the text content of the article
article_text = page.text

# Tokenize the article text into words
nltk.download("punkt")  # Download NLTK tokenizer data if not already downloaded
words = word_tokenize(article_text)

# Create a DataFrame with a single column "Words"
df = pd.DataFrame({"Words": words})

# Display the DataFrame
print(df.head())  # Display the first few rows of the DataFrame
print(df)

# Filter rows that contain words
filtered_df = df[df['Words'].str.contains(r'\w', na=False)]

# Save filtered DataFrame as CSV file
filtered_df.to_csv("wikipedia_data_science.csv", index=False)

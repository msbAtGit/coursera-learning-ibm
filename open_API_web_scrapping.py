import os
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

# load API key
client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

url = "https://quotes.toscrape.com"
html = requests.get(url).text

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a web scraping assistant."},
        {"role": "user", "content": f"Extract all quotes and authors from this HTML:\n{html}"}
    ]
)

print(response.choices[0].message.content)

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the IMDB Top 250 page
url = "https://www.imdb.com/chart/top/"
headers = {"User-Agent": "Mozilla/5.0"}   # fake a browser
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Extract movie rows
movies = soup.select("li.ipc-metadata-list-summary-item")  # movie items

titles = []
years = []
ratings = []

for movie in movies:
    # Extract title
    title = movie.find("h3").get_text(strip=True)
    
    # Extract year (inside span)
    year_span = movie.select_one("span.sc-b189961a-8")
    year = year_span.get_text(strip=True) if year_span else None
    
    # Extract rating
    rating_span = movie.select_one("span.ipc-rating-star")
    rating = rating_span.get_text(strip=True) if rating_span else None
    
    titles.append(title)
    years.append(year)
    ratings.append(rating)

# Step 3: Create DataFrame
df = pd.DataFrame({
    "Title": titles,
    "Year": years,
    "Rating": ratings
})

# Clean up Rating column
df["Rating"] = df["Rating"].str.extract(r"([\d.]+)").astype(float)

print(df.head(10))   # show first 10 movies

# Step 4: Simple analysis
print("\nAverage rating:", df["Rating"].mean())
print("\nTop 5 movies:")
print(df.nlargest(5, "Rating")[["Title", "Rating"]])



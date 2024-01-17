import requests

API_KEY = "1d91efc79c4d429fa402017e62be6ef0"
URL = ("https://newsapi.org/v2/everything?q=tesla&from="
       "2023-12-17&sortBy=publishedAt&apiKey=1d91efc79c4"
       "d429fa402017e62be6ef0")

# Make request
request = requests.get(URL)

# Get a dict with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
       print(article["title"])
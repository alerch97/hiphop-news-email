import requests
import os
from send_email import send_email

TOPIC = "(hiphop OR rap OR hip hop)"
LANGUAGE = "de"
API_KEY = os.environ.get("NEWS_API")
URL = ("https://newsapi.org/v2/everything?"
       f"q={TOPIC}&"
       "sortBy=publishedAt&"
       f"apiKey={API_KEY}&"
       f"language={LANGUAGE}")

# Make request
request = requests.get(URL)

# Get actual date of request
date = request.headers["Date"]

# Get a dict with data
content = request.json()

# Message header for the email
message = f"""\
Subject: Hip Hop & Rap News Update, {date[0:16]}

Tägliche automatisierte Update-Mail mit News aus der Hip Hop und Rap Welt #808


"""

# Access the article titles and description + add to message
for article in content["articles"]:
    if article["title"] is not None:
        message = (message + f"{article['title']}" + "\n"
                   + f"{article['description']}"
                   + "\n" + f"{article['url']}" + 2*"\n")

message = message.encode("utf-8")
send_email(message)
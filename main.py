import requests
from send_email import send_email

TOPIC = "(hiphop OR rap)"
API_KEY = "1d91efc79c4d429fa402017e62be6ef0"
URL = ("https://newsapi.org/v2/everything?"
       f"q={TOPIC}&"
       "sortBy=publishedAt&"
       f"apiKey={API_KEY}&"
       "language=de")

# Make request
request = requests.get(URL)

# Get actual date of request
date = request.headers["Date"]

# Get a dict with data
content = request.json()

# Message header for the email
message = f"""\
Subject: News Update, {date[0:16]}

"""

# Access the article titles and description + add to message
for article in content["articles"]:
    if article["title"] is not None:
        print(article["title"])
        message = (message + f"{article['title']}" + "\n"
                   + f"{article['description']}"
                   + "\n" + f"{article['url']}" + 2*"\n")

message = message.encode("utf-8")
send_email(message)
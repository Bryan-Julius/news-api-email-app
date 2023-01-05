import requests
from Send_Email import send_email

topic = "tesla"

api_key = "1524468cf3f9418ebe9c31a9b0a4fcc7"
url = "https://newsapi.org/v2/everything?" \
        f"q={topic}&" \
        "sortBy=publishedAt&" \
        "apiKey=1524468cf3f9418ebe9c31a9b0a4fcc7" \
        "language=en"
# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()


# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" \
                + article["description"] \
                + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)

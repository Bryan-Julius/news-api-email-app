import requests
from Send_Email import send_email

api_key = "1524468cf3f9418ebe9c31a9b0a4fcc7"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2022-12-04&sortBy=publishedAt&apiKey=" \
      "1524468cf3f9418ebe9c31a9b0a4fcc7"
# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""

# Access the article titles and description
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)


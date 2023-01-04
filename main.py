import requests

api_key = "1524468cf3f9418ebe9c31a9b0a4fcc7"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2022-12-04&sortBy=publishedAt&apiKey=" \
      "1524468cf3f9418ebe9c31a9b0a4fcc7"
# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
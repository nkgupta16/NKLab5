import requests


def get_headlines_for_city(api_key, city):
    url = 'https://newsapi.org/v2/everything'

    params = {
        'apiKey': api_key,
        'q': city,
        'pageSize': 5  # Set to 5 to get the top 5 articles. You can change accordingly!!
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        articles = response.json().get('articles', [])
        article_count = min(5, len(articles))

        for i in range(article_count):
            article = articles[i]
            title = article.get('title')
            source_name = article.get('source', {}).get('name')
            description = article.get('description')
            url = article.get('url')
            published_at = article.get('publishedAt')

            print(f"Article {i + 1}:")
            print(f"Title: {title}")
            print(f"Source: {source_name}")
            print(f"Description: {description}")
            print(f"URL: {url}")
            print(f"Published At: {published_at}")
            print(f"{'-' * 60}")
    else:
        print(f"Failed to retrieve articles. HTTP Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")


api_key = 'f7e07fcc168c44c9b07dbeaf19cb5cb9'
city = 'Saint Petersburg'
get_headlines_for_city(api_key, city)

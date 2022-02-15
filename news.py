import requests


class NewsFeed:
    """Represents multiple news titles and links as a string"""
    base_url = 'https://newsapi.org/v2/everything'
    api_key = '04d5d3a531ce47faafbc7eb0c07f0927'

    def __init__(self, topic,from_date, to_date,  language):
        self.topic = topic
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        # parameters of url q, searchin, language, to, from, and sortBy
        url = self._build_url()

        articles = self._get_articles(url)

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    # private method to be used inside the class only
    def _build_url(self):
        url = f'{self.base_url}?' \
              f'q={self.topic}&' \
              'searchIn=title,content&' \
              f'language={self.language}&' \
              f'to={self.to_date}&' \
              f'from={self.from_date}' \
              '&sortBy=publishedAt&' \
              f'apiKey={self.api_key}'
        return url


if __name__ == "__main__":
    news_feed = NewsFeed(topic='Astronomy', from_date='2022-02-11', to_date='2022-02-12', language='en')
    print(news_feed.get())
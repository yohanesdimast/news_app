import requests

class NewsAPI:
    def __init__(self) -> None:
        self.API_KEY = "&apiKey=786badd122df4f7682e025cb08d12862"
        self.url = f"https://newsapi.org/"

    def get_news_source(self, category):
        endpoint = f"v2/top-headlines?country=us&category={category}&pageSize=100"
        raw_content = requests.get(self.url + endpoint + self.API_KEY)
        content = raw_content.json()
        source_list = [articles['source']['name'] for articles in content['articles']]
        return source_list
    
    def get_news_articles(self, category, source):
        endpoint = f"v2/top-headlines?country=us&category={category}&pageSize=100"
        raw_content = requests.get(self.url + endpoint + self.API_KEY)
        content = raw_content.json()
        article_list = [article for article in content['articles'] if article['source']['name'] == source]
        return article_list
    
    def search_news(self, query):
        endpoint = f"/v2/everything?q={query}"
        size = f"&pageSize=20"
        raw_content = requests.get(self.url + endpoint + size + self.API_KEY)
        content = raw_content.json()
        article_list = content['articles']
        return article_list

        

# news = NewsAPI()
# print(news.search_news('biden'))
# # print(news.get_news_source())
# articles = news.get_news_articles('Buzzfeed')[0]
# print(articles['url'])
# print(articles['title'])


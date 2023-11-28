import requests

class NewsAPI:
    def __init__(self, category) -> None:
        self.category = category
        self.API_KEY = "&apiKey=01c355f31caa47399f2841c40959a965"
        self.url = f"https://newsapi.org/v2/top-headlines?country=us&category={self.category}"

    def get_news_source(self, page=1):
        page_number = f"&page={page}"
        raw_content = requests.get(self.url+page_number+self.API_KEY)
        content = raw_content.json()
        source_list = [articles['source']['name'] for articles in content['articles']]
        return source_list, content['totalResults']
    
    def get_news_articles(self, source):
        sources = self.content['articles']
        content = [article['url'] for article in sources if article['source']['name'] == source]
        # for article in sources:
        #     if article['source']['name'] == source:
        #         print(article['url'])
        return content
        

# news = NewsAPI('business')
# print(news.get_news_source()[0])
# print(news.get_news_source()[1])
# print(news.get_news_articles('Buzzfeed'))


    
# url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=01c355f31caa47399f2841c40959a965"
# # make request
# request = requests.get(url)

# # get dict of the data requested
# content = request.json()

# for article in content['articles']:
#     print(article['source']['name'])
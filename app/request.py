from .news import News
from .article import Articles
import urllib.request,json

#Getting api key
apikey=None

#getting the movie base url
base_url=None
#getting articles base url
Article_base_url=None

def configure_request(app):
    global apikey,base_url,Article_base_url
    apikey = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    Article_base_url=app.config['ARTICLE_API_URL']


def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = 'https://newsapi.org/v2/sources?apiKey=03a2bc584b204614aa752fb66a690094'

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        all_news_results = None

        if get_news_response['sources']:
            all_news_results_list = get_news_response['sources']
            all_news_results = process_results(all_news_results_list)


    return all_news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    all_news_results = []
   
    for all_news in news_list:
        id=all_news.get('id')
        name = all_news.get('name')
        url=all_news.get('url')
        description = all_news.get('description')
        category=all_news.get('category')
        country=all_news.get('country')
       

        if id:
            all_news_object = News(id,name,url,description,category,country)
            all_news_results.append(all_news_object)

    return all_news_results


def get_article(id):
    get_news_details_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=03a2bc584b204614aa752fb66a690094'.format(id)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        
        if news_details_response['articles']:
            news__article_list = news_details_response['articles']
            articles = process_article(news__article_list)
    return articles
       

def process_article(article_response_list):
    '''
    A function that returns the article respons list
    '''
    articles_results = []
    for articles in article_response_list:
        print(articles)
        id = articles.get('id')
        title=articles.get('title')
        author = articles.get('author')
        description = articles.get('decription')
        url = articles.get('url')
        urlToImage = articles.get('urlToImage')
        publishedAt = articles.get('publishedAt')
        content = articles.get('content')

        if urlToImage:
            article_object = Articles(id,title,author, description, url, urlToImage, publishedAt, content)
            articles_results.append(article_object)

    return articles_results


def search_article(news_name):
    search_news_url = 'https://newsapi.org/v2/sources?apiKey=03a2bc584b204614aa752fb66a690094 &query={}'.format(news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_news_results = process_results(search_news_list)


    return search_news_results
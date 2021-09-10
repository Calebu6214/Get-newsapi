from .news import News
from .article import Articles
import urllib.request,json

#Getting api key
apikey=None

#getting the movie base url
base_url=None

def configure_request(app):
    global apikey,base_url
    apikey = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,apikey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
   
    for news_item in news_list:
        id=news_item.get('id')
        # title = news_item.get('original_title')
        name = news_item.get('name')
        url=news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        description = news_item.get('description')
        publishedAt = news_item.get('publishedAt')
        country=news_item.get('country')

        if urlToImage:
            news_object = News(id,name,url,urlToImage,description,publishedAt,country)
            news_results.append(news_object)

    return news_results


def get_article(id):
    get_news_details_url = base_url.format(id,apikey)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            title = news_details_response.get('title')
            name = news_details_response.get('name')
            description = news_details_response.get('description')
            urlToImage = news_details_response.get('urlToImage')
            url=news_details_response.get('url')
            publishedAt = news_details_response.get('publishedAt')

            news_object = News(id,title,name,description,urlToImage,url,publishedAt)

    return news_object
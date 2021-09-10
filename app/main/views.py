from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_new,get_news

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title='Home-See your news'
    return render_template('index.html', title=title)


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular news
    popular_news = get_news('popular')
    print(popular_news)
    popular_article=get_news('popular_article')
    title = 'Home - News site'

    # search_news=request.args.get('news_query')

    # if search_news:
    #     return redirect(url_for('main.search',news_name=search_news))
    # else:
    #     return render_template('index.html', title = title,popular=popular_news)
    return render_template('index.html', title = title,popular = popular_news,popular_article=popular_article)
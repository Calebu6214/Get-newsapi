from app.article import Articles
from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_article,get_news
from app.request import search_article

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    all_news=get_news()
    title='Home-See your news'
    search_article=request.args.get('article_query')
    if search_article:
        return redirect(url_for('main.search',news_name=search_article))
    else:
    # if search_article:
        return render_template('index.html', title=title,all_news=all_news)


@main.route('/news/<id>')
def articles(id):

    '''
    View root page function that returns the index page and its data
    '''

    # Getting articles news
  
    articles=get_article(id)
    # return render_template('news.html', articles = articles)

    search_news=request.args.get('article_query')

    if search_news:
        return redirect(url_for('main.search',news_name=search_news))
    else:
       return render_template('news.html',articles=articles)
    

@main.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_article(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',title=title,all_news = searched_news)
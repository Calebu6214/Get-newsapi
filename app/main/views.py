from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_article, get_new,get_news

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    all_news=get_news()
    title='Home-See your news'
    return render_template('index.html', title=title,all_news=all_news)


@main.route('/news/<int:id>')
def news(id):

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular news
  
    results=get_article(id)

    # search_news=request.args.get('news_query')

    # if search_news:
    #     return redirect(url_for('main.search',news_name=search_news))
    # else:
    #     return render_template('index.html', title = title,popular=popular_news)
    return render_template('news.html', results = results,)
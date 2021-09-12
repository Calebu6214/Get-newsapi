import os

class Config:

    ARTICLE_API_URL ='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_API_BASE_URL='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    # ARTICLE_API_URL=os.environ.get(ARTICLE_API_URL)
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
class News:
    '''
    news class to define news Objects
    '''

    def __init__(self,title,name,urlToImage,description,publishedAt):
    
        self.title = title
        self.name = name
        self.urlToImage = "https://image.tmdb.org/t/p/w500/" + urlToImage
        self.description = description
        self.publishedAt = publishedAt
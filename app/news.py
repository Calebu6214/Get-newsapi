class News:
    '''
    news class to define news Objects
    '''

    def __init__(self,id,title,name,url,urlToImage,description,publishedAt):
        self.id=id
        self.title = title
        self.name = name
        self.url=url
        self.urlToImage =  urlToImage
        self.description = description
        self.publishedAt=publishedAt
        # self.category = category
        # self.country = country
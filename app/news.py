class News:
    '''
    news class to define news Objects
    '''

    def __init__(self,id,name,url,description,category,country):
        self.id=id
        self.name = name
        self.url=url
        self.description = description
        self.category = category
        self.country = country
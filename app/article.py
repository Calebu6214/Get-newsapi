class Articles:
  '''
  articles class to define article objects
  '''
  def __init__(self,id,title,author,description,url,urlToImage,publishedAt,content):
    self.id = id
    self.title=title
    self.author = author
    self.description = description
    self.url = url
    self.urlToImage = urlToImage
    self.publishedAt = publishedAt
    self.content = content
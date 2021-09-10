
import unittest
from app.article import Articles


class ArticlesTest(unittest.TestCase):
  '''
  Test Class to test the behaviour of the Articles class
  '''

  def setUp(self):
    '''
    Set up method that will run before every test
    '''
    self.new_articles = Articles('id','author','description','https://www.businessdailyafrica.com/bd/corporate/companies/suspended-ktda-chief-lerionka-tiampati-resigns-3545802',"https://www.businessdailyafrica.com/resource/image/3545836/landscape_ratio16x9/1160/652/aedf809f98335642414d6369b40b719e/Wu/ktda.jpg",'11/9/2021','content')


  def test_instance(self):
    self.assertTrue(isinstance(self.new_articles,Articles))

if __name__ == '__main__':
  unittest.main()   
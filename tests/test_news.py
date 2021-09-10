import unittest
from app.models import News


class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('Politics','Uhuru and Ruto','https://businesstoday.co.ke/wp-content/uploads/2019/11/Uhuruto_Madam-Magazine-Kenya.jpg',10/9/2021)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()
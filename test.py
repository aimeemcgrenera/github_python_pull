import unittest
from unittest.mock import patch
from mock import Mock
from main import *

class TestApi(unittest.TestCase):

    def setUp(self):
        self.instance = GithubApiData()
        self.__api_url = 'https://api.github.com/search/repositories'
        self.__api_query = 'language:python'
        self.__api_sort = 'stars'
        self.__api_order = 'desc'

    @patch('main.requests.get')
    def test_api_call(self, mock_get):
        """Mocking using a decorator"""
        mock_get.return_value.status_code = 200  # Mock status code of response.
        response = self.instance.api_call()
        print(response.status_code)

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.status_code, 200)

    def test_process_response(self, response):


    def test_create_df(self):


    def test_push_to_bq(self):



if __name__ == '__main__':
    unittest.main()
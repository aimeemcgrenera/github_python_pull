import unittest
from unittest.mock import patch
from mock import Mock
from main import *
import json

class TestApi(unittest.TestCase):

    def setUp(self):
        self.test_instance = GithubApiData()
        self.__columns = ['repository_id', 'name', 'url', 'created_date', 'last_push_date', 'description', 'stars']
        self.__bq_project_id = 'aerobic-ward-248616'
        self.__dataset_name = 'outside_data'
        self.__datatable_name = 'top_github_python_repos'


    @patch('requests.get') # mock 'requests' module 'get' method
    def test_api_call(self, mock_get):
        """Mocking using a decorator"""
        mock_get.return_value.status_code = 200  # Mock status code of response.
        response = self.test_instance.api_call()
        print(response.status_code)
        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.status_code, 200)
        # Assert that the JSON object has data
        self.assertIsNotNone(json.loads(response.text))


    def test_process_response(self):
        mock_response = self.test_instance.api_call()
        mock_rows = self.test_instance.process_response(mock_response)
        # assert type of return is list and length is 25
        assert type(mock_rows) == list
        assert len(mock_rows) == 25


    def test_create_df(self):
        mock_response = self.test_instance.api_call()
        mock_rows = self.test_instance.process_response(mock_response)
        mock_df = self.test_instance.create_df(mock_rows, self.__columns)
        # assert instance is a Pandas DataFrame
        assert isinstance(mock_df, pd.DataFrame)

    def test_push_to_bq(self):
        mock_df = Mock(spec=pd.DataFrame)
        function_state = self.test_instance.push_to_bq(mock_df, self.__bq_project_id, self.__dataset_name, self.__datatable_name)
        # assert that it hits the function_state of True
        self.assertTrue(function_state)


if __name__ == '__main__':
    unittest.main()
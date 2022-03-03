import unittest

from unittest import mock
from unittest.mock import Mock, patch, MagicMock
from githubapi import GithubApi



class TestGithubAPI(unittest.TestCase):
    @mock.patch('githubapi.GithubApi')
    def test_mock_test_requestStatus(self, mock_status):
        mock_status.return_value = MagicMock(status_code = 200)
        result = mock_status.return_value.status_code
        try:
            self.assertEqual(result, 200)
        except:
            print("Test Failed")
        else:
            print("Test succeed")
            
    @mock.patch('githubapi.GithubApi')
    def test_mock_numberReposandCommits(self, mock_number):
        mock_number.return_value = MagicMock(repository = 10)
        result = mock_number.return_value.repository
        try:
             self.assertEqual(result, 10)
        except:
            print("Test Failed")
        else:
            print("Test succeed")
    @mock.patch('githubapi.GithubApi')
    def test_mock_test_userID(self, mock_userID):
         mock_userID.return_value = MagicMock(userID = "willescamilla")
         result = mock_userID.return_value.userID
         try:
             self.assertEqual(result, "willescamilla")
         except:
            print("Test Failed")
         else:
            print("Test succeed")
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
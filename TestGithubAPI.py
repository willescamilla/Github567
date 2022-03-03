import unittest

from unittest import mock
from githubapi import GithubApi

@mock.patch('githubapi.GithubApi')
def mock_github_call(mock_GithubApi_func):
    mock_GithubApi_func.return_value = False

class TestGithubAPI(unittest.TestCase):
    def testGithubNone(self):
        self.assertEqual(GithubApi('?'), False)
    def testGithubNone2(self):
        self.assertEqual(GithubApi('willesc'), False)
    def testGithubSelf(self):
        self.assertEqual(len(GithubApi('willescamilla')), True)
    def testNoId(self):
        self.assertEqual(GithubApi(''), False)
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
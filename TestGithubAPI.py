import unittest

from unittest import mock
from githubapi import GithubApi

@mock.patch('githubapi.GithubApi')
def mock_github_call(mock_GithubApi_func):
    mock_GithubApi_func.return_value = []

class TestGithubAPI(unittest.TestCase):
    def testGithubNone(self):
        self.assertEqual(GithubApi('?'), [])
    def testGithubNone2(self):
        self.assertEqual(GithubApi('willesc'), [])
    def testGithubSelf(self):
        self.assertEqual(len(GithubApi('willescamilla')), 25)
    def testNoId(self):
        self.assertEqual(GithubApi(''), [])
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
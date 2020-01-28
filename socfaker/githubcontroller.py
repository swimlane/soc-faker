from github import Github

from .constants import __GITHUB_PAT__ as __GITHUB_PAT__

class GitHubController(object):

    def __init__(self):
        self.github = Github(__GITHUB_PAT__)
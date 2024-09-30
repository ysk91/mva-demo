from modules import config
from github import Github
from github import Auth

access_token = config.GITHUB_TOKEN
auth = Auth.Token(access_token)

g = Github(auth=auth)

owner = "ysk91"
repository = "mva-demo"
repo = g.get_repo(f"{owner}/{repository}")

def create_pr(head, title, body):
    repo.create_pull(base="main", head=head, title=title, body=body)

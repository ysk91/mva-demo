from modules import config
from github import Github
from github import Auth

access_token = config.GITHUB_TOKEN
auth = Auth.Token(access_token)

g = Github(auth=auth)

owner = "ysk91"
repository = "mva-demo"
repo = g.get_repo(f"{owner}/{repository}")

def create_issue(title, body):
    issue = repo.create_issue(
        title=title,
        body=body
    )

    print(f"Issue created: {issue.html_url}")

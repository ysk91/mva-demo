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

def create_new_branch(new_branch_name, repo=repo, base_branch_name="main"):
    source = repo.get_branch(base_branch_name)

    repo.create_git_ref(
        ref=f"refs/heads/{new_branch_name}",
        sha=source.commit.sha
    )

from modules import config
from github import Github
from github import Auth

ACCESS_TOKEN = config.GITHUB_TOKEN
REPOSITORY_PATH = config.REPOSITORY_PATH
auth = Auth.Token(ACCESS_TOKEN)

g = Github(auth=auth)
repo = g.get_repo(REPOSITORY_PATH)


def create_issue(title, body):
    issue = repo.create_issue(title=title, body=body)

    print(f"Issue created: {issue.html_url}")


def get_module_contents(path):
    try:
        file_content = repo.get_contents(f"modules/{path}")
        decoded_content = file_content.decoded_content.decode("utf-8")
        return {f"modules/{path}: {decoded_content}"}
    except Exception as e:
        if "Not Found" in str(e):
            print(f"Skipping {path} (not found in repo)")
            return None
        else:
            print(f"Error retrieving {path}: {e}")
            return None

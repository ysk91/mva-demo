from modules import config
from github import Github
from github import Auth

ACCESS_TOKEN = config.GITHUB_TOKEN
REPOSITORY_PATH = config.REPOSITORY_PATH
auth = Auth.Token(ACCESS_TOKEN)

g = Github(auth=auth)
repo = g.get_repo(REPOSITORY_PATH)


def get_file_contents(path, base_path=None):
    try:
        full_path = f"{base_path}/{path}" if base_path else path
        file_content = repo.get_contents(full_path)
        decoded_content = file_content.decoded_content.decode("utf-8")
        return {full_path: decoded_content}
    except Exception as e:
        if "Not Found" in str(e):
            print(f"Skipping {full_path} (not found in repo)")
        else:
            print(f"Error retrieving {full_path}: {e}")
        return None


def create_issue(title, body):
    issue = repo.create_issue(title=title, body=body)
    print(f"Issue created: {issue.html_url}")

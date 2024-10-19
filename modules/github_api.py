import os

from git import InvalidGitRepositoryError, Repo
from github import Auth, Github

from modules import config

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


def get_local_repo_path():
    try:
        repo = Repo(os.getcwd(), search_parent_directories=True)
        return repo.git.rev_parse("--show-toplevel")
    except InvalidGitRepositoryError:
        raise Exception(
            "The current working directory is not a valid Git repository."
        )


LOCAL_REPO_PATH = get_local_repo_path()
local_repo = Repo(LOCAL_REPO_PATH)


def checkout(branch_name):
    try:
        local_repo.remotes.origin.fetch()
        local_repo.git.checkout(branch_name)
    except Exception as e:
        print(f"Error checking out {branch_name}: {e}")


def commit_and_push_to_branch(branch_name, commit_message):
    local_repo.git.add('foods.yml')
    local_repo.index.commit(commit_message)

    origin = local_repo.remote(name="origin")
    origin.push(f"HEAD:refs/heads/{branch_name}")

    print(f"Changes pushed to {branch_name}")

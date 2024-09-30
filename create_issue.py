import modules.github_api

g = modules.github_api

issue_title = "New Issue"

text = 'テストテキスト'

issue_body = f"""
This is the body of the new issue.

Tis is {text}
"""

new_issue = g.create_issue(issue_title, issue_body)

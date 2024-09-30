import modules.github_api

g = modules.github_api

head = "feature/add_github-api"

title = "Create PR"

body = '''
## SUMMARY

This PR is test.

## TESTS
  - [x] チェックつきリスト
  - [ ] チェックなしリスト
'''

g.create_pr(head, title, body)

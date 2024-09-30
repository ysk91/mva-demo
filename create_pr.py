import modules.github_api

g = modules.github_api

branch = 'feature/test'

g.create_new_branch(branch)

title = "Create PR"

body = '''
## SUMMARY

This PR is test.

## TESTS
  - [x] チェックつきリスト
  - [ ] チェックなしリスト
'''

g.create_pr(branch, title, body)

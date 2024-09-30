# テスト用

import os
import modules.rescue_issue

rescue_issue = modules.rescue_issue

try:
    1 / 0
except Exception as e:
    script_path = os.path.basename(__file__)
    rescue_issue.rescue_issue(e, script_path)

from dotenv import load_dotenv
load_dotenv()

import os

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GPT_MODEL = os.getenv('GPT_MODEL')

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPOSITORY_PATH = os.getenv('REPOSITORY_PATH')

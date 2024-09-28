from dotenv import load_dotenv
load_dotenv()

import os

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GPT_MODEL = os.getenv('GPT_MODEL')

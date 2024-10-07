import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GPT_MODEL = os.getenv("GPT_MODEL")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_OWNER = os.getenv("GITHUB_OWNER")
REPOSITORY = os.getenv("REPOSITORY")
REPOSITORY_PATH = f"{GITHUB_OWNER}/{REPOSITORY}"

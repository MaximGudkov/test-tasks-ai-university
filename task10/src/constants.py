import os

from dotenv import load_dotenv

load_dotenv()

GITHUB_API_URL = os.environ.get("API_URL", "https://api.github.com/users/")

CREDENTIALS_PATH = os.environ.get("CREDENTIALS_PATH", r"../credentials.example.json")

SPREADSHEET_ID = os.environ.get("SPREADSHEET_ID", "your_sheet_id")
SPREADSHEET_RANGE = "A1:AF100"

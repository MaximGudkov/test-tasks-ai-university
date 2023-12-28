import googleapiclient.discovery
from google.oauth2 import service_account

from src.constants import CREDENTIALS_PATH

credentials = service_account.Credentials.from_service_account_file(
    CREDENTIALS_PATH,
    scopes=["https://www.googleapis.com/auth/spreadsheets"],
)

google_sheets_service = googleapiclient.discovery.build(
    "sheets", "v4", credentials=credentials
)

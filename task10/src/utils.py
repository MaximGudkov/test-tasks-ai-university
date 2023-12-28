import httpx
from fastapi import HTTPException

from src.constants import GITHUB_API_URL, SPREADSHEET_ID, SPREADSHEET_RANGE
from src.service import google_sheets_service


async def get_github_user_data(username: str):
    github_url = GITHUB_API_URL + username

    async with httpx.AsyncClient() as client:
        response = await client.get(github_url)
        if response.is_success:
            return response.json()
        else:
            raise HTTPException(
                status_code=response.status_code, detail="GitHub API request failed"
            )


def add_data_to_sheet(user_data):
    keys = list(user_data.keys())
    values = list(user_data.values())

    body = {"values": [keys, values]}

    google_sheets_service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=SPREADSHEET_RANGE,
        body=body,
        valueInputOption="RAW",
    ).execute()


def get_sheet_data():
    result = (
        google_sheets_service.spreadsheets()
        .values()
        .get(spreadsheetId=SPREADSHEET_ID, range=SPREADSHEET_RANGE)
        .execute()
    )

    values = result.get("values", [])

    return values

import httpx
from fastapi import APIRouter, HTTPException

from src.constants import GITHUB_API_URL, SPREADSHEET_ID, SPREADSHEET_RANGE
from src.service import google_sheets_service

router = APIRouter()


@router.get("/github/{username}")
async def get_github_user_info(username: str):
    github_url = GITHUB_API_URL + username
    async with httpx.AsyncClient() as client:
        response = await client.get(github_url)
        if response.status_code == 200:
            user_info = response.json()
            return user_info
        else:
            raise HTTPException(
                status_code=response.status_code, detail="User not found"
            )


@router.post("/add-to-sheet")
async def add_to_sheet(username: str):
    github_url = GITHUB_API_URL + username

    async with httpx.AsyncClient() as client:
        response = await client.get(github_url)
        if response.is_success:
            user_data = response.json()
        else:
            raise HTTPException(
                status_code=response.status_code, detail="GitHub API request failed"
            )

    keys = list(user_data.keys())
    values = list(user_data.values())

    body = {"values": [keys, values]}

    google_sheets_service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=SPREADSHEET_RANGE,
        body=body,
        valueInputOption="RAW",
    ).execute()

    return {"status": "success", "message": "Data added to Google Sheets"}


@router.get("/get-from-sheet")
async def get_from_sheet():
    result = (
        google_sheets_service.spreadsheets()
        .values()
        .get(spreadsheetId=SPREADSHEET_ID, range=SPREADSHEET_RANGE)
        .execute()
    )

    values = result.get("values", [])

    return values

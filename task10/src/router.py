import httpx
from fastapi import APIRouter

from src.utils import add_data_to_sheet, get_github_user_data, get_sheet_data

router = APIRouter()


@router.get("/github/{username}")
async def get_github_user_info(username: str):
    user_info = await get_github_user_data(username)
    return user_info


@router.get("/add-to-sheet")
async def add_to_sheet(username: str):
    user_data = await get_github_user_data(username)
    add_data_to_sheet(user_data)
    return {"status": "success", "message": "Data added to Google Sheets"}


@router.get("/get-from-sheet")
async def get_from_sheet():
    result = get_sheet_data()
    return result

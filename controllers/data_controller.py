from fastapi import APIRouter
from helpers.fetch_data import fetch_all
from pydantic import BaseModel
from models.setting import Setting

router = APIRouter()

class SyncInfo(BaseModel):
    fromDate: str
    endDate: str

@router.post("/sync-data")
async def sync_data(info: SyncInfo):
    setting = await Setting.filter(key="from_date").first() or Setting(key="from_date")
    setting.value = info.fromDate
    await setting.save()

    setting2 = await Setting.filter(key="end_date").first() or Setting(key="end_date")
    setting2.value = info.endDate
    await setting2.save()

    fetch_response = await fetch_all()
    return { "success": True, **fetch_response}

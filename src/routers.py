from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from src.documents import Test


router = APIRouter(prefix="/tests", tags=["tests"])


@router.get("/", response_description="List")
async def get_list() -> List[Test]:
    data = await Test.find_all().to_list()
    return data


@router.post("/", response_description="Create")
async def create(test: Test) -> Test:
    data = await test.create()
    return data


@router.get("/{test_id}", response_description="Retrieve")
async def get_retrieve(test_id: PydanticObjectId) -> Test:
    data = await Test.get(test_id)
    if not data:
        raise HTTPException(status_code=404, detail="Record was not found!")
    return data


@router.put("/{test_id}", response_description="Update")
async def update(test_id: PydanticObjectId, test: Test) -> Test:
    data = await Test.find_one(Test.id == test_id)
    if not data:
        raise HTTPException(status_code=404, detail="Record was not found!")
    await data.set(test.model_dump(exclude_unset=True))
    return data


@router.delete("/{test_id}", response_description="Delete")
async def delete(test_id: PydanticObjectId) -> dict:
    data = await Test.get(test_id)
    if not data:
        raise HTTPException(status_code=404, detail="Record was not found!")
    await data.delete()
    return {"message": "Record deleted successfully"}

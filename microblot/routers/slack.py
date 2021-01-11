from fastapi import APIRouter


router = APIRouter(prefix="/slack")


@router.get("/")
async def root():
    return {"slack": "root"}


@router.get("/sucks")
async def sucks():
    return {"slack": "sucks"}

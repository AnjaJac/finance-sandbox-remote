from fastapi import APIRouter

router = APIRouter(
    prefix="/tests",
    tags=["Users"]
)

@router.get("/")
async def get_users():
    return {"message": "Users endpoint hitting successfully"}
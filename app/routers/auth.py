from fastapi import APIRouter, Depends, HTTPException



router = APIRouter(
    tags=['auth']
)


@router.post('/login')
async def login():
    pass
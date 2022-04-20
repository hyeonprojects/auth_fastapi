from fastapi import Depends, FastAPI

app = FastAPI()

app.include_router()

@app.get('/')
async def auth_test():
    return '회원 관련 API'

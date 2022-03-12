from fastapi import Depends
from fastapi.security import SecurityScopes


SECRET_KEY = ''
ALGORITHM = ''
ACCESS_TOKEN_EXPRIRE_MINUTES = 30

async def get_current_user(security_scopes: SecurityScopes, token: str = Depends()):
    print("hyeon")
    pass

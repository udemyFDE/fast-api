'''

import APIRouter from fastapi which will allow us to be able to route from main.py file to auth.py

in main.py import this auth.py to use this router
'''

from fastapi import APIRouter

# Instead of app = FastAPI(), we have this
router = APIRouter()

# use the same variable used for APIRouter(), instead of @app.get --> @router.get
@router.get("/auth/")

async def get_user():
    return {"user": "Authenticated"}
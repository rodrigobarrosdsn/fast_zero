from fastapi import Depends, FastAPI

app = FastAPI()


@app.get('/')
async def read_root():
    return {'message': 'Welcome to the Fast Zero API!'}


from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from .db import get_session


@app.get('/db-status')
async def db_status(session: AsyncSession = Depends(get_session)):
    result = await session.execute(text('SELECT 1'))  # Use text()
    return {'db_status': result.scalar() == 1}
from repository.db import get_session
from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


app = FastAPI()


@app.get('/')
async def read_root():
    return {'message': 'Welcome to the Fast Zero API!'}


@app.get('/db-status')
async def db_status(session: AsyncSession = Depends(get_session)):
    result = await session.execute(text('SELECT 1'))  # Use text()
    return {'db_status': result.scalar() == 1}

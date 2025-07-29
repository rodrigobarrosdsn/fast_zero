import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

# Carrega variáveis de ambiente
load_dotenv()

DATABASE_URL = f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

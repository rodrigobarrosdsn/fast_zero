from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def read_root():
    return {'message': 'Welcome to the Fast Zero API!'}

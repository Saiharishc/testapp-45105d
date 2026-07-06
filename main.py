from fastapi import FastAPI

app = FastAPI()

@app.get('/items')
async def list_items():
    return []

@app.get('/')
async def read_root():
    return {"message": "Welcome to TestApp"}

@app.get('/api/health')
async def health_check():
    return {"status": "ok"}

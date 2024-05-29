from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root(message: str):
    return {"received_message": message}


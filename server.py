from fastapi import FastAPI
import uvicorn
from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
async def root():
    return {"Server_page"}

if __name__ == "__main__":
    uvicorn.run("server:app", host='0.0.0.0', port=8000, reload=True)
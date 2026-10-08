import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Abra Business Backend is Live!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
  

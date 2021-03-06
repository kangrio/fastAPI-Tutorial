from fastapi import FastAPI

app = FastAPI()

# Path Parameter แบบ path

@app.get("/files/{file_path:path}")
async def read_file(file_path : str):
    return {"file_path" : file_path}


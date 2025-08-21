from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
import os
import uuid
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def main():
    return """
    <html>
        <body>
            <h1>File Upload</h1>
            <form action="/uploadfile/" enctype="multipart/form-data" method="post">
                <input type="file" name="file"><br><br>
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """
    
@app.post("/files")
async def create_file(file: Annotated[bytes | None, File()]=None):
    if not file:
        return {"msg":"empty file"}
    
    filename = f"{uuid.uuid4()}.bin"
    save_path = f"upload/{filename}"
    
    os.makedirs("uploads", exist_ok=True)
    
    with open (save_path, "wb") as buffer:
        buffer.write(file)
        
    return {'file_size':len(file)}
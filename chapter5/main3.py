from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
import os
import uuid
from pydantic import BaseModel, Field
import shutil

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def main():
    return """
    <html>
        <body>
            <h1>File Upload (bytes)</h1>
            <form action="/files/" enctype="multipart/form-data" method="post">
                <input type="file" name="file"><br><br>
                <input type="submit" value="Upload">
            </form>
            <h1>File Upload (Uploadfile)</h1>
            <form action="/uploadfile/" enctype="multipart/form-data" method="post">
                <input type="file" name="file"><br><br>
                <input type="submit" value="Upload">
            </form>
            <h1>File Upload (Uploadfile)</h1>
            <form action="/uploadfile/" enctype="multipart/form-data" method="post">
                <input type="files" name="file" multiple><br><br>
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """

@app.post('/uploadfile')
async def uplaod_file(file: Annotated[UploadFile | None, File()]=None):
    if not file:
        return {"msg":"empty file"}
    
    save_path = f"uploads/{file.filename}"
    
    os.makedirs("uploads", exist_ok=True)
    
    with open (save_path, "wb") as buffer:
        buffer.write(file)
        shutil.copyfileobj(file.file, buffer)
    return {"filename":file.filename, "content_type":file.content_type}


#Multiple
@app.post('/multiplefile')
async def multi_file(files: Annotated[list[UploadFile], File()]):
    
    save_files= []
    os.makedirs("uploads", exist_ok=True)
    for file in files:
        save_path = f"upload/{files.filename}"
        with open (save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        save_files.append(file.filename)
    return save_files
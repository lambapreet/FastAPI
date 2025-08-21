from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
import os
import uuid
import shutil

app = FastAPI()



@app.get("/", response_class=HTMLResponse)
async def main():
    return """
    <html>
        <body>
            <h2>Login & File Upload</h2>
            <form action="/login/" enctype="multipart/form-data" method="post">
                
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required><br><br>

                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required><br><br>

                <label for="file">Upload File:</label>
                <input type="file" id="file" name="file" accept="image/*"><br><br>

                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """

@app.post("/login/")
async def user(username: Annotated[str, Form()],file:Annotated[UploadFile | None, File()]=None):
    response = {'username':username}
    if file:
        save_path = f"uploads/{file.filename}"
        os.makedirs("uploads", exist_ok=True)
        with open (save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            response['Filename'] = file.filename
        return response
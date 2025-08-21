from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
    <html>
        <body>
            <h2>Form</h2>
            <form action="/login/" method="post">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required><br><br>

                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required><br><br>

                <input type="submit" value="Login">
            </form>
        </body>
    </html>
    """
    
class FormData(BaseModel):
    username:str = Field(min_length=5)
    password:str = Field(min_length=8,max_length=12)
    model_config = {"extra":"forbid"}

@app.post('/login/')
async def login(data: Annotated[FormData, Form()]):
    return data
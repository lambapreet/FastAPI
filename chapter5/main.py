from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from typing import Annotated

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

@app.post('/login')
async def login(username:Annotated[str, Form()],password:Annotated[str, Form()],):
    return{"username":username,"password_length":len(password)}
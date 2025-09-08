from fastapi import FastAPI, BackgroundTasks


app = FastAPI()


def write_notifiaction(email:str, message:str):
    with open("log.txt",mode="w") as email_file:
        content = f"notification for {email}:{message}"
        email_file.write(content)
        
        
@app.post("/send-notification/{email}")
async def send_notification(email:str, background_tasks:BackgroundTasks):
    background_tasks.add_task(write_notifiaction,email, message="some notification")
    return {"message":"Sent!"}
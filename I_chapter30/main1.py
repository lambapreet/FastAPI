from fastapi import FastAPI, BackgroundTasks, UploadFile, File
import time
import os


app = FastAPI()


def save_file(filename:str,file_content:bytes):
    print(f"Starting background task:Saving File '{filename}'")
    start_time = time.time()
    time.sleep(5)
    with open(f"uploads/{filename}","wb") as file:
        file.write(file_content)
    end_time = time.time()
    
    print(f"Competed task: File '{filename}' saved_in {end_time-start_time:.2f} seconds")
    
    
@app.post("/upload-file")
async def upload_file(file: UploadFile = File(...),background_tasks: BackgroundTasks=None):
    os.makedirs("uploads", exist_ok=True)
    
    content = await file.read()
    
    background_tasks.add_task(save_file. file.filename, content)
    return {"message": f"File '{file.filename}' is being saved in background."}
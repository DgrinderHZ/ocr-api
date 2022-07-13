
import time
from typing import List
import utils
import ocr
import asyncio

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Visit the endpoint: /api/v1/extract_text to perform OCR.'}



@app.post("/api/v1/extract_text")
async def extract_text(Images: List[UploadFile] = File(...)):
    response = {}
    s = time.time()
    tasks = []
    for img in Images:
        print("Images Upladed : ", img.filename)
        temp_file = utils._save_file_to_server(img, path="./", save_as=img.filename)
        tasks.append(asyncio.create_task(ocr.read_image(temp_file)))
    text = await asyncio.gather(*tasks)
    for i, t in enumerate(text):
        response[Images[i].filename] = t
        
    response["Time Taken"] = round((time.time() - s), 2)

    return response


@app.post("/predict") 
def prediction(file: bytes = File(...)):
    label = ocr.read_image2(utils._return_img(file))
    return {'image content': label}


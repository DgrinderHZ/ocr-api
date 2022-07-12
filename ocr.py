import asyncio
import os
import pytesseract

if os.environ["ENV_VAR"] == "WIN":
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
elif os.environ["ENV_VAR"] == "her":
    pytesseract.pytesseract.tesseract_cmd = "/app/.apt/usr/bin/tesseract"

async def read_image(img_path, lang='eng'):
    try:
        text = pytesseract.image_to_string(img_path, lang=lang)
        await asyncio.sleep(2)
        return text
    except:
        return "[ERROR] Unable to process file: {0}".format(img_path)

# img_path = 'rd.jpeg'
# lang = 'eng'
# text = pytesseract.image_to_string(img_path, lang=lang)
# print(text)

import io
import os
import shutil
import cv2

import numpy as np


def _save_file_to_server(uploaded_file, path=".", save_as="default"):
    # extention = os.path.splitext(uploaded_file.filename)[-1]
    temp_file = os.path.join(path, save_as)

    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)
    
    return temp_file

def _return_img(uploaded_file):
    image_stream = io.BytesIO(uploaded_file)
    image_stream.seek(0)
    file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    return frame
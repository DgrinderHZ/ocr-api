
import os
import shutil


def _save_file_to_server(uploaded_file, path=".", save_as="default"):
    extention = os.path.splitext(uploaded_file.filename)[-1]
    temp_file = os.path.join(path, save_as + extention)

    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)
    
    return temp_file
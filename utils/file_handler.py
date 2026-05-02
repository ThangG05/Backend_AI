import uuid
import shutil
import os

def save_temp_file(file):
    filename = f"temp_{uuid.uuid4()}.mp3"

    with open(filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return filename

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
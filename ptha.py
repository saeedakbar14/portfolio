import zipfile
import os
from flask import Flask, request

app = Flask(__name__)

UPLOAD_FOLDER = "/tmp/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_zip():
    file = request.files["file"]
    zip_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(zip_path)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(UPLOAD_FOLDER)  

    return "File uploaded and extracted"

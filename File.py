import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route("/load", methods=["POST"])
def load_data():
    data = request.data
    obj = pickle.loads(data)  # 🚨 Insecure deserialization
    return str(obj)

if __name__ == "__main__":
    app.run()

from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the trained model
model = pickle.load(open("placement_model.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    
    data = request.json

    # Extract features from request
    test_score = data.get("testScore")
    percentage = data.get("percentage")

    # Prepare input for model
    features = np.array([test_score, percentage]).reshape(1, -1)

    # Make prediction
    prediction = model.predict(features)

    return jsonify({
        "placement_chance": int(prediction[0])
    })

if __name__ == "__main__":
    app.run(port=5001)

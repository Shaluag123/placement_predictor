from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)

# ✅ Load model and encoders
model = pickle.load(open("placement_model_final.pkl", "rb"))
le_stream = pickle.load(open("le_stream.pkl", "rb"))
le_tier = pickle.load(open("le_tier.pkl", "rb"))
le_internship = pickle.load(open("le_internship.pkl", "rb"))
le_skills = pickle.load(open("le_skills.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        # Get raw values from frontend
        test_score = int(data["testScore"])
        perc_10th = float(data["percentage_10th"])
        perc_12th = float(data["percentage_12th"])
        perc_grad = float(data["percentage_grad"])
        stream = data["stream"].strip().upper()
        tier = data["college_tier"].strip().capitalize()
        internship = data["internship"].strip().capitalize()
        certs = int(data["certifications"])
        projects = int(data["projects"])
        skills = data["skills"].strip().capitalize()

        # Encode categorical fields
        stream_encoded = le_stream.transform([stream])[0]
        tier_encoded = le_tier.transform([tier])[0]
        internship_encoded = le_internship.transform([internship])[0]
        skills_encoded = le_skills.transform([skills])[0]

        # Prepare input
        input_df = pd.DataFrame([{
            "Percentage_10th": perc_10th,
            "Percentage_12th": perc_12th,
            "Percentage_Grad": perc_grad,
            "Stream": stream_encoded,
            "College_Tier": tier_encoded,
            "Internship": internship_encoded,
            "Certifications": certs,
            "Projects": projects,
            "Skills": skills_encoded,
            "TestScore": test_score
        }])

        # Make prediction
        prediction = model.predict(input_df)
        return jsonify({"placement_chance": int(prediction[0])})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5001)

import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("placement_data_final.csv")

# Encode categorical features
le_stream = LabelEncoder()
df["Stream"] = le_stream.fit_transform(df["Stream"])

le_tier = LabelEncoder()
df["College_Tier"] = le_tier.fit_transform(df["College_Tier"])

le_internship = LabelEncoder()
df["Internship"] = le_internship.fit_transform(df["Internship"])

le_skills = LabelEncoder()
df["Skills"] = le_skills.fit_transform(df["Skills"])

# Features and label
X = df[[
    "Percentage_10th", "Percentage_12th", "Percentage_Grad",
    "Stream", "College_Tier", "Internship",
    "Certifications", "Projects", "Skills", "TestScore"
]]
y = df["Placed"]

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and encoders
pickle.dump(model, open("placement_model_final.pkl", "wb"))
pickle.dump(le_stream, open("le_stream.pkl", "wb"))
pickle.dump(le_tier, open("le_tier.pkl", "wb"))
pickle.dump(le_internship, open("le_internship.pkl", "wb"))
pickle.dump(le_skills, open("le_skills.pkl", "wb"))

print("✅ Model and encoders saved successfully.")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
data = pd.read_csv("placement_data.csv")

# Feature Engineering
X = data[['test_score', 'percentage']]
y = data['placed']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("placement_model.pkl", "wb"))

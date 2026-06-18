import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("Dataset/heart_attack_prediction_indonesia.csv")

# Remove column with many missing values
df = df.drop(columns=["alcohol_consumption"])

# Encode categorical columns
encoder = LabelEncoder()

for col in df.select_dtypes(include=["object", "string"]).columns:
    df[col] = encoder.fit_transform(df[col])

# Features and target
X = df.drop("heart_attack", axis=1)
y = df["heart_attack"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Random Forest
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Save model
joblib.dump(model, "Models/heart_attack_model.pkl")

print("Model Saved Successfully!")
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv(
    "Dataset/heart_attack_prediction_indonesia.csv"
)

# Important Features Only
FEATURES = [
    "age",
    "gender",
    "hypertension",
    "diabetes",
    "cholesterol_level",
    "obesity",
    "family_history",
    "stress_level",
    "sleep_hours",
    "blood_pressure_systolic",
    "blood_pressure_diastolic",
    "previous_heart_disease"
]

TARGET = "heart_attack"

# Select required columns
df = df[FEATURES + [TARGET]]

# Encode categorical columns
encoder = LabelEncoder()

for col in df.select_dtypes(include=["object", "string"]).columns:
    df[col] = encoder.fit_transform(df[col])

# Features and Target
X = df[FEATURES]
y = df[TARGET]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Accuracy
predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nModel Accuracy")
print(round(accuracy * 100, 2), "%")

# Save Model
joblib.dump(
    model,
    "Models/heart_attack_model.pkl"
)

print("\nNew Model Saved Successfully!")

print("\nFeatures Used:")
for feature in FEATURES:
    print("-", feature)
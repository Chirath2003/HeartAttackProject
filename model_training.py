import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# Load dataset
df = pd.read_csv("Dataset/heart_attack_prediction_indonesia.csv")

# Drop alcohol column (60% missing values)
df = df.drop(columns=["alcohol_consumption"])

# Encode categorical columns
encoder = LabelEncoder()

for col in df.select_dtypes(include=["object", "string"]).columns:
    df[col] = encoder.fit_transform(df[col])

# Features and target
X = df.drop("heart_attack", axis=1)
y = df["heart_attack"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Data Shape")
print(X_train.shape)

print("\nTesting Data Shape")
print(X_test.shape)

# Create Logistic Regression Model
model = LogisticRegression(
    max_iter=2000
)

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("\n==============================")
print("MODEL EVALUATION RESULTS")
print("==============================")

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# Confusion Matrix
cm = confusion_matrix(y_test, predictions)

print("\nConfusion Matrix")
print(cm)

# Classification Report
print("\nClassification Report")
print(classification_report(y_test, predictions))

# Sample Predictions
print("\nSample Predictions")
print("Actual:", y_test.iloc[:10].values)
print("Predicted:", predictions[:10])
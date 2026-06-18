import pandas as pd

df = pd.read_csv("Dataset/heart_attack_prediction_indonesia.csv")

print("Dataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nMissing Values")
print(df.isnull().sum())

print("\nHeart Attack Distribution")
print(df["heart_attack"].value_counts())
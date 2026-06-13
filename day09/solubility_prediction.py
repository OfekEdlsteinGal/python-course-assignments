import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    root_mean_squared_error
)
import joblib

# Load data
df = pd.read_csv("delaney-processed.csv")

# Features
X = df[
    [
        "Minimum Degree",
        "Molecular Weight",
        "Number of H-Bond Donors",
        "Number of Rings",
        "Number of Rotatable Bonds",
        "Polar Surface Area"
    ]
]

# Target
y = df["measured log solubility in mols per litre"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Metrics
r2 = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
rmse = root_mean_squared_error(y_test, predictions)

print(f"R²: {r2:.3f}")
print(f"MAE: {mae:.3f}")
print(f"RMSE: {rmse:.3f}")

# Save predictions
results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": predictions
})

results.to_csv(
    "solubility_predictions.csv",
    index=False
)

# Plot
plt.figure(figsize=(8,6))
plt.scatter(y_test, predictions)
plt.xlabel("Actual Solubility")
plt.ylabel("Predicted Solubility")
plt.title("Actual vs Predicted Solubility")
plt.tight_layout()

plt.savefig("solubility_plot.png")

# Save model
joblib.dump(
    model,
    "solubility_model.pkl"
)

print("\nModel Performance")
print("-" * 30)
print(f"R² Score: {r2:.3f}")
print(f"MAE: {mae:.3f}")
print(f"RMSE: {rmse:.3f}")

print("\nFirst 10 Predictions:")
print(results.head(10))

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

print("\nFeature Importance:")
print(feature_importance.sort_values(
    by="Importance",
    ascending=False
))
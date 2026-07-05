import json
from pathlib import Path

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_ROOT / "data" / "processed" / "clean_survey_data.csv"


def train_model():

    df = pd.read_csv(DATA_PATH)

    target = "satisfaction_category"

    remove_columns = [
        "employee_id",
        "open_comment",
        "clean_comment",
        "overall_satisfaction",
        target
    ]

    X = df.drop(columns=remove_columns)

    X = pd.get_dummies(
        X,
        columns=["department", "role"],
        drop_first=True
    )

    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight="balanced"
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    f1 = f1_score(
        y_test,
        predictions,
        average="weighted"
    )

    print("\nAccuracy :", round(accuracy, 4))
    print("Weighted F1 :", round(f1, 4))

    print("\nClassification Report\n")
    print(classification_report(y_test, predictions))

    print("\nConfusion Matrix\n")
    print(confusion_matrix(y_test, predictions))

    metrics = {
        "accuracy": float(accuracy),
        "f1_score": float(f1)
    }

    with open(PROJECT_ROOT / "evaluation_metrics.json", "w") as file:
        json.dump(metrics, file, indent=4)

    importance = {}

    for feature, score in zip(
        X.columns,
        model.feature_importances_
    ):
        importance[feature] = float(score)

    importance = dict(
        sorted(
            importance.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )

    with open(PROJECT_ROOT / "feature_importance.json", "w") as file:
        json.dump(importance, file, indent=4)

    joblib.dump(
        model,
        PROJECT_ROOT / "satisfaction_model.pkl"
    )

    print("\nModel Saved Successfully")
    print("evaluation_metrics.json created")
    print("feature_importance.json created")
    print("satisfaction_model.pkl created")


if __name__ == "__main__":
    train_model()
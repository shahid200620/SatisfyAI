import os
import pandas as pd


def clean_and_merge_data():

    demographics = pd.read_csv("data/raw/demographics.csv")

    survey = pd.read_csv("data/raw/survey_responses.csv")

    df = pd.merge(
        demographics,
        survey,
        on="employee_id",
        how="inner"
    )

    numeric_columns = [
        "q_work_life_balance",
        "q_manager_effectiveness",
        "q_career_growth"
    ]

    for column in numeric_columns:

        median_value = df[column].median()

        df[column] = df[column].fillna(median_value)

    df["open_comment"] = df["open_comment"].fillna("")

    df["composite_engagement_score"] = (
        df[
            [
                "q_work_life_balance",
                "q_manager_effectiveness",
                "q_career_growth"
            ]
        ].mean(axis=1)
    ).round(2)

    os.makedirs(
        "data/processed",
        exist_ok=True
    )

    output_path = "data/processed/clean_survey_data.csv"

    df.to_csv(
        output_path,
        index=False
    )

    print("Cleaning completed successfully.")
    print(f"Rows : {len(df)}")
    print(f"Columns : {len(df.columns)}")
    print(f"Saved : {output_path}")


if __name__ == "__main__":
    clean_and_merge_data()
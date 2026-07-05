import os
import random
import numpy as np
import pandas as pd


def generate_survey_data(num_employees=1000):

    random.seed(42)
    np.random.seed(42)

    employee_ids = []

    for i in range(1, num_employees + 1):
        employee_ids.append(f"EMP{str(i).zfill(4)}")

    departments = [
        "Engineering",
        "Sales",
        "Marketing",
        "Finance",
        "HR"
    ]

    roles = [
        "Individual Contributor",
        "Manager",
        "Director"
    ]

    department = np.random.choice(
        departments,
        size=num_employees,
        p=[0.40, 0.25, 0.15, 0.10, 0.10]
    )

    role = np.random.choice(
        roles,
        size=num_employees,
        p=[0.75, 0.20, 0.05]
    )

    tenure = np.random.normal(
        4,
        3,
        num_employees
    )

    tenure = np.clip(tenure, 0.5, 20)
    tenure = np.round(tenure, 1)

    demographics = pd.DataFrame({
        "employee_id": employee_ids,
        "department": department,
        "role": role,
        "tenure_years": tenure
    })

    work_life = np.random.normal(3.5, 1, num_employees)
    manager = np.random.normal(3.8, 1, num_employees)
    growth = np.random.normal(3.2, 1.2, num_employees)

    work_life = np.clip(work_life, 1, 5).round()
    manager = np.clip(manager, 1, 5).round()
    growth = np.clip(growth, 1, 5).round()

    engineering_mask = demographics["department"] == "Engineering"

    work_life[engineering_mask] = np.random.normal(
        2.5,
        1,
        engineering_mask.sum()
    ).clip(1, 5).round()

    satisfaction = (
        work_life * 0.4 +
        manager * 0.4 +
        growth * 0.2
    )

    satisfaction += np.random.normal(
        0,
        0.5,
        num_employees
    )

    satisfaction = satisfaction.clip(1, 5).round()

    satisfaction_category = pd.cut(
        satisfaction,
        bins=[0, 2.5, 3.5, 5],
        labels=[
            "Low",
            "Medium",
            "High"
        ]
    )

    comments = []

    positive = [
        "Great place to work",
        "Love my team",
        "Excellent culture",
        "Supportive manager",
        "Happy with benefits"
    ]

    neutral = [
        "Average experience",
        "Could be better",
        "Work is okay",
        "Nothing special",
        "Normal workplace"
    ]

    negative = [
        "Too much workload",
        "Poor management",
        "No work life balance",
        "Low career growth",
        "Need better leadership"
    ]

    for value in satisfaction_category:

        if value == "High":
            comments.append(random.choice(positive))

        elif value == "Medium":
            comments.append(random.choice(neutral))

        else:
            comments.append(random.choice(negative))

    survey = pd.DataFrame({

        "employee_id": employee_ids,

        "q_work_life_balance": work_life,

        "q_manager_effectiveness": manager,

        "q_career_growth": growth,

        "overall_satisfaction": satisfaction,

        "satisfaction_category": satisfaction_category,

        "open_comment": comments

    })

    for column in [
        "q_work_life_balance",
        "q_manager_effectiveness"
    ]:

        missing = np.random.rand(num_employees) < 0.05

        survey.loc[missing, column] = np.nan

    return demographics, survey


def save_files():

    os.makedirs("data/raw", exist_ok=True)

    demographics, survey = generate_survey_data()

    demographics.to_csv(
        "data/raw/demographics.csv",
        index=False
    )

    survey.to_csv(
        "data/raw/survey_responses.csv",
        index=False
    )

    print("Data generated successfully.")


if __name__ == "__main__":
    save_files()
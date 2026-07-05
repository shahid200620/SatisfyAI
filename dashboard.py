from pathlib import Path
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Employee Satisfaction Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp{
    background-color:#F5F7FB;
}

section[data-testid="stSidebar"]{
    background:#183153;
    color:white;
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

.main-title{
    font-size:42px;
    font-weight:700;
    color:#183153;
    margin-bottom:0px;
}

.subtitle{
    font-size:18px;
    color:#6b7280;
    margin-top:-10px;
    margin-bottom:30px;
}

.metric-card{

    background:white;

    padding:20px;

    border-radius:15px;

    border:1px solid #E5E7EB;

    box-shadow:0 8px 18px rgba(0,0,0,.08);

    transition:.3s;

}

.metric-card:hover{

    transform:translateY(-4px);

}

.footer{

    text-align:center;

    color:#808080;

    margin-top:40px;

    font-size:14px;

}
/* ---------- MAIN APP TEXT ---------- */

.stApp,
.stApp p,
.stApp span,
.stApp div,
.stApp label,
.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4,
.stApp h5,
.stApp h6,
.stMarkdown,
.stText,
.element-container,
[data-testid="stMarkdownContainer"],
[data-testid="stMetricLabel"],
[data-testid="stMetricValue"],
[data-testid="stMetricDelta"],
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    color: #111827 !important;
}

/* ---------- Tabs ---------- */

button[data-baseweb="tab"] {
    color: #111827 !important;
    font-weight: 600;
}

/* ---------- Inputs ---------- */

.stSelectbox label,
.stNumberInput label,
.stTextInput label,
.stSlider label,
.stCheckbox label,
.stRadio label,
.stMultiSelect label {
    color: #111827 !important;
    font-weight: 600;
}

/* ---------- Dataframe ---------- */

table {
    color: #111827 !important;
}

thead tr th {
    color: #111827 !important;
    font-weight: 700 !important;
}

tbody tr td {
    color: #111827 !important;
}

/* ---------- Expander ---------- */

.streamlit-expanderHeader {
    color: #111827 !important;
}

/* ---------- Info/Success/Warning ---------- */

.stAlert {
    color: #111827 !important;
}

/* ---------- Sidebar (keep white text) ---------- */

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* ---------- Buttons ---------- */

.stButton button {
    color: white !important;
    background: #183153 !important;
    border: none;
}

.stButton button:hover {
    background: #24466f !important;
}

/* ---------- Metric Cards ---------- */

.metric-card h2,
.metric-card h3,
.metric-card h4,
.metric-card p,
.metric-card span {
    color: #111827 !important;
}

</style>
""",unsafe_allow_html=True)

PROJECT = Path(__file__).resolve().parent

df = pd.read_csv(PROJECT/"data"/"processed"/"clean_survey_data.csv")

st.sidebar.markdown("# 🏢 HR Analytics")

st.sidebar.markdown("---")

st.sidebar.markdown("## Navigation")

page = st.sidebar.radio(

    "",

    [

        "🏠 Overview",

        "📊 Analytics",

        "🤖 ML Insights",

        "📂 Data Explorer"

    ]

)

st.sidebar.markdown("---")

st.sidebar.markdown("## Filters")

department = st.sidebar.selectbox(

    "Department",

    ["All"] + sorted(df.department.unique())

)

role = st.sidebar.selectbox(

    "Role",

    ["All"] + sorted(df.role.unique())

)

category = st.sidebar.selectbox(

    "Satisfaction",

    ["All"] + sorted(df.satisfaction_category.unique())

)

filtered = df.copy()

if department != "All":
    filtered = filtered[filtered.department==department]

if role != "All":
    filtered = filtered[filtered.role==role]

if category != "All":
    filtered = filtered[filtered.satisfaction_category==category]

st.markdown('<div class="main-title">📊 Employee Satisfaction Analytics</div>',unsafe_allow_html=True)

st.markdown('<div class="subtitle">Human Resources Intelligence Platform</div>',unsafe_allow_html=True)

st.info("Welcome! This dashboard presents employee engagement insights, sentiment analysis, and machine learning results based on the survey dataset.")

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.markdown(f"""

<div class="metric-card">

<h4>👥 Employees</h4>

<h2>{len(filtered)}</h2>

</div>

""",unsafe_allow_html=True)

with c2:

    st.markdown(f"""

<div class="metric-card">

<h4>⭐ Satisfaction</h4>

<h2>{filtered["overall_satisfaction"].mean():.2f}</h2>

</div>

""",unsafe_allow_html=True)

with c3:

    st.markdown(f"""

<div class="metric-card">

<h4>😊 Sentiment</h4>

<h2>{filtered["sentiment_score"].mean():.2f}</h2>

</div>

""",unsafe_allow_html=True)

with c4:

    st.markdown(f"""

<div class="metric-card">

<h4>📅 Avg Tenure</h4>

<h2>{filtered["tenure_years"].mean():.1f} yrs</h2>

</div>

""",unsafe_allow_html=True)

st.markdown("---")

import plotly.express as px
import plotly.graph_objects as go

tab1, tab2, tab3, tab4 = st.tabs(

    [

        "🏠 Executive Overview",

        "📊 Department Analytics",

        "🤖 Machine Learning",

        "📂 Data Explorer"

    ]

)

with tab1:

    left,right = st.columns((2,1))

    with left:

        st.subheader("Employee Satisfaction by Department")

        dept = (

            filtered

            .groupby("department")["overall_satisfaction"]

            .mean()

            .reset_index()

        )

        fig = px.bar(

            dept,

            x="department",

            y="overall_satisfaction",

            color="overall_satisfaction",

            text_auto=".2f",

            color_continuous_scale="Blues"

        )

        fig.update_layout(

            plot_bgcolor="white",

            paper_bgcolor="white",

            height=430,

            title="Average Satisfaction Score"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    with right:

        st.subheader("Employee Distribution")

        pie = px.pie(

            filtered,

            names="department",

            hole=.60,

            color_discrete_sequence=px.colors.sequential.Blues_r

        )

        pie.update_layout(

            height=430,

            showlegend=True

        )

        st.plotly_chart(

            pie,

            use_container_width=True

        )

    st.markdown("---")

    c1,c2 = st.columns(2)

    with c1:

        role_chart = (

            filtered

            .groupby("role")["overall_satisfaction"]

            .mean()

            .reset_index()

        )

        fig2 = px.bar(

            role_chart,

            x="role",

            y="overall_satisfaction",

            color="overall_satisfaction",

            text_auto=".2f",

            color_continuous_scale="Tealgrn"

        )

        fig2.update_layout(

            plot_bgcolor="white",

            paper_bgcolor="white",

            height=420,

            title="Average Satisfaction by Role"

        )

        st.plotly_chart(

            fig2,

            use_container_width=True

        )

    with c2:

        category = (

            filtered["satisfaction_category"]

            .value_counts()

            .reset_index()

        )

        category.columns = [

            "Category",

            "Employees"

        ]

        fig3 = px.pie(

            category,

            names="Category",

            values="Employees",

            hole=.65,

            color_discrete_sequence=px.colors.qualitative.Safe

        )

        fig3.update_layout(

            height=420,

            title="Satisfaction Categories"

        )

        st.plotly_chart(

            fig3,

            use_container_width=True

        )

    bottom_left, bottom_right = st.columns((2, 1))

with bottom_left:

    st.subheader("😊 Sentiment vs Satisfaction")

    scatter = px.scatter(

        filtered,

        x="sentiment_score",

        y="overall_satisfaction",

        color="department",

        hover_name="role",

        size="tenure_years",

        size_max=18,

        opacity=0.75,

        color_discrete_sequence=px.colors.qualitative.Bold

    )

    scatter.update_layout(

        height=470,

        plot_bgcolor="white",

        paper_bgcolor="white"

    )

    st.plotly_chart(

        scatter,

        use_container_width=True

    )

with bottom_right:

    st.subheader("Overall Satisfaction")

    average = filtered["overall_satisfaction"].mean()

    gauge = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=average,

            number={

                "font":{

                    "size":40

                }

            },

            gauge={

                "axis":{

                    "range":[1,5]

                },

                "bar":{

                    "color":"#1F77B4"

                },

                "steps":[

                    {

                        "range":[1,2],

                        "color":"#FDE2E4"

                    },

                    {

                        "range":[2,3],

                        "color":"#FFF3BF"

                    },

                    {

                        "range":[3,4],

                        "color":"#D8F3DC"

                    },

                    {

                        "range":[4,5],

                        "color":"#95D5B2"

                    }

                ]

            }

        )

    )

    gauge.update_layout(

        height=320,

        paper_bgcolor="white"

    )

    st.plotly_chart(

        gauge,

        use_container_width=True

    )

    st.markdown("### 💼 Executive Insights")

    highest = dept.sort_values(

        "overall_satisfaction",

        ascending=False

    ).iloc[0]

    lowest = dept.sort_values(

        "overall_satisfaction"

    ).iloc[0]

    st.success(

        f"🏆 Highest Satisfaction\n\n"

        f"**{highest['department']}** "

        f"({highest['overall_satisfaction']:.2f})"

    )

    st.warning(

        f"⚠ Needs Attention\n\n"

        f"**{lowest['department']}** "

        f"({lowest['overall_satisfaction']:.2f})"

    )

    st.info(

        "📌 Recommendation\n\n"

        "Focus HR initiatives on departments "

        "with lower satisfaction and "

        "improve manager effectiveness."

    )
with tab2:

    st.subheader("📊 Department Analytics")

    row1, row2 = st.columns(2)

    with row1:

        heat = (

            filtered.groupby(["department", "role"])["overall_satisfaction"]

            .mean()

            .reset_index()

            .pivot(

                index="department",

                columns="role",

                values="overall_satisfaction"

            )

        )

        heatmap = px.imshow(

            heat,

            text_auto=".2f",

            color_continuous_scale="Blues",

            aspect="auto"

        )

        heatmap.update_layout(

            title="Department vs Role Satisfaction",

            height=500,

            paper_bgcolor="white",

            plot_bgcolor="white"

        )

        st.plotly_chart(

            heatmap,

            use_container_width=True

        )

    with row2:

        tenure = px.box(

            filtered,

            x="department",

            y="tenure_years",

            color="department"

        )

        tenure.update_layout(

            title="Employee Tenure Distribution",

            height=500,

            showlegend=False,

            paper_bgcolor="white",

            plot_bgcolor="white"

        )

        st.plotly_chart(

            tenure,

            use_container_width=True

        )

    st.markdown("---")

    row3, row4 = st.columns(2)

    with row3:

        trend = (

            filtered.groupby("tenure_years")["overall_satisfaction"]

            .mean()

            .reset_index()

        )

        line = px.line(

            trend,

            x="tenure_years",

            y="overall_satisfaction",

            markers=True

        )

        line.update_layout(

            title="Satisfaction Across Tenure",

            height=430,

            paper_bgcolor="white",

            plot_bgcolor="white"

        )

        st.plotly_chart(

            line,

            use_container_width=True

        )

    with row4:

        sentiment = px.histogram(

            filtered,

            x="sentiment_score",

            nbins=30,

            color="satisfaction_category",

            opacity=0.85,

            barmode="overlay"

        )

        sentiment.update_layout(

            title="Sentiment Distribution",

            height=430,

            paper_bgcolor="white",

            plot_bgcolor="white"

        )

        st.plotly_chart(

            sentiment,

            use_container_width=True

        )

    st.subheader("Department Summary")

    summary = (

        filtered.groupby("department")

        .agg(

            Employees=("department", "count"),

            Avg_Satisfaction=("overall_satisfaction", "mean"),

            Avg_Sentiment=("sentiment_score", "mean"),

            Avg_Tenure=("tenure_years", "mean")

        )

        .reset_index()

    )

    summary["Avg_Satisfaction"] = summary["Avg_Satisfaction"].round(2)

    summary["Avg_Sentiment"] = summary["Avg_Sentiment"].round(2)

    summary["Avg_Tenure"] = summary["Avg_Tenure"].round(1)

    st.dataframe(

        summary,

        use_container_width=True,

        hide_index=True
    )
with tab3:

    st.subheader("🤖 Machine Learning Insights")

    import joblib
    from sklearn.metrics import (
        accuracy_score,
        precision_score,
        recall_score,
        f1_score,
        confusion_matrix
    )

    model_path = PROJECT / "models" / "employee_satisfaction_model.pkl"

    if model_path.exists():

        model = joblib.load(model_path)

        feature_columns = [
            c for c in filtered.columns
            if c not in [
                "overall_satisfaction",
                "satisfaction_category"
            ]
        ]

        ml_df = filtered.copy()

        X = pd.get_dummies(
            ml_df[feature_columns],
            drop_first=True
        )

        try:

            predictions = model.predict(X)

            actual = ml_df["satisfaction_category"]

            if len(predictions) == len(actual):

                m1, m2, m3, m4 = st.columns(4)

                with m1:
                    st.metric(
                        "Accuracy",
                        f"{accuracy_score(actual, predictions):.2%}"
                    )

                with m2:
                    st.metric(
                        "Precision",
                        f"{precision_score(actual, predictions, average='weighted', zero_division=0):.2%}"
                    )

                with m3:
                    st.metric(
                        "Recall",
                        f"{recall_score(actual, predictions, average='weighted', zero_division=0):.2%}"
                    )

                with m4:
                    st.metric(
                        "F1 Score",
                        f"{f1_score(actual, predictions, average='weighted', zero_division=0):.2%}"
                    )

                st.markdown("---")

                left, right = st.columns((3, 2))

                with left:

                    cm = confusion_matrix(actual, predictions)

                    cm_fig = px.imshow(
                        cm,
                        text_auto=True,
                        color_continuous_scale="Blues",
                        labels=dict(
                            x="Predicted",
                            y="Actual",
                            color="Count"
                        )
                    )

                    cm_fig.update_layout(
                        title="Confusion Matrix",
                        height=500,
                        paper_bgcolor="white",
                        plot_bgcolor="white"
                    )

                    st.plotly_chart(
                        cm_fig,
                        use_container_width=True
                    )

                with right:

                    prediction_counts = (
                        pd.Series(predictions)
                        .value_counts()
                        .reset_index()
                    )

                    prediction_counts.columns = [
                        "Category",
                        "Employees"
                    ]

                    pred_fig = px.pie(
                        prediction_counts,
                        names="Category",
                        values="Employees",
                        hole=0.6,
                        color_discrete_sequence=px.colors.qualitative.Set2
                    )

                    pred_fig.update_layout(
                        title="Predicted Satisfaction Distribution",
                        height=500
                    )

                    st.plotly_chart(
                        pred_fig,
                        use_container_width=True
                    )

        except Exception as e:

            st.error(f"Unable to generate ML insights: {e}")

    else:

        st.warning(
            "No trained model found. "
            "Train the model first and place it inside the models folder."
        )
    st.markdown("---")

    st.subheader("🔮 Employee Satisfaction Prediction")

    prediction_df = filtered.copy()

    numeric_columns = prediction_df.select_dtypes(
        include="number"
    ).columns.tolist()

    categorical_columns = prediction_df.select_dtypes(
        include="object"
    ).columns.tolist()

    if "satisfaction_category" in categorical_columns:
        categorical_columns.remove("satisfaction_category")

    if "overall_satisfaction" in numeric_columns:
        numeric_columns.remove("overall_satisfaction")

    with st.form("prediction_form"):

        col1, col2 = st.columns(2)

        user_inputs = {}

        with col1:

            for column in numeric_columns[: len(numeric_columns) // 2]:

                user_inputs[column] = st.number_input(

                    column.replace("_", " ").title(),

                    value=float(prediction_df[column].median())

                )

            for column in categorical_columns[: len(categorical_columns) // 2]:

                user_inputs[column] = st.selectbox(

                    column.replace("_", " ").title(),

                    sorted(prediction_df[column].dropna().unique())

                )

        with col2:

            for column in numeric_columns[len(numeric_columns) // 2:]:

                user_inputs[column] = st.number_input(

                    column.replace("_", " ").title(),

                    value=float(prediction_df[column].median())

                )

            for column in categorical_columns[len(categorical_columns) // 2:]:

                user_inputs[column] = st.selectbox(

                    column.replace("_", " ").title(),

                    sorted(prediction_df[column].dropna().unique())

                )

        predict_button = st.form_submit_button(
            "Predict Satisfaction"
        )

    if predict_button:

        if model_path.exists():

            try:

                input_df = pd.DataFrame([user_inputs])

                input_df = pd.get_dummies(
                    input_df,
                    drop_first=True
                )

                input_df = input_df.reindex(
                    columns=X.columns,
                    fill_value=0
                )

                prediction = model.predict(input_df)[0]

                st.success(
                    f"Predicted Satisfaction Category: **{prediction}**"
                )

                if hasattr(model, "predict_proba"):

                    probabilities = model.predict_proba(input_df)[0]

                    probability_df = pd.DataFrame(
                        {
                            "Category": model.classes_,
                            "Probability": probabilities
                        }
                    )

                    probability_chart = px.bar(
                        probability_df,
                        x="Category",
                        y="Probability",
                        color="Probability",
                        text_auto=".2%",
                        color_continuous_scale="Blues"
                    )

                    probability_chart.update_layout(
                        height=420,
                        paper_bgcolor="white",
                        plot_bgcolor="white",
                        title="Prediction Confidence"
                    )

                    st.plotly_chart(
                        probability_chart,
                        use_container_width=True
                    )

            except Exception as e:

                st.error(
                    f"Prediction failed: {e}"
                )
with tab4:

    st.subheader("📂 Data Explorer")

    st.write(
        "Explore the processed employee satisfaction dataset used for analysis."
    )

    exp1, exp2, exp3, exp4 = st.columns(4)

    with exp1:
        st.metric(
            "Rows",
            filtered.shape[0]
        )

    with exp2:
        st.metric(
            "Columns",
            filtered.shape[1]
        )

    with exp3:
        st.metric(
            "Missing Values",
            int(filtered.isna().sum().sum())
        )

    with exp4:
        st.metric(
            "Duplicate Rows",
            int(filtered.duplicated().sum())
        )

    st.markdown("---")

    st.subheader("Dataset Preview")

    st.dataframe(
        filtered,
        use_container_width=True,
        height=450
    )

    st.markdown("---")

    st.subheader("Column Information")

    info = pd.DataFrame(
        {
            "Column": filtered.columns,
            "Data Type": filtered.dtypes.astype(str).values,
            "Missing Values": filtered.isnull().sum().values,
            "Unique Values": filtered.nunique().values
        }
    )

    st.dataframe(
        info,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("Descriptive Statistics")

    st.dataframe(
        filtered.describe(include="all").transpose(),
        use_container_width=True
    )

    st.markdown("---")

    csv = filtered.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Filtered Dataset",
        data=csv,
        file_name="filtered_employee_satisfaction.csv",
        mime="text/csv"
    )
st.markdown("---")

st.markdown(
    """
    <div class="footer">
        Employee Satisfaction Analytics Dashboard<br>
        Built with ❤️ using Streamlit, Plotly, Pandas, and Scikit-learn
    </div>
    """,
    unsafe_allow_html=True
)

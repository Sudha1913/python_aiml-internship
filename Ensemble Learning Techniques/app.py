import streamlit as st
import pandas as pd
import joblib

# =========================================
# LOAD SAVED MODEL
# =========================================

model = joblib.load(
    "random_forest_model.pkl"
)

# =========================================
# TITLE
# =========================================

st.title("Netflix Type Prediction")

st.write(
    "Ensemble Learning Project using Random Forest"
)

# =========================================
# USER INPUTS
# =========================================

release_year = st.number_input(
    "Release Year",
    min_value=1900,
    max_value=2025,
    value=2020
)

rating = st.selectbox(
    "Rating",
    [
        "TV-MA",
        "TV-14",
        "TV-PG",
        "R",
        "PG-13",
        "PG"
    ]
)

country = st.selectbox(
    "Country",
    [
        "India",
        "United States",
        "United Kingdom",
        "Canada"
    ]
)

# =========================================
# MANUAL ENCODING
# =========================================

rating_dict = {
    "PG": 0,
    "PG-13": 1,
    "R": 2,
    "TV-14": 3,
    "TV-MA": 4,
    "TV-PG": 5
}

country_dict = {
    "Canada": 0,
    "India": 1,
    "United Kingdom": 2,
    "United States": 3
}

rating = rating_dict[rating]

country = country_dict[country]

# =========================================
# PREDICTION BUTTON
# =========================================

if st.button("Predict"):

    input_data = pd.DataFrame([[
        release_year,
        rating,
        country
    ]],
    columns=[
        "release_year",
        "rating",
        "country"
    ])

    prediction = model.predict(input_data)[0]

    # 0 = Movie
    # 1 = TV Show

    if prediction == 0:
        st.success("Predicted Type: Movie")

    else:
        st.success("Predicted Type: TV Show")
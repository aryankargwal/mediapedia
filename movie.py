# imports
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import streamlit as st

st.title("Movie Recommender")

# Sidebar Menu
st.sidebar.image("assets/logo.png")
st.sidebar.markdown(
    "MediaPedia is our attempt to make an interactive and user friendly media recommender web application with added utilities and features."
)
st.sidebar.markdown("Check out the code at:")
st.sidebar.markdown("[Github Repository](!https://github.com/aryankargwal/mediapedia)")


# Data loading and feature engineering
df = pd.read_csv("data/dataset.csv")
features = ["keywords", "cast", "genres", "director"]


def combine_features(row):
    return (
        row["keywords"]
        + " "
        + row["cast"]
        + " "
        + row["genres"]
        + " "
        + row["director"]
    )


for feature in features:
    df[feature] = df[feature].fillna("")


df["combined_features"] = df.apply(combine_features, axis=1)

cv = CountVectorizer()

count_matrix = cv.fit_transform(df["combined_features"])
cosine_sim = cosine_similarity(count_matrix)


def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]


def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]


movie_user_likes = st.text_input("What movie do you like? ", "Life of Pi")

movie_index = get_index_from_title(movie_user_likes)

similar_movies = list(enumerate(cosine_sim[movie_index]))

sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]


# function to show the final movies
def movie():
    i = int(0)
    st.write("Movies Similar to " + movie_user_likes + " are:\n")
    for element in sorted_similar_movies:
        if i < 5:
            st.write(get_title_from_index(element[0]))
            i = i + 1


movie()

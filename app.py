import streamlit as st
import pandas as pd
import numpy as np
from security import (
    make_hashes,
    check_hashes,
    create_usertable,
    add_userdata,
    view_all_users,
    login_user,
)

# Sidebar Menu
st.sidebar.image("assets/logo.png")
st.sidebar.markdown(
    "MediaPedia is our attempt to make an interactive and user friendly media recommender web application with added utilities and features."
)
st.sidebar.markdown("Check out the code at:")
st.sidebar.markdown("[Github Repository](!https://github.com/aryankargwal/mediapedia)")


# Landing page
def landing():
    st.header("MediaPedia")
    st.image("assets/confused.jpg")
    st.subheader(
        "With the rise of MultiMedia due to advancement in the ease of content creation, through CGI, grammar checkers and predictive text, for us the average media consumer looking for a perfect movie or a TV Series or a Book is a very hard job. We plan to tackle this very prompt utilizing modern ML techniques like NLP and NLTK and deploying it on the Internet in form of a web-app."
    )
    st.subheader("Let us start!")
    menu = ["Login", "SignUp"]
    login = st.sidebar.selectbox("Menu", menu)

    if login == "Home":
        st.subheader("Home")

    elif login == "Login":
        st.sidebar.subheader("Login Section")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type="password")
        if st.sidebar.button("Login"):
            # if password == '12345':
            create_usertable()
            hashed_pswd = make_hashes(password)
            result = login_user(username, check_hashes(password, hashed_pswd))
            if result:

                st.sidebar.success("Logged In as {}".format(username))

            else:
                st.sidebar.warning("Incorrect Username/Password")

    elif login == "SignUp":
        st.sidebar.subheader("Create New Account")
        new_user = st.sidebar.text_input("Username")
        new_password = st.sidebar.text_input("Password", type="password")

        if st.sidebar.button("Signup"):
            create_usertable()
            add_userdata(new_user, make_hashes(new_password))
            st.sidebar.success("You have successfully created a valid Account")
            st.sidebar.info("Go to Login Menu to login")


if __name__ == "__main__":
    landing()

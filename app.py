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

with open("style.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Sidebar Menu
menu = ["Welcome", "OTT Recommendation", "Book Recommnedation"]
st.sidebar.image("assets/logo1.png")
st.sidebar.markdown(
    "MediaPedia is our attempt to make an interactive and user friendly media recommender web application with added utilities and features."
)
st.sidebar.markdown("Check out the code at:")
st.sidebar.markdown("[Github Repository](!https://github.com/aryankargwal/mediapedia)")
option = st.sidebar.selectbox("Menu", menu)

# Landing page
if option == "Welcome":
    st.header("MediaPedia")
    st.image("assets/confused.jpg")
    st.subheader(
        "With the rise of MultiMedia due to advancement in the ease of content creation, through CGI, grammar checkers and predictive text, for us the average media consumer looking for a perfect movie or a TV Series or a Book is a very hard job. We plan to tackle this very prompt utilizing modern ML techniques like NLP and NLTK and deploying it on the Internet in form of a web-app."
    )
    st.subheader("Let us start!")
    menu = ["Login", "SignUp"]
    login = st.selectbox("Menu", menu)

    if login == "Home":
        st.subheader("Home")

    elif login == "Login":
        st.subheader("Login Section")

        username = st.text_input("User Name")
        password = st.text_input("Password", type="password")
        if st.checkbox("Login"):
            # if password == '12345':
            create_usertable()
            hashed_pswd = make_hashes(password)
            result = login_user(username, check_hashes(password, hashed_pswd))
            if result:

                st.success("Logged In as {}".format(username))

                task = st.selectbox("Task", ["Add Post", "Analytics", "Profiles"])
                if task == "Add Post":
                    st.subheader("Add Your Post")

                elif task == "Analytics":
                    st.subheader("Analytics")
                elif task == "Profiles":
                    st.subheader("User Profiles")
                    user_result = view_all_users()
                    clean_db = pd.DataFrame(
                        user_result, columns=["Username", "Password"]
                    )
                    st.dataframe(clean_db)
            else:
                st.warning("Incorrect Username/Password")

    elif login == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type="password")

        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user, make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")

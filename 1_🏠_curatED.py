import streamlit as st
from streamlit_extras.colored_header import colored_header
from custom_functions import *

display_banner()
display_logo()

colored_header(
    label="Welcome to CURATED 😎",
    description="",
    color_name="blue-70",
)

st.info("**An open source project that focuses on curating awesome resources for learning awesome skills.**")
st.text("\n")

goto_page("I want to get started with Python 🐍", "Python 101")
goto_page("I want to understand the WHYs and WHATs of Machine Learning 🦾", "Machine Learning 101")
goto_page("I want to get started with the concepts in Machine Learning 🤖", "Machine Learning 102")

st.image("https://media.tenor.com/P2cQctPfjpAAAAAC/im-working-on-it-progress.gif")

footer()
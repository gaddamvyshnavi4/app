import base64
import streamlit as st





page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://wallpaperaccess.com/full/3543885.jpg");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}



[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
import streamlit as st
import time

# Set Streamlit app to wide mode
#st.set_page_config(layout="wide")

# Define custom CSS for green text and radiant outline
custom_css = """
<style>
    .green-text {
        color: Blue;
        background: linear-gradient(45deg, #ffcc00, #00ccff);
        border: 6px solid transparent;
        border-image: linear-gradient(45deg, #ffcc00, #00ccff);
        border-image-slice: 1;
        padding: 10px;
        border-radius: 10px;
        font-size: 24px;
    }
    body {
        background-image: url('https://th.bing.com/th/id/R.1249395f3897c1adfb15d39308432554?rik=Nx%2bbj24w4rN%2fHA&riu=http%3a%2f%2fupload.wikimedia.org%2fwikipedia%2fcommons%2f8%2f8e%2fBarley_crop_-blue_sky-4May2008.jpg&ehk=8uvqS22E9G%2ftpdGYBfAKwTxqtHieaJ4xS7Vfz30wHYg%3d&risl=1&pid=ImgRaw&r=0');
        background-size: cover;
    }
</style>
"""

# Display the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Display the green text with radiant outline
st.markdown("<p class='green-text'><b>Welcome to the Crop Yield Prediction App!</p>", unsafe_allow_html=True)



selected=option_menu(
    menu_title=None,
    options=["Home ","English","తెలుగు"],
    icons=["house","alphabet-uppercase",""],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)


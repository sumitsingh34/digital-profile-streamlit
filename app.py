import streamlit as st
import pandas as pd
import numpy as np
import requests
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(page_title="Sumit Digital Profile", page_icon=":tada:", layout="wide") # default layout is center

# for icon https://www.webfx.com/tools/emoji-cheat-sheet/

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Asset urls
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_sumit = Image.open("images/1628351101010.jfif")


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


# ----- Header Section: Start ------
with st.container():
    st.subheader("Hi, I am Sumit :wave:")
    st.title("A Data Engineer from United States")
    st.write("I am data science enthusiastic and have proven experties in Big Data Analysis & Development")
    st.write("[LinkedIn Profile](https://www.linkedin.com/in/sumit-singh03/)")

# ----- Header Section: End ------

# ----- WHAT I DO: Start ------
with st.container():
    st.write("---")
    left_col, right_col = st.columns(2)
    with left_col:
        st.header("What I do")
        st.write("##")
        st.write(
            """
                I am IT Professional.
                - Use Data Science and Data Analysis to perform meaningful and impactful analyses.
                - Evaluate business needs and objectives.
                - Access Data and information with APIs/KPIs.
                - Imporve Data Qality and Efficiency.
            """
        )

    with right_col:
         st_lottie(lottie_coding, height=300, key="coding")

# ----- WHAT I DO: End ------

# ----- Experiances: Start ------
with st.container():
    st.write("---")
    left_col, right_col = st.columns((2,1))
    with left_col:
        st.header("Full-Time Employment")
        st.write("##")
        st.subheader("Tata Consultancy Services")
        st.write(
            """
                Data Engineer
                - Two years
            """
        )
        st.image(img_sumit, width=200)

    with right_col:
         st.header("Part-Time Experiance")
         st.write("##")
         st.subheader("Indiana State University")
         st.write(
             """
                Graduate Research Assistant
                - 6 months
             """
         )



# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/susumit8478@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

import streamlit as st
import os
import requests
from PIL import Image
from io import BytesIO

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    return score


st.title("💖 Love Calculator 💖")


image_url = "https://play-lh.googleusercontent.com/3dFUhJhYiIYFvp3fKW2imYWVOn2silI0LCC0urhUm2BQC_JnzuAs0RKk6djS72oUrhk"  
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

image = image.resize((400, int(image.height * 400 / image.width)))

st.image(image, caption="Love is in the air!", use_column_width=False)

st.write("Find out your love compatibility!")

name1 = st.text_input("Enter the first name:")
name2 = st.text_input("Enter the second name:")

if st.button("Calculate Love Score"):
    if name1 and name2:
        score = calculate_love_score(name1, name2)
        st.success(f"Your love score is {score}!")
    else:
        st.error("Please enter both names to calculate the score.")

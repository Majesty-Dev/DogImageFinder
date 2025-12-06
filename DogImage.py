import requests
import json
import streamlit as st

def get_image():
    result = requests.get('https://dog.ceo/api/breeds/image/random')
    image_url = json.loads(result.content.decode())['message']
    img = requests.get(image_url).content

    filename = "dog-image.jpg"
    with open(filename, "wb") as f:
        f.write(img)

    return img


_,headingCentre,_=st.columns(3)
_,buttonCentre,_=st.columns(3)
_,imageAlign,_=st.columns(3)

with headingCentre:
    st.write("### **Dog Image Finder**")

with buttonCentre:
    if st.button("Get New Image"):
        st.image(get_image())
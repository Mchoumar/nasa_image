import streamlit as st
from api import get_api
from PIL import Image

# Get the api content
content = get_api()

# opens the pic
image = Image.open('image.jpg')

# set up the website
st.title(content["title"])
st.image(image, caption=content['copyright'], width=700)
st.write(content["explanation"])

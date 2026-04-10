import google.generativeai as genai
import streamlit as st
from PIL import Image 
genai.configure(api_key="AIzaSyAPKmOY6cpx_pV5Cwl0Cm-7K-2kihH5C-Y")
model=genai.GenerativeModel("gemini-2.5-flash")
st.title("Q&A Chatbot")

a=st.file_uploader("Upload an image",type=["jpg","jpeg","png"])
prompt=st.text_input("Your are a interoior designer, you have to give the best design for the room according to the image and the question in easy to read format.")
if st.button('submit'):
    img=Image.open(a)
    response=model.generate_content([img,prompt])
    st.write(response.text)
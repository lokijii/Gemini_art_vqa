from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import pathlib
import textwrap3
from PIL import Image
import google.generativeai as genai

def to_markdown(text):
  text = text.replace('•', '  *')
  return (textwrap3.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key="")


def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(question)
    return response.text

def get_gemini_response_image(input,image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

with st.sidebar:
    st.header("Text as input")
    text_input_prompt =st.text_input("Enter the prompt: ",key="input")
    st.markdown("<h1 style='text-align: center;'>(or)</h1>", unsafe_allow_html=True)
    img_input_prompt =st.text_input("Enter the prompt: ",key="input1")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image="" 
    submit=st.button("Generate response")


if submit:
    if text_input_prompt:
        response=get_gemini_response(text_input_prompt)
        st.subheader("Generated response:")
        st.write(response)
    elif uploaded_file:
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image.", use_column_width=True)
        st.subheader("Generated response:")
        response=get_gemini_response_image(img_input_prompt,image)
        st.write(response)

import streamlit as st
from PIL import Image
import io

from prompt_builder import build_prompt
from image_generator import generate_image

st.set_page_config(page_title="AI Child Generator")

st.title("👶 AI Child Prediction Generator")

st.write("Upload parent images (for context) + choose settings")

father = st.file_uploader("Upload Father's Photo", type=["jpg", "png", "jpeg"])
mother = st.file_uploader("Upload Mother's Photo", type=["jpg", "png", "jpeg"])

gender = st.selectbox("Child Gender", ["Boy", "Girl"])
age = st.slider("Child Age", 0, 18, 5)

if st.button("Generate Child Image"):

    if father and mother:

        st.info("Generating AI image... please wait")

        prompt = build_prompt(gender, age)

        try:
            image_bytes = generate_image(prompt)

            image = Image.open(io.BytesIO(image_bytes))

            st.image(image, caption="Generated Child")

            st.success("Done!")

        except Exception as e:
            st.error(f"Image generation failed: {str(e)}")

    else:
        st.warning("Please upload both parent images")
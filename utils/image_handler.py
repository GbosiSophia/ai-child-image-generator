from PIL import Image

def load_image(uploaded_file):
    image = Image.open(uploaded_file)
    return image
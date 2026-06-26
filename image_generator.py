import requests
import urllib.parse

def generate_image(prompt):
    encoded_prompt = urllib.parse.quote(prompt)

    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Image generation failed")

    return response.content
from PIL import Image
import requests
from io import BytesIO


response = requests.get("https://www.gstatic.com/android/keyboard/emojikitchen/20210521/u1fa84/u1fa84_u1f917.png")
img = Image.open(BytesIO(response.content))
img = img.convert('RGBA')
img.thumbnail((50, 50))
img.save("test.png")
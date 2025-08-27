from django.test import TestCase

# Create your tests here.
from PIL import Image

img = Image.open("exemplo.jpg")  # substitua pelo nome da sua imagem
img.show()
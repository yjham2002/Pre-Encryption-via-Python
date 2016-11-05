import os
import random
from PIL import Image, ImageDraw, ImageFont
from tempfile import NamedTemporaryFile

PWD = os.getcwd()
SEP = os.path.sep
FONT_FILE = SEP.join([PWD, "arial.ttf"])
FONT_SIZE = 40
POOL = '1234567890'
POOL2 = '-+'
LENGTH = 1
WIDTH = 50
HEIGHT = 50

def generate_captcha(PATH = PWD):
    R = random.randint(0, 100)
    G = random.randint(0, 100)
    B = random.randint(0, 100)
    with NamedTemporaryFile(suffix='.jpg', dir=PATH, delete=False) as fp:
         im = Image.new("RGB", (WIDTH, HEIGHT), (R, G, B))
         draw = ImageDraw.Draw(im)
         font = ImageFont.truetype(FONT_FILE, FONT_SIZE, encoding='utf-8')
         value = ''.join(random.sample(POOL2, LENGTH)+random.sample(POOL, LENGTH))
         draw.text((5, 1), value, font=font)
         draw.ellipse([random.randint(0, WIDTH/2), random.randint(0, HEIGHT/2), random.randint(0, WIDTH), random.randint(0, HEIGHT)], (R, B, G))
         im.save(fp.name)
    return fp.name, value


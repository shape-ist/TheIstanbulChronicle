from os import remove
from sys import maxsize
import PIL, base64, time, re, io, requests
from PIL import Image, ImageOps
from sys import displayhook, maxsize
from flask import request
from setup import storage


def update_pfp(uid):
    image = Image.open(io.BytesIO(request.files['pfpinput'].read()))

    width, height = image.size

    if width >= 200 and height >= 200:
        if width < height:
            resize_size = (200, maxsize)
            resized = PIL.ImageOps.contain(image, resize_size)
            width, height = resized.size
            top = (height - 200) / 2
            cropped = resized.crop((0, top, 200, top + 200))
        if width > height:
            resize_size = (maxsize, 200)
            resized = PIL.ImageOps.contain(image, resize_size)
            width, height = resized.size
            left = (width - 200) / 2
            cropped = resized.crop((left, 0, left + 200, 200))
        if width == height:
            resize_size = (200, 200)
            cropped = PIL.ImageOps.contain(image, resize_size)

    cropped.save(uid + ".png", "PNG")
    storage.child("profilepics/" + uid + ".png").put("temp.png")
    remove(uid + ".png")

    url = storage.child("profilepics/" + uid + ".png").get_url()

    Image.open(requests.get(url, stream=True).raw)

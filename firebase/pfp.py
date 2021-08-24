import os, PIL, base64, time, re, io
from PIL import Image, ImageOps
from sys import displayhook, maxsize
from flask import request
from firebase.setup import db, auth, storage

def update(uid):
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
    os.remove(uid + ".png")
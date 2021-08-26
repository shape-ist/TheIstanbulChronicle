from os import remove
from sys import maxsize

import PIL
import io
import requests
from PIL import Image
from flask import request

from firebase.setup import db
from firebase.setup import storage


def update_pfp(uid, img_size=200):
    # image = Image.open(io.BytesIO(request.files['pfpinput'].read()))
    image = Image.open('C:\\Users\\binan\\Downloads\\uwu.png')

    width, height = image.size

    if width >= img_size and height >= img_size:
        if width < height:
            resize_size = (img_size, maxsize)
            resized = PIL.ImageOps.contain(image, resize_size)
            width, height = resized.size
            top = (height - img_size) / 2
            cropped = resized.crop((0, top, img_size, top + img_size))
        if width > height:
            resize_size = (maxsize, img_size)
            resized = PIL.ImageOps.contain(image, resize_size)
            width, height = resized.size
            left = (width - img_size) / 2
            cropped = resized.crop((left, 0, left + img_size, img_size))
        if width == height:
            resize_size = (img_size, img_size)
            cropped = PIL.ImageOps.contain(image, resize_size)

    cropped.save(uid + ".png", "PNG")
    storage.child("pps/" + uid + ".png").put(uid + ".png")
    remove(uid + ".png")

    url = storage.child("pps/" + uid + ".png").get_url()
    db.collection(u'users').document(uid).update({u'pfp': url})

    return url

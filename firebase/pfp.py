from os import remove, mkdir
from os.path import exists
from sys import maxsize

import PIL
import io
import requests
from PIL import Image
from flask import request

from firebase.setup import db
from firebase.setup import storage

from PIL import ImageOps


def update_pfp(uid, target_size=400, target_filetype='webp'):
    # image = Image.open(io.BytesIO(request.files['pfpinput'].read()))
    image = Image.open('test.jpeg').convert('RGB')

    width, height = image.size

    if width < height:
        resize_size = (target_size, maxsize)
        resized = ImageOps.contain(image, resize_size)
        width, height = resized.size
        top = (height - target_size) / 2
        cropped_image = resized.crop((0, top, target_size, top + target_size))
    if width > height:
        resize_size = (maxsize, target_size)
        resized = ImageOps.contain(image, resize_size)
        width, height = resized.size
        left = (width - target_size) / 2
        cropped_image = resized.crop(
            (left, 0, left + target_size, target_size))
    if width == height:
        resize_size = (target_size, target_size)
        cropped_image = ImageOps.contain(image, resize_size)

    if not exists('pfp_temp'):
        mkdir('pfp_temp')

    cropped_image.save(f'./pfp_temp/{uid}.{target_filetype}',
                       target_filetype.upper())
    storage.child(f'pfps/{uid}.{target_filetype}').put(
        f'./pfp_temp/{uid}.{target_filetype}')
    remove(f'./pfp_temp/{uid}.{target_filetype}')

    print(f'./pfp_temp/{uid}.{target_filetype}')
    print(f'./pfp_temp/{uid}.{target_filetype}')
    print(f'./pfp_temp/{uid}.{target_filetype}')
    print(f'./pfp_temp/{uid}.{target_filetype}')
    print(f'./pfp_temp/{uid}.{target_filetype}')
    print(f'./pfp_temp/{uid}.{target_filetype}')
    print(f'./pfp_temp/{uid}.{target_filetype}')

    # get_url method requires one positional argument for some reason, we don't know why
    url = storage.child(f'pfps/{uid}.{target_filetype}').get_url(None)
    db.collection(u'users').document(uid).update({u'pfp': url})

    return url


def get_default():
    from random import randint
    return storage.child(f'default.webp').get_url(None)

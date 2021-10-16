from firebase.setup import auth, db, storage, firestore
from firebase.article import upload_article
from firebase import schema
import os


def update_pfp(uid, target_size=600, target_filetype='webp', coll=u'users'):
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
                       target_filetype.upper(),
                       optimize=True,
                       quality=95)
    storage.child(f'pfps/{uid}.{target_filetype}').put(
        f'./pfp_temp/{uid}.{target_filetype}')
    remove(f'./pfp_temp/{uid}.{target_filetype}')

    # get_url method requires one positional argument for some reason, we don't know why
    url = storage.child(f'pfps/{uid}.{target_filetype}').get_url(None)
    db.collection(coll).document(uid).update({u'pfp': url})

    return url


import urllib.request as r

r.urlopen(
    "https://upload.wikimedia.org/wikipedia/commons/b/b6/Image_created_with_a_mobile_phone.png",
    b"./allah.png")


def main():
    for filename in os.listdir('./article'):
        print(filename)


if __name__ == '__main__':
    main()
""" upload_article(
    schema.article(
        title='some title',
        body='some text',
        cover_image=
        'https://example.com/example.png'  # will be implemented later, this needs to be uploaded to the server as a file before article object is sent to database 
    )) """
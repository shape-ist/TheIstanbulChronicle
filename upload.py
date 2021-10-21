from firebase.setup import auth, db, storage, firestore
import urllib.request
from PIL import Image, ImageOps
import uuid
from os import mkdir, path, listdir
from shutil import rmtree, copyfile
from firebase.article import upload_article
from firebase import schema
from firebase import user
from firebase import tools as fbtools
from sys import maxsize


def upload_img(img_path,
               uid,
               target_size=600,
               target_filetype='webp',
               coll=u'articles'):
    image = Image.open(img_path).convert('RGB')

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

    if not path.isdir('img_temp'):
        mkdir('img_temp')

    cropped_image.save(f'./img_temp/{uid}.{target_filetype}',
                       target_filetype.upper(),
                       optimize=True,
                       quality=95)
    storage.child(f'article_covers/{uid}.{target_filetype}').put(
        f'./img_temp/{uid}.{target_filetype}')

    # get_url method requires one positional argument for some reason, we don't know why
    url = storage.child(f'article_covers/{uid}.{target_filetype}').get_url(
        None)
    db.collection(coll).document(uid).update({u'cover_image': url})

    return url


def init_article_upload():
    if path.isdir('./temp'):
        rmtree('./temp')

    mkdir('./temp/')


def read_remove_first_line(filename):
    with open(filename, 'r') as f_in:
        first_line = f_in.readline()
    with open(filename, 'r+') as f:  # open file in read / write mode
        firstLine = f.readline()  # read the first line and throw it out
        data = f.read()  # read the rest
        f.seek(0)  # set the cursor to the top of the file
        f.write(data)  # write the data back
        f.truncate()  # set the file size to the current size
        return firstLine
    return first_line


def init_articles(a):
    for index, i in enumerate(a):
        current_uid = upload_article(schema.article())
        data_path = f'./temp/{current_uid}/DATA'
        article_source_path = f'./article/{a[index]}'
        cover_path = f"./temp/{current_uid}/img.webp"

        mkdir(f'./temp/{current_uid}')
        copyfile(article_source_path, data_path)

        img_url = read_remove_first_line(data_path)
        title_str = read_remove_first_line(data_path)

        urllib.request.urlretrieve(img_url, cover_path)

        with open(data_path) as f:
            lines = f.readlines()

        fbtools.update_fields('articles', current_uid, {
            'title': title_str,
            'body': '\\n\\n'.join(lines)
        })

        permalink = upload_img(cover_path, current_uid)


def cleanup():
    if path.isdir('./temp'):
        rmtree('./temp')
    if path.isdir('./img_temp'):
        rmtree('./img_temp')


def main():
    user.login("dmeoeom@gdgd.com", "passssword")
    init_article_upload()
    init_articles(listdir('./article'))
    cleanup()


if __name__ == '__main__':
    main()
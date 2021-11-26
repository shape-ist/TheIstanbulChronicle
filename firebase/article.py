from firebase.setup import db
from firebase import schema
import urllib.request

def upload_article(content):
    from firebase import tools as fbtools
    article_ref = db.collection(u'articles').document()
    article_ref.set(content)
    uid = article_ref.id
    fbtools.update_fields('articles', uid, {'uid': uid})
    return uid


def writer_upload(t, b, c):
    article_content = schema.article(
        title=t,
        body=b,
        cover_image={
            's': c.strip(),
            'm': c.strip(),
            'l': c.strip(),
        }
        # TODO: RESIZE THESE IMAGES TO CORRESPONDING RESOLUTIONS
    )
    upload_article(article_content)


def delete_article(id):
    db.collection(u'articles').document(id).delete()

def saveImage(url, path):
    urllib.request.urlretrieve(url, path)
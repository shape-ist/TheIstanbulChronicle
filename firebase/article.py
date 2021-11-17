from firebase.setup import db
from firebase import schema


def upload_article(content):
    from firebase import tools as fbtools
    article_ref = db.collection(u'articles').document()
    article_ref.set(content)
    uid = article_ref.id
    fbtools.update_fields('articles', uid, {'uid': uid})
    return uid


def writer_upload(t, b):
    article_content = schema.article(title=t, body=b)
    upload_article(article_content)


def delete_article(id):
    db.collection(u'articles').document(id).delete()

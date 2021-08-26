from firebase.setup import db
from firebase.schema import article


def upload_article(content):
    db.collection(u'articles').document().set(content)


def delete_article(id):
    db.collection(u'articles').document(id).delete()


"""use it like so:

upload_article(
    article(
        db,
        writer_uid = 'kqsAAv8QQNN37m2kETro7GbsnNB3',
        title = 'Nirvana sued!!',
        body = 'text text text',
        article_type = 'article'
))"""
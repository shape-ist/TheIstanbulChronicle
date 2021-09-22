from firebase.setup import db


def upload_article(content):
    from firebase import tools as fbtools
    article_ref = db.collection(u'articles').document()
    article_ref.set(content)
    uid = article_ref.id
    fbtools.update_fields('articles', uid, {'uid': uid})
    return uid


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

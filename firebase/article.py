from firebase.setup import db

def upload_article(content):
    from firebase.schema import article
    db.collection(u'articles').document().set(content)
    
    
    
    
    
    
"""


use it like so:

upload_article(
    article(
        db,
        writer_uid = 'kqsAAv8QQNN37m2kETro7GbsnNB3',
        title = 'Nirvana sued!!',
        body = 'text text text',
        article_type = 'article'
))


"""
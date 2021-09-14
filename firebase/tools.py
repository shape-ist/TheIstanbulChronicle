from firebase.setup import db


def get_doc(coll, uid):
    return db.collection(coll).document(uid).get().to_dict()


def connected(host='http://neverssl.com'):
    import urllib.request
    try:
        urllib.request.urlopen(host)
        return True
    except: return False
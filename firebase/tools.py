from firebase.setup import db


def get_doc(coll: str, uid: str):
    return db.collection(coll).document(uid).get().to_dict()


def isauthorized(level: str, uid: str):
    return level in list(get_doc(u'users', uid)['elevation'])


def update_fields(coll: str, uid: str, fields: dict):
    db.collection(coll).document(uid).set(fields, merge=True)

from firebase.setup import db


def get_doc(coll, uid):
    return db.collection(coll).document(uid).get().to_dict()
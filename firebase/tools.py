from firebase.setup import db


def get_doc(coll: str, uid: str):
    return db.collection(coll).document(uid).get().to_dict()


def isauthorized(level: str, uid: str):
    return level in list(get_doc(u'users', uid)['elevation'])


def update_fields(coll: str, uid: str, fields: dict):
    db.collection(coll).document(uid).set(fields, merge=True)


def document_unpack(data):
    data, dictkeys = obj['data'], set()
    for dk in dictkeys:
        for pagi_item in data:
            for currentkey, value in pagi_item.items():
                if currentkey == dk:
                    pagi_item[dk] = pagi_item[dk].get().to_dict()
    return data
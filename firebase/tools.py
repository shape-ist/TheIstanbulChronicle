from firebase.setup import db


def get_doc(coll: str, uid: str):
    return db.collection(coll).document(uid).get().to_dict()


def isauthorized(level: str, uid: str):
    return level in list(get_doc(u'users', uid)['elevation'])


def update_fields(coll: str, uid: str, fields: dict):
    db.collection(coll).document(uid).set(fields, merge=True)

def serialize(obj, classkey=None):
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = todict(v, classkey)
        return data
    elif hasattr(obj, "_ast"):
        return todict(obj._ast())
    elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [todict(v, classkey) for v in obj]
    elif hasattr(obj, "__dict__"):
        data = dict([(key, todict(value, classkey)) 
            for key, value in obj.__dict__.items() 
            if not callable(value) and not key.startswith('_')])
        if classkey is not None and hasattr(obj, "__class__"):
            data[classkey] = obj.__class__.__name__
        return data
    else:
        return obj
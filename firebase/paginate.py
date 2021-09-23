from firebase.setup import db


def paginate(coll: str,
             sort: str, **kwargs):
    out = []
    limit = int(kwargs.get('limit', 10))
    order = kwargs.get('order', 'ASC')
    last_uid = kwargs.get('last_uid', None)
    query = db.collection(coll).order_by(sort).limit(limit)
    if last_uid is not None:
        query = query.start_after(db.collection(coll).document(last_uid).get())
    pagi_stream = query.stream()
    for i in pagi_stream:
        out.append(i.to_dict())
    if order.upper() == 'DESC': out = out[::-1]
    return {'data': out}
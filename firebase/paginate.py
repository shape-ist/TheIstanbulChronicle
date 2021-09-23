from firebase.setup import db, firestore


def paginate(coll: str, sort: str, **kwargs):
    limit, order, last_uid = int(kwargs.get('l', 10)), kwargs.get(
        'o', 'ASC'), kwargs.get('i', None)
    order_obj = firestore.Query.DESCENDING if order.upper(
    ) == 'DESC' else firestore.Query.ASCENDING
    query = db.collection(coll).order_by(sort,
                                         direction=order_obj).limit(limit)
    if last_uid is not None:
        query = query.start_after(db.collection(coll).document(last_uid).get())
    pagi_stream = query.stream()
    out = [i.to_dict() for i in pagi_stream]
    for article in out:
        article['writer'] = article['writer'].get().to_dict()
    return {'data': out, 'last_uid': str(out[-1]['uid'])}

from firebase.setup import db


def paginate(coll: str,
             sort: str,
             limit: int = 10,
             order: str = 'ASC',
             last_uid: str = ''):
    from collections import defaultdict
    out: list = []
    query = db.collection(coll).order_by(sort).limit(limit)
    if last_uid != '':
        query = query.start_after(db.collection(coll).document(last_uid).get())
    pagi_stream = query.stream()
    for i in pagi_stream:
        out.append(i.to_dict())
    if order.upper() == 'DESC': out = out[::-1]
    for article in out:
        article['writer'] = article['writer'].get().to_dict()
    return dict(zip([a['uid'] for a in out], out))
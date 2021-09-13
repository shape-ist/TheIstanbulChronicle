from firebase.setup import db


def paginate(coll: str, sort: str, limit: int, order: str):
    out: list = []
    query = (
        db.collection(coll)
            .order_by(sort)
            .limit(limit)
    )
    pagi_stream = query.stream()
    for i in pagi_stream:
        out.append(i.to_dict())
    if order == 'desc':
        return out[::-1]
    return out

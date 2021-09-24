from firebase import tools as fbtools
from firebase.setup import db, firestore


def paginate(coll: str, sort: str, **kwargs):
    try:
        limit, order, last_uid = int(kwargs.get('l', 10)), kwargs.get(
            'o', 'ASC'), kwargs.get('i', None)
        if order.upper() not in ['ASC', 'DESC']:
            raise Exception("invalid order: use 'ASC' or 'DESC'")
        if limit > 100:
            raise Exception(
                'Max limit reached, cannot query more than 100 documents using the pagination API'
            )
        order_obj = firestore.Query.DESCENDING if order.upper(
        ) == 'DESC' else firestore.Query.ASCENDING
        query = db.collection(coll).order_by(sort,
                                             direction=order_obj).limit(limit)
        if last_uid is not None:
            query = query.start_after(
                db.collection(coll).document(last_uid).get())
        pagi_stream = query.stream()
        out = [i.to_dict() for i in pagi_stream]
        obj = {'data': out, 'last_uid': str(out[-1]['uid'])}
        data, dictkeys = obj['data'], set()
        for item in data:
            item['local_sort'] = data.index(item)
            for key, value in item.items():
                if isinstance(value, firestore.DocumentReference):
                    dictkeys.add(key)
        for dk in dictkeys:
            for pagi_item in data:
                for currentkey, value in pagi_item.items():
                    if currentkey == dk:
                        pagi_item[dk] = pagi_item[dk].get().to_dict()
        return obj
    except Exception as e:
        return {'data': {'error': str(e)}}

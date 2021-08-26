from typing import List


def user(email: str = '',
         bio: str = '',
         uid: int = 0,
         name: str = '',
         pfp: str = '',
         elevation: List[str] = [],
         ban: bool = False):
    return {
        u'email': email,
        u'bio': bio,
        u'uid': uid,
        u'name': name,
        u'pfp': pfp,
        u'elevation': elevation,
        u'ban': ban,
    }


def article(
        db,
        title: str = '',
        body: str = '',
        writer_uid: str = '',
        tag: str = '',
        article_type: str = ''
):
    return {
        u'title': title,
        u'body': body,
        u'writer_uid': db.collection(u'users').document(writer_uid),
        u'article_type': article_type
        # u'tag': tag,
        # ^^ TODO: UNCOMMENT THIS WHEN TAGS ARE IMPLEMENTED
    }


"""
    The schema module will be used like so:

    import schema
    schema.user(
        name = 'Emir Öven',
        uid = 72358260,
        elevation = ['W', 'E', 'A']
    )

    or in context:
    
    db.collection(u'users').document(uid).set(schema.user(
        name=display_name,
        email=email,
        uid=uid
    ))

    which will return an object.
    Empty paramteres will be set to default with their respective types.

    Note that these functions are strongly typed:
    Every parameter must be the specified type, wrong types raise a TypeError, this is important for security purposes.

"""

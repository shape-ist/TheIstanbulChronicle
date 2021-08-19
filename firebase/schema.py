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
    title: str = '',
    body: str = '',  # TODO: implement markdown here
    writer: str = '',
    #  ^^ reference uid here
    # use firestore reference object here if possible
    tag: str = '',
    # ^^ same here, use reference object here
):
    return {
        u'title': title,
        u'body': body,
        u'writer': writer,
        u'tag': tag,
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

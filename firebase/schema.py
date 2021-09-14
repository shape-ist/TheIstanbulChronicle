from typing import List

from firebase.setup import db


def user(email: str = '',
         bio: str = '',
         uid: int = 0,
         name: str = '',
         pfp: str = '',
         elevation: List[str] = [],
         ban: bool = False,
         location: str = '',
         phone: str = '',
         email_public: bool = False):
    return {
        u'email': email,
        u'bio': bio,
        u'uid': uid,
        u'name': name,
        u'pfp': pfp,
        u'elevation': elevation,
        u'ban': ban,
        u'location': location,
        u'phone': phone,
        u'email_public': email_public
    }


def article(db=db,
            title: str = '',
            body: str = '',
            writer_uid: str = '',
            article_type: str = '',
            is_approved: bool = False):
    return {
        u'title': title,
        u'body': body,
        u'writer_uid': db.collection(u'users').document(writer_uid),
        u'article_type': article_type,
        u'is_approved': is_approved
        # TODO: implement tags here ^^^^
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

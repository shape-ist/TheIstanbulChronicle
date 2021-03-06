from typing import List

from firebase.setup import db, auth
from firebase import user as fbuser

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


def article(title: str = '',
            body: str = '',
            tag: str = '',
            article_type: str = '',
            cover_image: dict = {
                's': '',
                'm': '',
                'l': ''
            },
            is_approved: bool = False):
    from time import time
    cover_image_s, cover_image_m, cover_image_l = cover_image[
        's'], cover_image['m'], cover_image['l']
    return {
        u'title': title,
        u'body': body,
        u'writer':
        db.collection(u'users').document(fbuser.current_uid()),
        u'article_type': article_type,
        u'is_approved': False,
        u'timestamp': time(),
        u'cover_image_s': cover_image_s,
        u'cover_image_m': cover_image_m,
        u'cover_image_l': cover_image_l,
        u'is_approved': is_approved,
        u'tag': tag
    }

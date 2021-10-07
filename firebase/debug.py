from firebase import article
from firebase import schema
from firebase import user


def debug_user():
    try:
        try:
            return user.login(f"debug@debug.com", "debug1234")
        except:
            return user.register(f"debug@debug.com", "debug1234", "ada lovelace")
    except:
        raise Exception('debug user auth. failed.')


def test_articles():
    for i in range(50):
        article.upload_article(schema.article(
            title=f'{i + 1}- Article title',
            body='Lorem ipsum dolor sit amet constrectur adispiscing elit.',
            cover_image='https://udiscoverbrand.co/img/products/84396-goel-tekne-agaclar-daglar-bulutlar-doga-manzara-255fj-odas-ev-duvar-modern-sanat-dekor-ahsap-cerceve-poster.jpg'
        ))

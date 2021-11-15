# searching articles by keyword

from firebase.setup import db


def search_article(keyword: str):
    searched_articles = []
    articles = db.collection(u'articles')

    for article in articles.get():
        content = article.to_dict()["body"]
        if keyword.lower() in content.lower():
            searched_articles.append(article)
    if not articles:
        print("\nno article available\n")
    for index, _ in enumerate(searched_articles):
        searched_articles[index] = searched_articles[index].get(None)
    data = searched_articles
    print(data['writer'])
    data["writer"] = data["writer"].to_dict()
    return {"data": data}

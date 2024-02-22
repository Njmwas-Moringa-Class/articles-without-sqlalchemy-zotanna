from Article import Article

class Author:
    # Class variable to store all authors
    all_authors = []

    def __init__(self, name):
        # Constructor to initialize author attributes
        self.name = name
        self.authored_articles = []
        self.__class__.all_authors.append(self)

    def __str__(self):
        return f"Author: {self.name}"

    @property
    def articles(self):
        return self.authored_articles

    @property
    def magazines(self):
        return list(set(article.magazine for article in self.authored_articles))

    def add_article(self, magazine, title):
        # Method to add a new article authored by the author
        new_article = Article(self, magazine, title)
        self.authored_articles.append(new_article)

    @property
    def topic_areas(self):
        return list(set(article.magazine.category for article in self.authored_articles))
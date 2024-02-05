class Author:
    authors = []

    def __init__(self, name):
        self.author_name = name
        self.articles_written = []
        Author.authors.append(self)

    def name(self):
        return self.author_name

    def articles(self):
        return self.articles_written

    def magazines(self):
        return list(set([article.magazine_name for article in self.articles_written]))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self.articles_written.append(new_article)
        return new_article

    def topic_areas(self):
        return list(set([article.magazine_name.mag_category for article in self.articles_written]))

    def __str__(self):
        return f"Author: {self.author_name}"

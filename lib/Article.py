class Article:
    articles = []

    def __init__(self, author, magazine, title):
        self.author_name = author
        self.magazine_name = magazine
        self.title_mag = title
        self.author_name.articles_written.append(self)
        self.magazine_name.articles_written.append(self)
        Article.articles.append(self)

    def title(self):
        return self.title_mag

    def author(self):
        return self.author_name

    def magazine(self):
        return self.magazine_name

    def all(self):
        return Article.articles

    def __str__(self):
        return f"Author: {self.author_name} Magazine: {self.magazine_name} Title: {self.title_mag}"

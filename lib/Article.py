class Article:
    # Class variable to store all articles
    all_articles = []

    def __init__(self, author, magazine, title):
        # Constructor to initialize article attributes
        self.author = author
        self.magazine = magazine
        self.title = title
        # Add the article to various lists
        self.__class__.all_articles.append(self)
        magazine.published_articles.append(self)
        author.authored_articles.append(self)

    @property
    def article_title(self):
        return self.title

    @property
    def author_name(self):
        return self.author.name

    @property
    def magazine_name(self):
        return self.magazine.name
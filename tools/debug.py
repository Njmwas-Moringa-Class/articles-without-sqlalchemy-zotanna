#!/usr/bin/env python3

import sys
import ipdb

sys.path.append('lib')

from Author import Author
from Article import Article
from Magazine import Magazine

if __name__ == '__main__':
    # WRITE YOUR TEST CODE HERE ###

    # Function to print all authors
    def print_all_authors():
        print("All Authors:")
        for author in Author.authors:
            print(author)

    # Function to print all articles
    def print_all_articles():
        print("All Articles:")
        for article in Article.articles:
            print(article)

    # Function to print all magazines
    def print_all_magazines():
        print("All Magazines:")
        for magazine in Magazine.magazines:
            print(magazine)

    # Function to print information about articles in a specific magazine
    def print_articles_in_magazine(magazine_name):
        print(f"Articles in Magazine '{magazine_name}':")
        for article in Article.articles:
            if article.magazine_name == magazine_name:
                print(article)

    # Function to print articles written by a specific author
    def print_articles_by_author(author_name):
        print(f"Articles by Author '{author_name}':")
        for article in Article.articles:
            if article.author_name == author_name:
                print(article)

    # Function to print articles and their authors
    def print_articles_with_authors():
        print("Articles with Authors:")
        for article in Article.articles:
            author = next((author.author_name for author in Author.authors if author.author_name == article.author_name), None)
            if author:
                print(f"Article: {article.title_mag} | Author: {author}")

    # Function to print articles in a specific magazine along with their authors
    def print_articles_in_magazine_with_authors(magazine_name):
        print(f"Articles in Magazine '{magazine_name}' with Authors:")
        for article in Article.articles:
            if article.magazine_name == magazine_name:
                author = next((author.author_name for author in Author.authors if author.author_name == article.author_name), None)
                if author:
                    print(f"Article: {article.title_mag} | Author: {author}")

    # DO NOT REMOVE THIS
    ipdb.set_trace()

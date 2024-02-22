import logging
from Author import Author
from Magazine import Magazine
from Article import Article

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def add_article():
    try:
        author_name = input("Enter author's name: ")
        magazine_name = input("Enter magazine name: ")
        magazine_category = input("Enter magazine category: ")
        article_title = input("Enter article title: ")

        # Create or find the author
        author = next((author for author in Author.all_authors if author.name == author_name), None)
        if not author:
            author = Author(author_name)

        # Create or find the magazine
        magazine = Magazine.find_by_partial_name(magazine_name)
        if not magazine:
            magazine = Magazine(magazine_name, magazine_category)

        # Check if the article already exists for this author and magazine
        existing_article = next((article for article in magazine.published_articles if article.title == article_title), None)

        if not existing_article:
            author.add_article(magazine, article_title)
            print(f"Article '{article_title}' added to {magazine_name} by {author_name}.")
        else:
            print(f"Article '{article_title}' already exists in {magazine_name}.")

    except Exception as e:
        logger.error(f"Error adding article: {e}")
        print("An error occurred. Please try again.")

def get_magazine_info():
    try:
        magazine_name = input("Enter magazine name: ")
        magazine = Magazine.find_by_name(magazine_name)

        if magazine:
            print(f"Magazine Info:\n{magazine}")
            print(f"Contributors: {[author.name for author in magazine.contributors]}")
            print(f"Article Titles: {magazine.article_titles}")
            
            # Print contributing authors (more than 2 articles)
            contributing_authors = magazine.contributing_authors()
            print(f"Contributing Authors (more than 2 articles): {[author.name for author in contributing_authors]}")
        else:
            print(f"Magazine '{magazine_name}' not found.")

    except Exception as e:
        logger.error(f"Error getting magazine info: {e}")
        print("An error occurred. Please try again.")

def update_magazine_info():
    try:
        article_title = input("Enter article title: ")
        article = next((article for article in Article.all_articles if article.title == article_title), None)

        if article:
            new_magazine_name = input("Enter new magazine name: ")
            new_magazine_category = input("Enter new magazine category: ")

            # Remove the article from the current magazine's published articles list
            article.magazine.published_articles.remove(article)

            # Create or find a new magazine with the updated information
            new_magazine = Magazine.find_by_name(new_magazine_name)
            if not new_magazine:
                new_magazine = Magazine(new_magazine_name, new_magazine_category)

            # Update the article's magazine and add it to the new magazine's published articles list
            article.magazine = new_magazine
            new_magazine.published_articles.append(article)

            print(f"Magazine name updated for '{article_title}' to '{new_magazine_name}' in category '{new_magazine_category}'.")
        else:
            print(f"Article '{article_title}' not found.")

    except Exception as e:
        logger.error(f"Error updating magazine info: {e}")
        print("An error occurred. Please try again.")

def get_articles_by_author():
    try:
        author_name = input("Enter author's name: ")
        author = next((author for author in Author.all_authors if author.name == author_name), None)

        if author:
            for article in author.authored_articles:
                print(f"\nArticles by {author_name}: {article.title} in {article.magazine.name} ({article.magazine.category})")
        else:
            print(f"Author '{author_name}' not found.")

    except Exception as e:
        logger.error(f"Error getting articles by author: {e}")
        print("An error occurred. Please try again.")

def get_authors_by_magazine():
    try:
        magazine_name = input("Enter magazine name: ")
        magazine = Magazine.find_by_partial_name(magazine_name)

        if magazine:
            print(f"\nAuthors who have contributed to {magazine_name}:")
            for author in magazine.contributors:
                print(f"- {author.name}")
        else:
            print(f"Magazine '{magazine_name}' not found.")

    except Exception as e:
        logger.error(f"Error getting authors by magazine: {e}")
        print("An error occurred. Please try again.")

def get_articles_by_magazine():
    try:
        magazine_name = input("Enter magazine name: ")
        magazine = Magazine.find_by_partial_name(magazine_name)

        if magazine:
            print(f"\nArticles in {magazine_name}:")
            for article in magazine.published_articles:
                print(f"- {article.title} by {article.author.name}")
        else:
            print(f"Magazine '{magazine_name}' not found.")

    except Exception as e:
        logger.error(f"Error getting articles by magazine: {e}")
        print("An error occurred. Please try again.")

def main():
    while True:
        print("\nOptions:")
        print("1. Add Article")
        print("2. Get Magazine Info")
        print("3. Update Magazine Info")
        print("4. Get Articles by Author")
        print("5. Get Authors by Magazine")
        print("6. Get Articles by Magazine")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == "1":
            add_article()
            get_magazine_info()
        elif choice == "2":
            get_magazine_info()
        elif choice == "3":
            update_magazine_info()
            get_magazine_info()
        elif choice == "4":
            get_articles_by_author()
        elif choice == "5":
            get_authors_by_magazine()
        elif choice == "6":
            get_articles_by_magazine()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, or 7.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception(f"Unhandled exception: {e}")
        print("An unexpected error occurred. Please check the logs.")
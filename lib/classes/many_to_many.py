class Article:
    articles_list = []

    def __init__(self, author, magazine, title):
        self._title = None
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.articles_list.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if not (5 <= len(new_title) <= 50):
            raise ValueError("Title length must be between 5 and 50 characters")
        self._title = new_title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise TypeError("Author must be an instance of the Author class")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class")
        self._magazine = new_magazine


class Author:
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not new_name:
            raise ValueError("Name can't be empty")
        self._name = new_name

    def articles(self):
        return [article for article in Article.articles_list if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        areas = list({magazine.category for magazine in self.magazines()})
        return areas if areas else None


class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not (2 <= len(new_name) <= 16):
            raise ValueError("Name length must be between 2 and 16 characters")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not new_category:
            raise ValueError("Category can't be empty")
        self._category = new_category

    def articles(self):
        return [article for article in Article.articles_list if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author = article.author
            if author not in author_counts:
                author_counts[author] = 0
            author_counts[author] += 1

        frequent_authors = []
        for author in author_counts:
            if author_counts[author] >= 2:
                frequent_authors.append(author)

        return frequent_authors if frequent_authors else None
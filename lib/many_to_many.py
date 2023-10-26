import ipdb

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [c for c in Contract.all if c.author == self]
    
    def books(self):
        return [c.book for c in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        total = 0
        for c in self.contracts():
            total += c.royalties
        return total


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        return [c.author for c in self.contracts()]

class Contract:
    all = []

    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def book(self):
        return self._book
        
    @book.setter
    def book(self, new_book):
        if isinstance(new_book, Book):
            self._book = new_book
        else:
            raise Exception('Not a book!')
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise Exception('Not an author!')
    
    @property
    def date(self):
        return self._date
        
    @date.setter
    def date(self, new_date):
        if isinstance(new_date, str):
            self._date = new_date
        else:
            raise Exception('Not a string!')
        
    @property
    def royalties(self):
        return self._royalties
        
    @royalties.setter
    def royalties(self, new_royalties):
        if isinstance(new_royalties, int):
            self._royalties = new_royalties
        else:
            raise Exception('Not an int!')

# ipdb.set_trace()
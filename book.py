"""Definition of the Book class."""
# Author(s): Pierre Abraham Mulamba
# Date of creation (modification): 20200224 (20200224)
# Usage: import book
#        create an object book = Book('GA403', 'Big C++', 2009, 8, 0, 0)

from dataclasses import dataclass


@dataclass(init=True, repr=True)
class Book(object):
    """
    Definition of a Book with the following attributes:
    quote
    title
    year
    minimal_age
    n_possess
    n_available.
    """
    nBooks = 0
    __slots__ = ['quote', 'title', 'year', 'minimal_age', 'n_possess', 'n_available']
    quote: str
    title: str
    year: int
    minimal_age: int
    n_possess: int
    n_available: int
    nBooks += 1

    # Accessors methods
    @property
    def get_quote(self) -> str:
        """Returns the quote of a book instance."""
        return self.quote

    @property
    def get_title(self) -> str:
        """Returns the title of a book instance."""
        return self.title

    @property
    def get_year(self) -> int:
        """Returns the year of a book instance."""
        return self.year

    @property
    def get_minimal_age(self) -> int:
        """Returns the minimal age required to read a book instance."""
        return self.minimal_age

    @property
    def get_n_possess(self) -> int:
        """Returns the number of copies of a book possessed."""
        return self.n_possess

    @property
    def get_n_available(self) -> int:
        """Returns the number of books available."""
        return self.n_available

    # Mutators methods
    def set_quote(self, quote):
        """Set the quote of a book."""
        self.quote = quote

    def set_title(self, title):
        """Set the title of a book."""
        self.title = title

    def set_year(self, year):
        """Set the year of a book."""
        self.year = year

    def set_minimal_age(self, minimal_age):
        """Set the minimal age required to read a book."""
        self.minimal_age = minimal_age

    def set_n_possess(self, n_possess):
        """Set the number of copies possess."""
        self.n_possess = n_possess

    def set_n_available(self, n_available):
        """Set the number of copies available."""
        self.n_available = n_available

    def info(self):
        """Print the information about a book."""
        return "{}. {}. {} y.o.".format(self.get_quote, self.get_title, self.get_minimal_age)

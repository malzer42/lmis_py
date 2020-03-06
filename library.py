"""Definition of the Library class."""
# Author(s): Pierre Abraham Mulamba
# Date of creation (modification): 20200224 (20200224)
# Usage: import book
#        create an object book = Book('GA403', 'Big C++', 2009, 8, 0, 0)
# tmp_subscriber = Subscriber('', '', '', 0)

# for subscriber in self.subscribers:
#    if subscriber.get_id_number == id_number:
#        tmp_subscriber = subscriber
#        break
# self.subscribers.remove(tmp_subscriber)
# del tmp_subscriber
# tmp_book = Book('', '', 2020, 0, 0, 0)
# for book in self.books:
#    if book.get_quote == quote_book:
#        tmp_book = book
#        break
# self.books.remove(tmp_book)
# del tmp_book
# for book in self.books:
#    if title in book.get_title:
#        print(book.info())
# for book in self.books:
#    if quote_to_search in book.get_quote:
#        print(book.info())

from dataclasses import dataclass

from book import Book
from subscriber import Subscriber
from borrow import Borrow


@dataclass(init=True, repr=True)
class Library(object):
    """
    Definition to the Library class with the following attributes:
    subscribers: List[Subscriber]
    n_subscribers: int
    books: List[Book]
    n_books: int
    borrowers: List[Borrow]
    n_borrowers: int
    """
    __slots__ = ['subscribers', 'n_subscribers', 'books', 'n_books', 'borrowers', 'n_borrowers']

    subscribers: list
    n_subscribers: int
    books: list
    n_books: int
    borrowers: list
    n_borrowers: int

    def add_subscriber_to_library(self, subscriber_obj):
        """
        Adding a Subscriber object to the library
        subscriber_obj: Subscriber instance.
        """
        try:
            if subscriber_obj not in self.subscribers:
                self.subscribers.append(subscriber_obj)
                self.n_subscribers = len(self.subscribers)
                print("{} added successfully".format(subscriber_obj))
            else:
                print("WARNING {} already exists in the Library".format(subscriber_obj))
        except Exception as exception_add_sub:
            print(exception_add_sub)
            raise
        else:
            print("Total {} subscriber(s) added to the Library".format(len(self.subscribers)))
        finally:
            print("Done")

    def remove_subscriber_from_library(self, id_number):
        """
        Remove a Subscriber based on his id_number
        id_number: str
        """
        try:
            [self.subscribers.remove(sub_obj) for sub_obj in self.subscribers if sub_obj.get_id_number == id_number][0]
            print("{} removed successfully".format(id_number))
            self.n_subscribers = len(self.subscribers)
        except IndexError as index_error:
            print("{} Non existent in the Library - {}".format(id_number, index_error))
        except Exception as exception_rem_sub:
            print("{} Non  existent in the Library - {}".format(id_number, exception_rem_sub))
            raise
        else:
            print("Total {} subscriber(s) in the Library".format(len(self.subscribers)))

        finally:
            print("Done")

    def add_book_to_library(self, book_obj):
        """
        Adding a Book instance to the library
        book_obj: Book instance.
        """
        try:
            if book_obj not in self.books:
                self.books.append(book_obj)
                self.n_books = len(self.books)
                print("{} added successfully".format(book_obj))
            else:
                print("WARNING {} already exists in the Library".format(book_obj))
        except Exception as exception_add_book:
            print(exception_add_book)
            raise
        else:
            print("Total of {} book(s) added to the Library".format(len(self.books)))
        finally:
            print("Done")

    def remove_book_from_library(self, quote_book):
        """
        Remove a book from the library based on the quote of the book
        quote_book: str
        """
        try:
            [self.books.remove(book_obj) for book_obj in self.books if book_obj.get_quote == quote_book][0]
            self.n_books = len(self.books)
            print("{} removed successfully".format(quote_book))
        except Exception as exception_rem_book:
            print("{} is not in the Library - {}".format(quote_book, exception_rem_book))
            raise
        else:
            print("Total {} book(s) in the Library".format(len(self.books)))
        finally:
            print("Done")

    def search_book_title(self, title):
        """
        Search and display all the book with the title containing the text_to_find
        title: str
        """
        try:
            [print(book_obj.info()) for book_obj in self.books if title in book_obj.get_title]
        except Exception as exception_search_title:
            print("{} Not found - {}".format(title, exception_search_title))
            raise
        else:
            print("Title {} found!".format(title))
        finally:
            pass

    def search_book_quote(self, quote_to_search):
        """
        Search and display information about a book based on the quote of the book
        quote_to_search: str
        """
        try:
            for book_obj in self.books:
                if quote_to_search in book_obj.get_quote:
                    print("{} found!".format(book_obj.info()))
                    return
        except Exception as exception_quote:
            print(exception_quote)
            raise
        else:
            pass
        finally:
            pass

    def borrow_book_by_subscriber(self, sub_id_number, book_quote, book_return_date) -> bool:
        """
        The method check if it is possible that the book can be borrowed by the subscriber
        if it is possible, then a new borrow is added to the list of borrowers.
        It is possible to borrow a book by a subscriber if the book is available,
        the subscriber as the minimal required age to read the book,
        the subscriber did not already borrow the book
        the subscriber did not exceed the maximal number (2) of books to borrow.
        :param sub_id_number: str
        :param book_quote: str
        :param book_return_date: date
        :return: bool, True in case of success borrow and False otherwise
        """
        success_or_fail: bool = False
        number_of_books_borrowed_by_subscriber: int = 0
        maximal_number_to_borrow: int = 2

        try:
            # Search a book with the given book_quote in the list of books and assign it to tmp_book
            # Check if the book is available in the list of books.
            book_obj = [book_elt for book_elt in self.books if book_elt.get_quote == book_quote][0]

            if book_obj.get_n_available > 0:
                is_book_available = True
            else:
                print("{} is not available {}".format(book_obj.get_quote, book_obj.get_n_available))
                return success_or_fail

            # Search a subscriber with the given sub_id_number in the list of subscribers and assign him to tmp_subscriber
            sub_obj = [subscriber_elt for subscriber_elt in self.subscribers if subscriber_elt.get_id_number == sub_id_number][0]

            # Check if the given subscriber has borrowed the book in the list of borrowers
            # Count the number of time the subscriber occurs in the borrowers list
            has_subscriber_borrowed_the_book: bool = False
            borrow_obj = Borrow(sub_obj, book_obj, book_return_date)
            if borrow_obj in self.borrowers:
                print("{} - {} exists in the borrowers list".format(borrow_obj.get_book_obj.get_quote, borrow_obj.get_sub_obj.get_id_number))
                return success_or_fail

            for borrow_elt in self.borrowers:
                if borrow_elt.get_sub_obj.get_id_number == sub_id_number:
                    number_of_books_borrowed_by_subscriber = number_of_books_borrowed_by_subscriber + 1
                    if number_of_books_borrowed_by_subscriber >= maximal_number_to_borrow:
                        success_or_fail = False
                        print("Number of books borrowed by subscriber {}".format(number_of_books_borrowed_by_subscriber))
                        print("{} has reached the limit to borrow a book".format(sub_obj.get_id_number))
                        # print("Excess Failure to borrow the book {} by the subscriber {}".format(book_obj, sub_obj))
                        return success_or_fail

                    else:
                        print("!!!! {}. {} - {} !!!!".format(number_of_books_borrowed_by_subscriber, borrow_elt.get_book_obj.get_quote, borrow_elt.get_sub_obj.get_id_number))

            # Check if the subscriber has the required age to read the book,
            # the subscriber did not exceed the maximal number allowed to borrow.
            has_required_age: bool = False
            if sub_obj.get_age >= book_obj.get_minimal_age:
                has_required_age = True
            else:
                print("{} does not have the required age to read the book {}".format(sub_obj.get_id_number, book_obj.get_quote))
                return success_or_fail

            # number_of_books_borrowed_by_subscriber = self.borrowers.count(borrow_obj)

            if number_of_books_borrowed_by_subscriber > maximal_number_to_borrow:
                print("{} has exceed the limit to borrow a book".format(sub_obj.get_id_number))
                return success_or_fail

            if has_required_age and is_book_available and number_of_books_borrowed_by_subscriber < maximal_number_to_borrow and not has_subscriber_borrowed_the_book:
                if borrow_obj not in self.borrowers:
                    self.borrowers.append(borrow_obj)
                    book_obj.set_n_available(book_obj.get_n_available - 1)
                    number_of_books_borrowed_by_subscriber += 1
                    print("{} borrowed by {}".format(book_quote, sub_id_number))
                    success_or_fail = True
                    return success_or_fail
                else:
                    print("Number of books borrowed by subscriber {}".format(number_of_books_borrowed_by_subscriber))
                    print("Failure to borrow the book {} by the subscriber {}".format(book_obj, sub_obj))
                    return success_or_fail

        except Exception as exception__borrow_book:
            print("{} is not in the library -{}".format(book_quote, exception__borrow_book))
            raise
        else:
            print("Total {} borrow(s) from the Library".format(len(self.borrowers)))
        finally:
            print("Done")
            return success_or_fail

    def return_book_by_subscriber(self, sub_id_number, book_quote) -> bool:
        """
        If a subscriber has borrowed a book, the borrow is removed from the borrowers list
        otherwise nothing is done
        :param sub_id_number: str
        :param book_quote: str
        :return: True/False: bool
        """

        is_book_returned_by_subscriber: bool = False

        try:
            sub_obj = [sub_elt for sub_elt in self.subscribers if sub_elt.get_id_number == sub_id_number][0]
            book_obj = [book_elt for book_elt in self.books if book_elt.get_quote == book_quote][0]
            borrow_obj = [borrow_elt for borrow_elt in self.borrowers if borrow_elt.get_sub_obj == sub_obj and borrow_elt.get_book_obj == book_obj][0]
            if borrow_obj in self.borrowers:
                self.borrowers.remove(borrow_obj)
                is_book_returned_by_subscriber = True
                book_obj.set_n_available(book_obj.get_n_available + 1)
                print("Success return of {} by {}".format(book_obj.get_quote, sub_obj.get_id_number))
                return is_book_returned_by_subscriber

        except Exception as exception_return_book:
            print("Failed return of {} by {} - {}".format(book_quote, sub_id_number, exception_return_book))
            raise
        else:
            print("Total {} borrow(s) in the borrowers list".format(len(self.borrowers)))
        finally:
            print("Done")
            return is_book_returned_by_subscriber

    def subscriber_info(self, sub_id_number):
        """
        Print the subscriber last name, first name and borrowed books
        :param sub_id_number: str
        :return:
        """
        try:
            sub_obj = [sub_elt for sub_elt in self.subscribers if sub_elt.get_id_number == sub_id_number][0]
            print("{}".format(sub_obj.info()))
            [print(borrow_obj.info()) for borrow_obj in self.borrowers if borrow_obj.get_sub_obj.get_id_number == sub_id_number]
        except Exception as exception_sub_info:
            print("{} Not found in the Library - {}".format(sub_id_number, exception_sub_info))
            raise
        else:
            pass
        finally:
            print("Done")

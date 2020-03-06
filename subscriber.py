"""Definition of the Subscriber class."""
# Author(s): Pierre Abraham Mulamba
# Date of creation (modification): 20200224 (20200224)
# Usage: import the subscriber
#        create an object sub = Subscriber("102030", "Pierre", "Abraham", 20)

from dataclasses import dataclass


# from borrow import Borrow


@dataclass(init=True, repr=True)
class Subscriber(object):
    """
    Definition of a Subscriber with the following attributes:
    id_number: str
    first_name: str
    last_name: str
    age: int
    borrowers: list[Borrow]
    """
    __slots__ = ['id_number', 'first_name', 'last_name', 'age']
    id_number: str
    first_name: str
    last_name: str
    age: int

    # Accessors methods
    @property
    def get_id_number(self) -> str:
        """Returns the id_number."""
        return self.id_number

    @property
    def get_first_name(self) -> str:
        """Returns the first_name."""
        return self.first_name

    @property
    def get_last_name(self) -> str:
        """Returns the last_name."""
        return self.last_name

    @property
    def get_age(self) -> int:
        """Returns the age."""
        return self.age

    @property
    def get_last_name(self) -> str:
        """
        Get the last name of the subscriber
        :return: last_name
        """
        return self.last_name

    @property
    def get_age(self) -> int:
        """
        Get the age of the subscriber.
        :return: age
        """
        return self.age

    # Mutators methods
    def set_id_number(self, id_number):
        """Set the id_number.
        :param id_number:str
        """
        self.id_number = id_number

    def set_first_name(self, first_name):
        """Set the first name."""
        self.first_name = first_name

    def set_last_name(self, last_name):
        """Set the last name."""
        self.last_name = last_name

    def set_age(self, age):
        """Set the age."""
        self.age = age

    def info(self):
        """Print the information of a subscriber."""
        return "{}, {}. {} y.o. #{}".format(self.get_first_name,
                                            self.get_last_name,
                                            self.get_age,
                                            self.get_id_number)

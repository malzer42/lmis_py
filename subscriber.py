"""A sample class."""


# Autor(s): Pierre Abraham Mulamba
# Date of creation (modification): 20180525(20180525)

class Subscriber(object):
    """docstring for Subscriber."""

    nSubscribers = 0

    def __init__(self, id, fname, lname, age):
        """Ctor."""
        self.id_ = id
        self.fname_ = fname
        self.lname_ = lname
        self.age_ = age
        Subscriber.nSubscribers += 1

    def __repr__(self):
        """Return the representation of an instance of class Subscriber."""
        return f"Subscriber({self.id_}, {self.fname_}, {self.lname_}, {self.age_})"

    def __str__(self):
        """Return the End user representation of Subscriber."""
        return f'{self.fname_}, {self.lname_}. {self.age_} ans. #{self.id_}'

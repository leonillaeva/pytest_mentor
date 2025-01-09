from django.db import models, DataError

from authentication.models import CustomUser
from book.models import Book


class Order(models.Model):
    """
           This class represents an Order. \n
           Attributes:
           -----------
           param book: foreign key Book
           type book: ForeignKey
           param user: foreign key CustomUser
           type user: ForeignKey
           param created_at: Describes the date when the order was created. Can't be changed.
           type created_at: int (timestamp)
           param end_at: Describes the actual return date of the book. (`None` if not returned)
           type end_at: int (timestamp)
           param plated_end_at: Describes the planned return period of the book (2 weeks from the moment of creation).
           type plated_end_at: int (timestamp)
       """
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(default=None, null=True, blank=True)
    plated_end_at = models.DateTimeField(default=None)

    def __str__(self):
        """
        Magic method is redefined to show all information about Book.
        :return: book id, book name, book description, book count, book authors
        """
        if self.end_at == None:
            return f"\'id\': {self.pk}, " \
                   f"\'user\': CustomUser(id={self.user.pk})," \
                   f" \'book\': Book(id={self.book.pk})," \
                   f" \'created_at\': \'{self.created_at}\'," \
                   f" \'end_at\': {self.end_at}," \
                   f" \'plated_end_at\': \'{self.plated_end_at}\'"
        else:
            return f"\'id\': {self.pk}, " \
                   f"\'user\': CustomUser(id={self.user.pk})," \
                   f" \'book\': Book(id={self.book.pk})," \
                   f" \'created_at\': \'{self.created_at}\'," \
                   f" \'end_at\': \'{self.end_at}\'," \
                   f" \'plated_end_at\': \'{self.plated_end_at}\'"

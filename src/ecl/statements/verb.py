"""This module is for defining the Verb object"""


import typing


class Verb:
    """Verb instance with the relative attributes"""

    def __init__(self, database: object, **kwargs: typing.Union[str, list]):
        self.id_ = kwargs.pop("id_")
        self.method = kwargs.pop("method", None)
        self.description = kwargs.pop("description", None)

    def to_dict(self):
        """return a dictionary with the column names as keys"""

        return {
            "verb_id": self.id_,
            "method": self.method,
            "description": self.description,
        }

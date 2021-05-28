"""This module is for defining the Qualia object"""

import typing


class Qualia:
    """Qualia instance with the relative attributes"""

    def __init__(self, database, **kwargs: typing.Union[str, list]):
        self.id_ = kwargs.pop("id_")
        self.qualia = kwargs.pop("qualia", None)
        self.description = kwargs.pop("description", None)
        self.category = kwargs.pop("category", None)
        self.is_negative = kwargs.pop("is_negative", None)
        self.kwargs = kwargs

    def to_dict(self):
        """return a dictionary with the column names as keys"""

        return {
            "qualia_id": self.id_,
            "qualia": self.qualia,
            "description": self.description,
            "category": self.category,
            "is_negative": self.is_negative,
        }

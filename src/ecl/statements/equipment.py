"""This module is for defining the Equipment object"""

import typing


class Equipment:
    """Equipment instance with the relative attributes"""

    def __init__(self, database: object, **kwargs: typing.Union[str, list]):
        self.id_ = kwargs.pop("id_")
        self.item = kwargs.pop("equipment", None)
        self.is_common = kwargs.pop("is_common", None)

    def to_dict(self):
        """return a dictionary with the column names as keys"""

        return {
            "equipment_id": self.id_,
            "equipment": self.item,
            "is_common": self.is_common,
        }

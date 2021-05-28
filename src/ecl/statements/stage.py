"""This module is for defining the Stage object"""

import typing


class Stage:
    """Stage instance with the relative attributes"""

    def __init__(self, database, **kwargs: typing.Union[str, list]):
        self.id_ = kwargs.pop("id_")
        self.stage = kwargs.pop("stage", None)

    def to_dict(self):
        """return a dictionary with the column names as keys"""

        return {"stage_id": self.id_, "stage": self.stage}

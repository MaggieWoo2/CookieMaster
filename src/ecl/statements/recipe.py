"""This module is for defining the Recipe object"""

import typing


class Recipe:
    """Recipe instance with the relative attributes"""

    def __init__(
        self,
        database,
        id_: str,
        name: str,
        stage: str,
        step: str,
        prev: str,
        ingredient: typing.List[str],
        step_id: str,
    ):
        self.id_ = id_
        self.name = name
        self.stage = [database.get_stage(i) for i in stage if i != ""]
        self.step = step
        self.prev = prev
        self.ingredient = [database.get_ingredient(i) for i in ingredient if i != ""]
        self.step_id = [database.get_step(i) for i in step_id if i != ""]

    def to_dict(self):
        """return a dictionary with the column names as keys"""

        return {
            "recipe_id": self.id_,
            "recipe_name": self.name,
            "stage": [i.stage for i in self.stage if i is not None],
            "step": self.step,
            "previous_step": self.prev,
            "ingredients": [i.item for i in self.ingredient if i is not None],
            "step_id": [i.id_ for i in self.step_id if i is not None],
        }

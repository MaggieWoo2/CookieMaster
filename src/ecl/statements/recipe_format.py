"""This module is for defining the RecipeFormat object"""

import typing


class RecipeFormat:
    """RecipeFormat instance with the relative attributes"""

    def __init__(
        self,
        database: object,
        id_: str,
        recipe_name: str,
        stage_name: str,
        input_stage: typing.List[str],
        output: typing.List[str],
        absorbed: str,
    ):
        self.id_ = id_
        self.recipe_name = recipe_name
        self.stage_name = [database.get_stage(i) for i in stage_name if i != ""]
        self.input_stage = [database.get_stage(i) for i in input_stage if i != ""]
        self.output = output
        self.absorbed = absorbed

    def to_dict(self):
        """return a dictionary with the column names as keys"""
        return {
            "recipeFormat_id": self.id_,
            "recipe_name": self.recipe_name,
            "stage_name": [i.stage for i in self.stage_name if i is not None],
            "input_stage": [i.stage for i in self.input_stage if i is not None],
            "output": self.output,
            "absorbed": self.absorbed,
        }

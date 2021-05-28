"""This module is for defining the Substitution object"""

import typing


class Substitution:
    """Substitution instance with the relative attributes"""

    def __init__(
        self,
        database,
        id_: str,
        name: str,
        items_out: typing.List[str],
        items_in: typing.List[str],
        in_out_ratio: typing.List[str],
        steps_out: typing.List[str],
        steps_in: typing.List[str],
        scope: typing.List[str],
        change_qualia_cookie: typing.List[str],
        change_qualia_brownie: typing.List[str],
        change_qualia_pancake: typing.List[str],
        change_qualia_cupcake: typing.List[str],
        steps_impacted: str,
        change_actions: str,
        change_duration: str,
        change_output: str,
        change_complexity: str,
        **kwargs
    ):
        # ift, action_notes, change_step_note, assumption, notes, explanation
        self.id_ = id_
        self.name = name
        self.items_out = [database.get_ingredient(i) for i in items_out if i != "X"]
        self.items_in = [database.get_ingredient(i) for i in items_in if i != "X"]
        self.in_out_ratio = in_out_ratio
        self.steps_out = [database.get_step(i) for i in steps_out if i != "X"]
        self.steps_in = [database.get_step(i) for i in steps_in if i != "X"]
        self.scope = scope
        self.change_qualia_cookie = [database.get_qualia(q) for q in change_qualia_cookie if q != ""]
        self.change_qualia_brownie = [database.get_qualia(q) for q in change_qualia_brownie if q != ""]
        self.change_qualia_pancake = [database.get_qualia(q) for q in change_qualia_pancake if q != ""]
        self.change_qualia_cupcake = [database.get_qualia(q) for q in change_qualia_cupcake if q != ""]
        self.steps_impacted = steps_impacted  # could be better if there is id_
        self.change_actions = change_actions
        self.change_duration = change_duration
        self.change_output = change_output
        self.change_complexity = change_complexity

    def to_dict(self):
        """return a dictionary with the column names as keys"""

        return {
            "substitution_id": self.id_,
            "name": self.name,
            "items_out": [i.item for i in self.items_out if i is not None],
            "items_in": [i.item for i in self.items_in if i is not None],
            "in_out_ratio": self.in_out_ratio,
            "steps_out": [i.id_ for i in self.steps_out if i is not None],
            "steps_in": [i.id_ for i in self.steps_in if i is not None],
            "scope": self.scope,
            "change_qualia_cookie": [i.qualia for i in self.change_qualia_cookie if i is not None],
            "change_qualia_pancake": [i.qualia for i in self.change_qualia_pancake if i is not None],
            "change_qualia_brownie": [i.qualia for i in self.change_qualia_brownie if i is not None],
            "change_qualia_cupcake": [i.qualia for i in self.change_qualia_cupcake if i is not None],
            "steps_impacted": self.steps_impacted,
            "change_actions": self.change_actions,
            "change_duration": self.change_duration,
            "change_output": self.change_output,
            "change_complexity": self.change_complexity,
        }

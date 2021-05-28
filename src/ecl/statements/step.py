"""This module is for defining the Step object"""

import typing


class Step:
    """Step instance with the relative attributes"""

    def __init__(
        self,
        database,
        id_: str,
        stage: str,
        required_items: typing.List[str],
        verb: typing.List[str],
        action_notes: str,
        duration: str,
        output: str,
        complexity: str,
        **kwargs
    ):
        self.id_ = id_
        self.stage = [database.get_stage(i) for i in stage]
        self.required_items = [database.get_ingredient_or_equip(i) for i in required_items if i != ""]
        self.verb = [database.get_verb(i) for i in verb if i != ""]
        self.action_notes = action_notes
        self.duration = duration
        self.output = output
        self.complexity = complexity

    def to_dict(self):
        """return a dictionary with the column names as keys"""

        return {
            "step_id": self.id_,
            "stage": [i.stage for i in self.stage if i is not None],
            "required_items": [i.item for i in self.required_items if i is not None],
            "verb": [i.method for i in self.verb if i is not None],
            "action_notes": self.action_notes,
            "duration": self.duration,
            "output": self.output,
            "complexity": self.complexity,
        }

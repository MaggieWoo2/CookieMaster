"""This module is for defining the Equipment object"""

import typing


class Ingredient:
    """Ingredient instance with the relative attributes"""

    def __init__(
        self,
        database: object,
        id_: str,
        item: str,
        inherit: typing.List[str],
        required_attribute: typing.List[str],
        attribute_default: typing.List[str],  # dict[str,str]
        qualia: typing.List[str],
        notes: str,
    ):

        self.id_ = id_
        self.item = item
        self.inherit = inherit
        self.required_attribute = required_attribute
        self.attribute_default = attribute_default
        self.qualia = [database.get_qualia(q) for q in qualia if q != ""]
        self.notes = notes

    def __str__(self):
        return f"Ingredient {self.item} with tags {self.inherit} and ..."

    def __repr__(self):
        return f"Ingredient {self.item} with tags {self.inherit} and ..."

    def to_dict(self):
        """return a dictionary with the column names as keys"""

        return {
            "ingr_id": self.id_,
            "item": self.item,
            "inherit": self.inherit,
            "required_attribute": self.required_attribute,
            "attribute_default": self.attribute_default,
            "qualia": [i.qualia for i in self.qualia if i is not None],
            "notes": self.notes,
        }

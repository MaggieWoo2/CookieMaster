"""This module is to export the database"""

import pathlib
import typing

import pandas as pd

from ecl.statements.database import Database


def export_database(database: Database, path: typing.Union[str, pathlib.Path]):
    """Export the database as a dataframe"""

    ing_df = pd.DataFrame([i.to_dict() for i in database.ingredient])
    qua_df = pd.DataFrame([i.to_dict() for i in database.qualia])
    stage_df = pd.DataFrame(i.to_dict() for i in database.stage)
    step_df = pd.DataFrame([i.to_dict() for i in database.step])
    recipe_df = pd.DataFrame([i.to_dict() for i in database.recipe])
    verb_df = pd.DataFrame([i.to_dict() for i in database.verb])
    rf_df = pd.DataFrame([i.to_dict() for i in database.recipe_format])
    equip_df = pd.DataFrame([i.to_dict() for i in database.equipment])
    sub_df = pd.DataFrame([i.to_dict() for i in database.substitution])

    for df in [ing_df, qua_df, step_df, recipe_df, verb_df, rf_df, equip_df, sub_df]:
        for col in df.columns:
            df[col] = df[col].apply(
                lambda _: str(_).replace("[", "").replace("]", "").replace("'", "").replace("nan", "")
            )

    with pd.ExcelWriter(path) as writer:
        ing_df.to_excel(writer, sheet_name="Ingredient", index=False)
        sub_df.to_excel(writer, sheet_name="Substitution", index=False)
        step_df.to_excel(writer, sheet_name="Step", index=False)
        recipe_df.to_excel(writer, sheet_name="Recipe", index=False)
        rf_df.to_excel(writer, sheet_name="Recipe_Format", index=False)
        verb_df.to_excel(writer, sheet_name="Verb", index=False)
        qua_df.to_excel(writer, sheet_name="Qualia", index=False)
        equip_df.to_excel(writer, sheet_name="Equipment", index=False)
        stage_df.to_excel(writer, sheet_name="Stage", index=False)

"""This module is to import the spreadsheet as a set of objects"""


import pathlib
import typing

import numpy as np
import pandas as pd

from ecl.statements.database import Database

pd.set_option("display.max_columns", None)


def import_database_qualia(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocessing the qualia spreadsheet and return a dataframe"""

    qualia = df.iloc[:, :4]
    for col in qualia.columns:
        qualia[col] = qualia[col].fillna("")
        qualia[col] = qualia[col].str.lower()
        # qualia[col] = qualia[col].str.split(", ")
        # qualia[col] = qualia[col].map(lambda l: [s.lower() for s in l])

    qualia.columns = ["qualia", "description", "category", "is_negative"]
    qualia["category"] = qualia["category"].str.split(", ")
    qualia["is_negative"] = [True if i == ["y"] else False for i in qualia["is_negative"]]
    qualia.insert(0, "id_", ["q-" + str(i) for i in range(len(qualia))])
    qualia.set_index("id_")
    return qualia


def import_database_ingredients(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocessing the ingredients spreadsheet and return a dataframe"""

    def import_raw_ingredients(df: pd.DataFrame) -> pd.DataFrame:
        df = df.loc[:, "Tag/item name":"Notes"]
        data = df.copy()
        i = df[df["Tag/item name"].isna()].index
        df = df.drop(data.index[i], axis=0)
        df.reset_index()
        j = df[df.isnull().sum(axis=1) > 4].index
        df = df.drop(data.index[j], axis=0)
        df.reset_index()
        # remove NAs, convert into list
        for col in df.columns[1:5]:
            df[col] = df[col].fillna("")
            df[col] = df[col].str.split(", ")
            # df[col] = df[col].str.split('; ')
        df["Tag/item name"] = df["Tag/item name"].map(lambda x: x.lower())
        df["Inherits from"] = df["Inherits from"].map(lambda l: [x.lower() for x in l])
        # Attribute defaults
        # df['Attribute defaults'] = df['Attribute defaults'].str.replace('%', 'percentage')
        df.to_string()
        return df

    def get_ingredient_info_base(ingredients_dataset, ingredient):
        """a function to check the data for a given ingredient, without inheriting from parents
        return inherit_from, attribute_default"""

        for idx, item in enumerate(ingredients_dataset["Tag/item name"]):
            if ingredient == item:
                return (
                    ingredients_dataset.iloc[idx, 1],
                    ingredients_dataset.iloc[idx, 3],
                )

    def get_ingredient_info_all(ingredients_dataset, ingredient):
        """with inheriting from parents, use get_ingredient_info_base()"""

        base_i_f, base_a_d = get_ingredient_info_base(ingredients_dataset, ingredient)
        temp_i_f, temp_a_d = [], []
        # base_i_f.remove('nan')
        if len(base_i_f) > 0:
            for i in base_i_f:
                if i in list(ingredients_dataset["Tag/item name"]):
                    parent_i_f, parent_a_d = get_ingredient_info_base(ingredients_dataset, i)
                    temp_i_f += parent_i_f
                    temp_a_d += parent_a_d

        i_f = list(set(base_i_f + temp_i_f))
        a_d = list(set(base_a_d + temp_a_d))
        if "" in i_f:
            i_f.remove("")
        if "" in a_d:
            a_d.remove("")
        return i_f, a_d

    def update_ingredients(df):
        df["Inherits from"] = [get_ingredient_info_all(df, i)[0] for i in df["Tag/item name"]]
        df["Attribute defaults"] = [get_ingredient_info_all(df, i)[1] for i in df["Tag/item name"]]
        return df

    def attribute_pair(attr_default):
        def pair_up(str_):
            return "ratio=" + str_

        lst = []
        for l in attr_default:
            ls = []
            for attr in l:
                attr = attr.lower()
                if "=" not in attr:
                    ls.append(pair_up(attr))
                else:
                    ls.append(attr)
            lst.append(ls)
        return lst

    ingredients_raw = import_raw_ingredients(df)
    ingredients = update_ingredients(ingredients_raw)  # a dataframe

    ingredients.columns = [
        "item",
        "inherit",
        "required_attribute",
        "attribute_default",
        "qualia",
        "notes",
    ]
    ingredients.attribute_default = attribute_pair(ingredients.attribute_default)
    ingredients.qualia = ingredients.qualia.fillna("X")
    ingredients.insert(0, "id_", ["ingr-" + str(i) for i in range(len(ingredients))])
    ingredients.set_index("id_")
    ingredients["qualia"] = ingredients["qualia"].map(lambda l: [s.lower().strip() for s in l])

    return ingredients


def import_database_substitutions(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocessing the substitutions spreadsheet and return a dataframe"""

    substitutions = df.loc[:, :"Explanation"]
    j = substitutions[substitutions.isnull().sum(axis=1) > 4].index
    substitutions = substitutions.drop(df.index[j], axis=0)
    substitutions.reset_index()
    substitutions.insert(0, "id_", ["subs-" + str(i) for i in range(len(substitutions))])
    substitutions.set_index("id_")
    substitutions = substitutions.replace("X", np.nan)
    substitutions["Items in"] = substitutions["Items in"].str.split(",")
    substitutions["Items out"] = substitutions["Items out"].str.split(",")
    substitutions["Steps out"] = substitutions["Steps out"].str.split(",")
    substitutions["Steps in"] = substitutions["Steps in"].str.split(",")
    for col in [
        "Scope",
        "Δqualia (cookies)",
        "Δqualia (brownies)",
        "Δqualia (pancakes)",
        "Δqualia (cupcakes)",
    ]:
        substitutions[col] = substitutions[col].fillna("")
        substitutions[col] = substitutions[col].str.split(", ")
    substitutions["Steps out"] = substitutions["Steps out"].fillna("").map(lambda l: [s.lower().strip() for s in l])
    substitutions["Steps in"] = substitutions["Steps in"].fillna("").map(lambda l: [s.lower().strip() for s in l])

    substitutions.columns = [
        "id_",
        "ift",
        "name",
        "items_out",
        "items_in",
        "in_out_ratio",
        "steps_out",
        "steps_in",
        "scope",
        "change_qualia_cookie",
        "change_qualia_brownie",
        "change_qualia_pancake",
        "change_qualia_cupcake",
        "steps_impacted",
        "change_actions",
        "action_notes",
        "change_duration",
        "change_output",
        "change_complexity",
        "change_step_note",
        "assumption",
        "notes",
        "explanation",
    ]
    substitutions.scope = substitutions.scope.fillna("x").map(lambda l: [s.lower().strip() for s in l])
    substitutions.items_out = substitutions.items_out.fillna("X").map(lambda l: [s.lower().strip() for s in l])
    substitutions.items_in = substitutions.items_in.fillna("X").map(lambda l: [s.lower().strip() for s in l])
    substitutions.change_qualia_cookie = substitutions.change_qualia_cookie.fillna("X").map(
        lambda l: [s.lower() for s in l]
    )
    substitutions.change_qualia_brownie = substitutions.change_qualia_brownie.fillna("X").map(
        lambda l: [s.lower() for s in l]
    )
    substitutions.change_qualia_pancake = substitutions.change_qualia_pancake.fillna("X").map(
        lambda l: [s.lower() for s in l]
    )
    substitutions.change_qualia_cupcake = substitutions.change_qualia_cupcake.fillna("X").map(
        lambda l: [s.lower() for s in l]
    )

    return substitutions


def import_database_steps(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocessing the steps spreadsheet and return a dataframe"""

    steps = df.loc[:, :"Explanation"]
    # Add ids
    j = steps[steps.isnull().sum(axis=1) > 4].index
    steps = steps.drop(steps.index[j], axis=0)
    steps.reset_index()
    steps.insert(0, "id_", ["step-" + str(i) for i in range(len(steps))])
    steps.set_index("id_")
    steps.id_ = steps.id_.astype(str)

    steps = steps.replace("X", np.nan)
    for col in ["Stage?", "Required items", "Action"]:
        steps[col] = steps[col].fillna("")
        steps[col] = steps[col].str.split(", ")
        steps[col] = steps[col].map(lambda l: [s.lower().strip() for s in l])
    steps["Complexity"] = steps["Complexity"].replace(
        "Depends", 0
    )  # maybe modified later (change Depends to 0 for calculation)
    steps["Complexity"] = steps["Complexity"].replace(np.nan, 0)
    steps.columns = [
        "id_",
        "stage",
        "required_items",
        "verb",
        "action_notes",
        "duration",
        "output",
        "complexity",
        "assumptions",
        "notes",
        "explaination",
    ]
    return steps


def import_database_recipes(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocessing the recipes spreadsheet and return a dataframe"""

    recipes = df.iloc[:, :6]
    j = recipes[recipes.isnull().sum(axis=1) > 4].index
    recipes = recipes.drop(recipes.index[j], axis=0)
    recipes.reset_index()
    # remove NAs, convert into list
    # recipes['Refrence [New] Steps'] = recipes['Refrence [New] Steps'].replace('X', np.nan).fillna('')
    recipes["Refrence [New] Steps"] = recipes["Refrence [New] Steps"].str.replace("Steps", "step")
    for col in recipes.columns[1:6]:
        recipes[col] = recipes[col].replace("X", np.nan)
        recipes[col] = recipes[col].fillna("")
        recipes[col] = recipes[col].str.split(", ")
        recipes[col] = recipes[col].map(lambda l: [s.lower() for s in l])

    recipes.columns = ["name", "stage", "step", "prev", "ingredient", "step_id"]

    indices_lst = list(recipes["name"].unique())
    recipes.insert(0, "id_", ["recp-" + str(indices_lst.index(x)) for x in recipes.name])
    return recipes


def import_database_recipeFormats(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocessing the recipe_formats spreadsheet and return a dataframe"""

    rf = df.iloc[:, :5]
    j = rf[rf.isnull().sum(axis=1) > 4].index
    rf = rf.drop(rf.index[j], axis=0)
    rf.reset_index()
    for col in rf.columns[1:5]:
        rf[col] = rf[col].replace("X", np.nan)
        rf[col] = rf[col].fillna("")
        rf[col] = rf[col].str.split(", ")
        rf[col] = rf[col].map(lambda l: [s.lower().strip() for s in l])

    rf.columns = ["recipe_name", "stage_name", "input_stage", "output", "absorbed"]
    indices_lst = list(rf["recipe_name"].unique())
    rf.insert(0, "id_", ["rf-" + str(indices_lst.index(x)) for x in rf.recipe_name])

    return rf


def import_database_verbs(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocessing the verbs spreadsheet and return a dataframe"""

    verb = df.iloc[:, :2]

    verb.columns = ["method", "description"]
    verb.method = verb.method.map(lambda s: s.lower())
    verb.insert(0, "id_", ["v-" + str(i) for i in range(len(verb))])
    verb.set_index("id_")
    return verb


def import_database_equipments(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocessing the equipments spreadsheet and return a dataframe"""

    equip = df.iloc[:, :2]
    equip.columns = ["equipment", "is_common"]
    equip["is_common"] = [True if i == "Y" else False for i in equip["is_common"]]
    equip.equipment = equip.equipment.map(lambda s: s.lower())
    equip.insert(0, "id_", ["e-" + str(i) for i in range(len(equip))])
    equip.set_index("id_")
    return equip


def import_database_stages(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocessing the stages spreadsheet and return a dataframe"""

    stages = df.iloc[:, :1]
    # stages.Stages = stages.Stages.map(lambda s: s.lower())
    stages.Stages = stages.Stages.str.lower()
    stages.columns = ["stage"]
    stages.insert(0, "id_", ["s-" + str(i) for i in range(len(stages))])
    stages.set_index("id_")
    return stages


def import_database(filepath: typing.Union[str, pathlib.Path], database: Database) -> Database:
    """Import the spreadsheet raw data, preprocessing...
    return a database with each spreadsheet as an object"""

    qualia_df = pd.read_excel(filepath, sheet_name="Qualia")
    ingredients_df = pd.read_excel(filepath, sheet_name="Ingredients")
    substitutions_df = pd.read_excel(filepath, sheet_name="new Substitutions")
    steps_df = pd.read_excel(filepath, sheet_name="new Steps")
    recipes_df = pd.read_excel(filepath, sheet_name="Recipes")
    rf_df = pd.read_excel(filepath, sheet_name="Recipe Formats")
    verb_df = pd.read_excel(filepath, sheet_name="Verbs")
    equip_df = pd.read_excel(filepath, sheet_name="Equipment")
    stage_df = pd.read_excel(filepath, sheet_name="Stages")

    for _, row in import_database_qualia(qualia_df).iterrows():
        database.add_qualia(**row)
    for _, row in import_database_ingredients(ingredients_df).iterrows():
        database.add_ingredient(**row)
    for _, row in import_database_verbs(verb_df).iterrows():
        database.add_verb(**row)
    for _, row in import_database_equipments(equip_df).iterrows():
        database.add_equipment(**row)
    for _, row in import_database_stages(stage_df).iterrows():
        database.add_stage(**row)
    for _, row in import_database_steps(steps_df).iterrows():
        database.add_step(**row)
    for _, row in import_database_recipes(recipes_df).iterrows():
        database.add_recipe(**row)
    for _, row in import_database_recipeFormats(rf_df).iterrows():
        database.add_recipe_format(**row)
    for _, row in import_database_substitutions(substitutions_df).iterrows():
        database.add_substitution(**row)

    return database

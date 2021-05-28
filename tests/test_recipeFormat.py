from ecl.statements.database import Database
from ecl.statements.recipe_format import RecipeFormat


def test_recipeFormat():
    database = Database()

    database.add_stage(id_="s_1", stage="preparation")
    database.add_stage(id_="s_2", stage="measure")
    recipeCat = RecipeFormat(
        database,
        id_="rf_0",
        recipe_name="cookie",
        stage_name=["preparation"],
        input_stage=["measure"],
        output="output",
        absorbed="nothing",
    )

    assert recipeCat.recipe_name == "cookie"
    assert recipeCat.stage_name == [database.get_stage("preparation")]
    assert recipeCat.input_stage == [database.get_stage("measure")]
    assert recipeCat.output == "output"
    assert recipeCat.absorbed == "nothing"

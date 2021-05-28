from ecl.statements.database import Database
from ecl.statements.recipe import Recipe


def test_recipe():
    database = Database()
    database.add_stage(id_="s_1", stage="preparation")
    database.add_ingredient(
        id_="i_0",
        item="anything",
        inherit="parent",
        required_attribute="flavor",
        attribute_default="sweet",
        qualia=["sad"],
        notes="this is a note",
    )
    database.add_step(
        id_="step_0",
        stage=["preparation"],
        required_items=["anything"],
        verb=["mix"],
        action_notes="no action notes",
        duration=0,
        output="well",
        complexity=2,
    )

    recipe = Recipe(
        database,
        id_="r_0",
        name="brownie",
        stage=["preparation"],
        step="step1",
        prev="previous step",
        ingredient=["anything"],
        step_id=["step_0"],
    )
    assert recipe.id_ == "r_0"
    assert recipe.name == "brownie"
    assert recipe.stage == [database.get_stage("preparation")]
    assert recipe.step == "step1"
    assert recipe.prev == "previous step"
    assert recipe.ingredient == [database.get_ingredient("anything")]
    assert recipe.step_id == [database.get_step("step_0")]

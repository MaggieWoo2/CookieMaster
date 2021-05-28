from ecl.statements.database import Database
from ecl.statements.step import Step


def test_step():
    database = Database()
    database.add_ingredient(
        id_="i_0",
        item="anything",
        inherit="parent",
        required_attribute="flavor",
        attribute_default="sweet",
        qualia=["sad"],
        notes="this is a note",
    )
    database.add_equipment(id_="e_0", equipment="toolkit", is_common=True)
    database.add_verb(id_="v_0", method="mix", description="this is a verb")
    database.add_stage(
        id_="s_1",
        stage="preparation",
    )

    prep_step = Step(
        database,
        id_="step_0",
        stage=["preparation"],
        required_items=["anything"],
        verb=["mix"],
        action_notes="no action notes",
        duration=0,
        output="well",
        complexity=2,
    )

    assert prep_step.id_ == "step_0"
    assert prep_step.stage == [database.get_stage("preparation")]
    assert prep_step.required_items == [database.get_ingredient_or_equip("anything")]
    assert prep_step.verb == [database.get_verb("mix")]
    assert prep_step.action_notes == "no action notes"
    assert prep_step.duration == 0
    assert prep_step.output == "well"
    assert prep_step.complexity == 2

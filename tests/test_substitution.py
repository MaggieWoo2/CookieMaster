from ecl.statements.database import Database
from ecl.statements.substitution import Substitution


def test_substitution():
    database = Database()
    database.add_qualia(
        id_="q_0",
        qualia="happy",
        description="Hopefully this works",
        category="flavor",
        is_negative=False,
    )
    database.add_ingredient(
        id_="i_0",
        item="anything",
        inherit=["parent"],
        required_attribute=["flavor"],
        attribute_default=["sweet"],
        qualia=["happy"],
        notes="this is a note",
    )
    database.add_equipment(id_="e_0", equipment="toolkit", is_common=True)
    database.add_verb(id_="v_0", method="mix", description="this is a verb")
    database.add_stage(
        id_="s_1",
        stage="preparation",
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

    sub = Substitution(
        database,
        id_="sb_0",
        name="another method",
        items_out=["anything"],
        items_in=["anything"],
        in_out_ratio="1:2",
        steps_out=["step_0"],
        steps_in=["step_0"],
        scope="cookie",
        change_qualia_cookie=["happy"],
        change_qualia_brownie=["happy"],
        change_qualia_cupcake=["happy"],
        change_qualia_pancake=["happy"],
        steps_impacted="idk",
        change_actions="nope",
        change_duration="undecided",
        change_output="new output",
        change_complexity=3,
        ift="",
        action_notes="",
        change_step_note="",
        assumption="",
        notes="",
        explanation="",
    )

    assert sub.id_ == "sb_0"
    assert sub.name == "another method"
    assert sub.items_out == [database.get_ingredient("anything")]
    assert sub.items_in == [database.get_ingredient("anything")]
    assert sub.in_out_ratio == "1:2"
    assert sub.steps_out == [database.get_step("step_0")]
    assert sub.steps_in == [database.get_step("step_0")]
    assert sub.scope == "cookie"
    assert sub.change_qualia_cookie == [database.get_qualia("happy")]
    assert sub.change_qualia_brownie == [database.get_qualia("happy")]
    assert sub.change_qualia_cupcake == [database.get_qualia("happy")]
    assert sub.change_qualia_cupcake == [database.get_qualia("happy")]
    assert sub.steps_impacted == "idk"
    assert sub.change_actions == "nope"
    assert sub.change_duration == "undecided"
    assert sub.change_output == "new output"
    assert sub.change_complexity == 3

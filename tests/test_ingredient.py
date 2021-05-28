from ecl.statements.database import Database
from ecl.statements.ingredient import Ingredient


def test_ingredient():
    database = Database()
    database.add_qualia(
        id_="q_0",
        qualia="sad",
        description="Hopefully this works",
        category="flavor",
        is_negative=False,
    )
    flour = Ingredient(
        database,
        id_="i_0",
        item="anything",
        inherit=["parent"],
        required_attribute=["flavor"],
        attribute_default=["sweet"],
        qualia=["sad"],
        notes="this is a note",
    )

    assert flour.id_ == "i_0"
    assert flour.item == "anything"
    assert flour.inherit == ["parent"]
    assert flour.required_attribute == ["flavor"]
    assert flour.attribute_default == ["sweet"]
    assert flour.qualia == [database.get_qualia("sad")]
    assert flour.notes == "this is a note"

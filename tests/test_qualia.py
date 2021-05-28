from ecl.statements.database import Database
from ecl.statements.qualia import Qualia


def test_qualia():
    database = Database()
    happy = Qualia(
        database,
        id_="q_0",
        qualia="happy",
        description="Hopefully this works",
        category="flavor",
        is_negative=False,
    )
    assert happy.qualia == "happy"
    assert not happy.is_negative
    assert happy.description == "Hopefully this works"
    assert happy.category == "flavor"

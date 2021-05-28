from ecl.statements.database import Database
from ecl.statements.stage import Stage


def test_stage():
    database = Database()
    Prep = Stage(
        database,
        id_="s_1",
        stage="preparation",
    )
    assert Prep.id_ == "s_1"
    assert Prep.stage == "preparation"

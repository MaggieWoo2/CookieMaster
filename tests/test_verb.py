from ecl.statements.database import Database
from ecl.statements.verb import Verb


def test_verb():
    database = Database()
    move = Verb(database, id_="v_0", method="mix", description="this is a verb")
    assert move.id_ == "v_0"
    assert move.method == "mix"
    assert move.description == "this is a verb"

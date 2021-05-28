from ecl.statements.database import Database
from ecl.statements.equipment import Equipment


def test_equipment():
    database = Database()
    tool = Equipment(database, id_="e_0", equipment="toolkit", is_common=True)
    assert tool.id_ == "e_0"
    assert tool.item == "toolkit"
    assert tool.is_common

from sql_tools.core.queries import (
    version,
    user,
    databases,
    make_database,
    remove_database,
    tables,
    table_fields,
    table_fields_data,
    table_primary_start,
    table_content,
    make_table,
    remove_table,
    copy_table,
    add_field,
    remove_field,
    change_field,
    add_element,
    remove_elements,
    select_elements,
    update_element,
    select_optimised,
)

from sql_tools.types.datatypes import (
    INT,
    VARCHAR,
    BOOLEAN,
    ENUM,
    JSON,
    TIMESTAMP,
)

db = "TEST_DB"
tb = "TEST_TABLE"


def test_databases():
    _db = databases()
    assert _db
    assert len(_db) >= 4
    assert "mysql" in _db
    make_database(db)
    _db = databases()
    assert db in _db
    remove_database(db)
    _db = databases()
    assert not (db in _db)
    return 1


def test_table_manipulations():
    # init
    make_database(db)
    _tb = tables(db)
    # make table
    assert len(_tb) == 0
    make_table(db,
               tb,
               field1=INT(2),
               field2=VARCHAR(3, default=5),
               field3=JSON())
    _tb = tables(db)
    assert tb in _tb
    # check fields
    fields = table_fields(db, tb)
    assert "field1" in fields and \
           "field2" in fields and \
           "field3" in fields
    fields_data = table_fields_data(db, tb)
    # check fields type
    assert len(fields_data) == 3
    assert fields_data[0][0] == "field1"
    assert fields_data[0][1] == "int(2)"
    assert fields_data[1][0] == "field2"
    assert fields_data[1][1] == "varchar(3)"
    assert fields_data[2][0] == "field3"
    assert fields_data[2][1] == "json"
    # check fields manipulations
    add_field(db, tb, "field4", BOOLEAN(default=0))
    fields_data = table_fields_data(db, tb)
    assert len(fields_data) == 4
    assert fields_data[3][0] == "field4"
    assert fields_data[3][1] == "tinyint(1)"
    # change field
    change_field(db, tb, "field4", "fieldc", "INT(5)")
    fields_data = table_fields_data(db, tb)
    assert len(fields_data) == 4
    assert fields_data[3][0] == "fieldc"
    assert fields_data[3][1] == "int(5)"
    # delete field
    remove_field(db, tb, "fieldc")
    fields_data = table_fields_data(db, tb)
    assert len(fields_data) == 3
    # assert ??
    # clean table
    remove_table(db, tb)
    _tb = tables(db)
    assert len(_tb) == 0
    # Clean up test database
    remove_database(db)
    return 1


def test_elements_postget():
    # init
    make_database(db)
    _tb = tables(db)
    make_table(db,
               tb,
               field1=INT(3, True, auto_increment=True),
               field2=VARCHAR(3),
               field3=JSON(),
               primary_key="field1")
    table_primary_start(db, tb, 0)
    # table content
    ct = table_content(db, tb)
    assert len(ct) == 0
    # add elements
    add_element(db, tb, field2="kik", field3='[]')
    add_element(db, tb, field2="kok", field3='[]')
    ct = table_content(db, tb)
    assert len(ct) == 2
    assert ct[0][0] == 1
    assert ct[0][1] == "kik"
    assert ct[0][2] == '[]'
    assert ct[1][0] == 2
    assert ct[1][1] == "kok"
    assert ct[1][2] == '[]'
    # /!\ this isnt really it place but its a post get treatement
    # copy table
    copy_table(db, 'copied_table', tb)
    ct2 = table_content(db, 'copied_table')
    assert len(ct2) == 2
    assert ct2[0][0] == 1
    assert ct2[0][1] == "kik"
    assert ct2[0][2] == '[]'
    assert ct2[1][0] == 2
    assert ct2[1][1] == "kok"
    assert ct2[1][2] == '[]'
    #clear clone
    #remove_table(db, 'copied_table')
    # remove element
    remove_elements(db, tb, where="field2 = 'kik'")
    # recheck ct
    ct = table_content(db, tb)
    assert len(ct) == 1
    assert ct[0][1] == "kok"
    assert ct[0][2] == '[]'
    remove_elements(db, tb, where="field1 = 2", with_limit=1)
    ct = table_content(db, tb)
    assert len(ct) == 0
    # clean
    remove_table(db, tb)
    remove_database(db)
    return 1


def test_selections_advanced():
    #init
    def _column_of_matrix(matrix, column):
        return [i[column] for i in matrix]
    make_database(db)
    _tb = tables(db)
    make_table(db,
               tb,
               field1=INT(3, True, auto_increment=True),
               field2=VARCHAR(3),
               field3=JSON(),
               primary_key="field1")
    table_primary_start(db, tb, 0)
    add_element(db, tb, field2="kik", field3="[]")
    add_element(db, tb, field2="kok", field3='[0]')
    add_element(db, tb, field2="daw", field3='[]')
    add_element(db, tb, field2="rek", field3='[2, 3]')
    #select
    selection = select_elements(db,
                                tb,
                                with_limit=1,
                                selection='field2',
                                where="field1 = 3")
    assert len(selection) == 1
    assert selection[0][0] == 'daw'
    selection = select_elements(db,
                                tb,
                                selection='field2 , field3',
                                where="field1 > 2")
    assert len(selection) == 2
    assert selection[0][0] == 'daw'
    assert selection[0][1] == '[]'
    assert selection[1][0] == 'rek'
    assert selection[1][1] == '[2, 3]'
    selection = select_optimised(db,
                                 tb,
                                 with_limit=2,
                                 selection="*",
                                 kind="ASC",
                                 sorted_by="field1")
    assert _column_of_matrix(selection, 0) == [1, 2]
    remove_table(db, tb)
    remove_database(db)
    return 1


__all__ = [test_databases,
           test_table_manipulations,
           test_elements_postget,
           test_selections_advanced]

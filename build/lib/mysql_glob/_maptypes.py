from ._dt_pytypes import (INT,
                          VARCHAR,
                          JSON_DICT,
                          JSON_LIST,
                          JSON,
                          BOOLEAN)

map_types = {
    int : INT,
    str : VARCHAR,
    dict : JSON_DICT,
    list : JSON_LIST,
    'json' : JSON,
    bool : BOOLEAN,
}

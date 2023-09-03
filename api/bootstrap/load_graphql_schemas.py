from ariadne import load_schema_from_path
from typing import List

def load_schema():
    type_defs = []
    paths = [
        "api/schemas/",
        "api/user/schemas/"
    ]
    file_name = "schema.graphql"
    for path in paths:
        type_defs.append(
            load_schema_from_path(path + file_name)
        )
    return type_defs
    
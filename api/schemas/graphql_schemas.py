from ariadne import make_executable_schema
from ariadne.asgi import GraphQL
from api.bootstrap.load_graphql_schemas import load_schema

type_defs = load_schema()

schema = make_executable_schema(
    type_defs,
    [
        
    ]
)

graphql = GraphQL(
    schema=schema,
    debug=True,
)

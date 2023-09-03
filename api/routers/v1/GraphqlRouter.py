from fastapi import APIRouter
from api.schemas.graphql_schemas import graphql
from fastapi import Request

GraphqlRouter = APIRouter(
    prefix="/graphql",
    tags=["graphql", "v1"]
)

@GraphqlRouter.get("/")
def graphql_route():
    return graphql.handle_request()

# GraphqlRouter.
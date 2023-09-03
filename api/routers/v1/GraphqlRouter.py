from fastapi import APIRouter
from api.schemas.graphql_schemas import graphql
from fastapi import Request

GraphqlRouter = APIRouter(
    prefix="/graphql",
    tags=["graphql", "v1"]
)

@GraphqlRouter.get("/")
async def graphql_route(request: Request):
    return await graphql.handle_request(request)

# GraphqlRouter.
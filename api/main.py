from fastapi import FastAPI
import api.config as config
from api.routers.v1.GraphqlRouter import GraphqlRouter
from api.schemas.graphql_schemas import graphql

app = FastAPI()
ROUTE_PREFIX = f"/api/{config.API_VERSION}"

app.include_router(
    router=GraphqlRouter,
    prefix=ROUTE_PREFIX
)

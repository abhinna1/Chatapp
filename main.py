from fastapi import FastAPI
from fastapi.routing import BaseRoute, APIRoute, APIRouter, Route, Mount
from fastapi.responses import JSONResponse

    
    
ROUTES = [
    Route(
        "/",
        endpoint=root,
    ),
]

app = FastAPI(
    routes=Mount(
        path="/api/v1",
        routes=ROUTES,
    )
)

# @app.get("/")

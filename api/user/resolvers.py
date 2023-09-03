from ariadne.types import GraphQLResolveInfo

# Graphql resolver functions.

async def resolve_user(obj:any, info:GraphQLResolveInfo, **data) -> dict:
    return {
            "id": 1,
            "name": "user1",
            "email": "user@gmail.com"
        }
    
        
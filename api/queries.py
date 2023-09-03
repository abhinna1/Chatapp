from ariadne import QueryType
from api.user.resolvers import (
    resolve_user,
)
query = QueryType()

query.set_field("user", resolve_user)
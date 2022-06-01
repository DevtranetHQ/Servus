from collections import namedtuple

# AioHttpResponseWrapper Object fields/properties
RESPONSE_PROPS = ["response", "json", "data", "txt"]

# Response Model used for Serializing Response objects
AioHttpResponseWrapper = namedtuple(
    "AioHttpResponseWrapper", RESPONSE_PROPS, defaults={"json": {}}
)

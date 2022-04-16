from collections import namedtuple

RESPONSE_PROPS = ["response","json","data","txt"]
AioHttpResponseWrapper  = namedtuple("AioHttpResponseWrapper",RESPONSE_PROPS, defaults={"json":{}})


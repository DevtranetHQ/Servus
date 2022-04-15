import aiohttp

class AioRequestsClient():
    def __init__(self, *args, **kwargs):
        self.session = aiohttp.ClientSession()

    def get(self, url):
        pass
    
    def post(self, url):
        pass 

    def put(self, url):
        pass
    
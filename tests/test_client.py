from cgi import test
import servus
import asyncio

async def main():
    testClient = servus.aioclient.AioRequestsClient()
    response = await testClient.get("http://httpbin.org")
    print("My Response",response)

    await testClient.close_client()

asyncio.run(main())
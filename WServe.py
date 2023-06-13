#Websocket Echo Server
import asyncio
from websockets.server import serve


async def handler(websocket):
    async for message in websocket:
        

async def main():
    async with serve(handler, '10.4.50.240', 8000):
        await asyncio.Future()

asyncio.run(main())
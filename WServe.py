#Websocket Echo Server
import asyncio
import json
from websockets.server import serve
from WStrucks import Connections

con = Connections()

async def initWS(websocket, event):
    con.addController(event{"SenderID"})


async def handler(websocket):
    message = await websocket.recv()
    event = json.loads(message)

async def main():
    async with serve(handler, '10.4.50.240', 8000):
        await asyncio.Future()

asyncio.run(main())

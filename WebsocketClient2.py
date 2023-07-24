import asyncio
import websockets
import time
from random import randint

class client:

    def __init__(self, ID):
        self.ID = ID
        asyncio.run(self.JoinAndVibe())

    def joinMSG(self):
        return "JOIN" + self.ID

    async def JoinAndVibe(self):
        uri="ws://localhost:8080"

        async with websockets.connect(uri) as websocket:

            await websocket.send(self.joinMSG())
            async for message in websocket:
                await self.Response(websocket, message)
                return "000"
                

    async def Response(self, websocket, message):
        while("PONG" in message or "HEYO" in message):
            time.sleep(2)

            if(randint(0, 10) == 2):
                print("Sending message to another client")
                await self.Talk(websocket)


            await websocket.send("PING")
            print("PING")
            message = await websocket.recv()


        if("NONO" in message):
            return "001"
        
    async def Talk(self, websocket):
        await websocket.send("MSGS1234jklq")

    async def main(self):
        await asyncio.gather(self.JoinAndVibe())
            
example = client("1234jkls")

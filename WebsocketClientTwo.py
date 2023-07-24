import asyncio
import websockets
import time

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
        while("PONG" in message or "HEYO" in message or "auto" in message):

            if("auto" in message):
                print("You received a new message!")

            time.sleep(2)
            await websocket.send("PING")
            print("PING")
            message = await websocket.recv()


        
        
    async def main(self):
        await asyncio.gather(self.JoinAndVibe())
            
example = client("1234jklq")
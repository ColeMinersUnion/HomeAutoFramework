import websockets
import asyncio
import time

class MyServer:

    def __init__(self, Domain, port) -> None:
        self.Domain = Domain
        self.port = port
        self.connections = {}

        print("About to start the server")
        self.server = websockets.serve(self.handlerFunc, self.Domain, self.port)
        asyncio.get_event_loop().run_until_complete(self.server)
        asyncio.get_event_loop().run_forever()


    async def handlerFunc(self, websocket):
        print("The server is up and running")
        async for message in websocket:
            if("JOIN" in message and len(self.connections) < 25):
                ID = message.replace("JOIN", "")
                print("CONNECTION SUCCESSFUL")
                self.connections[ID] = websocket
                await self.Pong(websocket, message)
                

    async def Pong(self, websocket, message):
        while ("PING" in message or "JOIN" in message):
            time.sleep(2)
            await websocket.send("PONG")
            print("PONG")
            message = await websocket.recv()
        print("HELP")



server = MyServer("localhost", 8080)

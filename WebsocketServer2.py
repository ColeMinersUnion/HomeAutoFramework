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
        
        while ("PING" in message or "JOIN" in message or "MSGS" in message):

            if("MSGS" in message):
                id = message.replace("MSGS", "")
                await self.Talk(id)

            time.sleep(2)
            await websocket.send("PONG")
            print("PONG")
            message = await websocket.recv()
        
            

    async def Talk(self, ID):
        websocket = self.connections[ID]
        message = "Hi me, this is a auto generated message."
        print("About to send a message")
        await websocket.send(message)
        print("sent the message")
        



server = MyServer("localhost", 8080)


""" TO-DO:

Since each of the connections adds a new user to the connections dictionary,
I could have the response to the join message relay the active users. 
Actually I would rather receive a confirmation and send an update to all of the controller users of a new device. 

Find a way to close connections without just forcibly breaking out of the connection.

Integrate JSON as the way you organize data through communication.
Strings are cool but it's unorganized
"""


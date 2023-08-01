from WebsocketClient2 import client
import json
import asyncio
import websockets
from PrintColors import bcolors

class ControllerClient(client):

    def __init__(self, ID):
        super().__init__(ID)
        self.ws = None

    def start(self):
        asyncio.run(self.JoinAndVibe())

    def end(self):
        self.ws.close()
        
    async def JoinAndVibe(self):
        uri="ws://localhost:8080"

        websocket = await websockets.connect(uri)

        await websocket.send(self.genMsg("Join", "Server", msg=self.ID))
        async for message in websocket:
            self.ws = websocket

            await self.Response(websocket, message)
                

    async def Response(self, websocket, message):
        message = await websocket.recv()
        message = json.loads(message)

        if message["Type"] == "Welcome":
            print(bcolors.OKBLUE + str(message) + bcolors.ENDC)
            for i in message["Message"]:
                self.others.append(i)
            print("Connection Successful\n")

            print(self.others)
            print("\n")

        elif message["Type"] == "New_User":
            print("We got a new User")
            self.others.append(message["Message"])
            print(bcolors.WARNING + str(self.others) + bcolors.ENDC)

        await websocket.send(self.genMsg("PING", "Server"))
        print(bcolors.HEADER + "PING" + bcolors.ENDC)

        

    async def Toggle(self, recvr):
        await self.ws.send(self.genMsg("Command", recvr, msg="Toggle"))

    async def CheckState(self, recvr):
        await self.ws.send(self.genMsg("Command", recvr, msg="Check_State"))

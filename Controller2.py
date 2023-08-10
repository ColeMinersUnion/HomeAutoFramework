#Controller Client Pt 2

from WebsocketClient2 import client
import asyncio
import websockets
from PrintColors import bcolors
import json


class Controller(client):
    def __init__(self, ID):
        super().__init__(ID)
        self.ws = None

    async def toggle(self):
        await self.ws.send(self.genMsg("Command", "Server", msg="Toggle"))

    async def JoinAndVibe(self):
        uri="ws://localhost:8080"

        self.ws = await websockets.connect(uri)

        await self.ws.send(self.genMsg("Join", "Server", msg=self.ID))
        await self.Response()

    async def Response(self):

        websocket = self.ws

        await websocket.send(self.genMsg("PING", "Server"))
        print(bcolors.HEADER + "PING" + bcolors.ENDC)
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


    



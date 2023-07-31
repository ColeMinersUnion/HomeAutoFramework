from ..WebsocketV2.WebsocketClient2 import client
import json
import asyncio
from ..WebsocketV2.PrintColors import bcolors

class ControllerClient(client):

    def __init__(self, ID):
        super().__init__(ID)
        self.ws = None
        
    async def Response(self, websocket, message):
        self.ws = websocket
        while True:

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
            message = await websocket.recv()

    async def Toggle(self, recvr):
        await self.ws.send(self.genMsg("Command", recvr, msg="Toggle"))

    async def CheckState(self, recvr):
        await self.ws.send(self.genMsg("Command", recvr, msg="Check_State"))

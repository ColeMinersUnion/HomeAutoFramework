from WebsocketClient2 import client
import websockets
from PrintColors import bcolors
import json

class switch (client): 
    def __init__(self, ID, uri="ws://localhost:8080"):
        super().__init__(ID)
        self.uri = uri
        self.ws = None
        self.state = False
        self.pin = None #Pin(25, Pin.OUT)
        #PLEASE INITIALIZE PIN HERE

    def Wtoggle(self):
        self.state = not self.state
        self.pin.toggle()

    async def JoinAndVibe(self):
        self.ws = await websockets.connect(self.uri)
        await self.ws.send(self.genMsg("Join", "Server", msg=self.ID))
        await self.Response()

    async def Response(self):

        websocket = self.ws
        while(True):
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

            elif message["Type"] == "Toggle":
                print(bcolors.WARNING + str(self.state) + bcolors.ENDC)
                self.Wtoggle()

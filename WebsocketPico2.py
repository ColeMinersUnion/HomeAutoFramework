from WebsocketClient2 import client
from machine import Pin
import asyncio
import json
from PrintColors import bcolors

class HardwareClient (client):
    def __init__(self, ID, state, PIN):
        super().__init__(ID)
        self.state = state
        self.PIN = PIN

    async def Response(self, websocket, message):
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

            elif message["Type"] == "Command":
                print("New Commands!")
                if message["Message"] == "Toggle":
                    self.toggle()
                elif message["Message"] == "Check_State":
                    websocket.send(self.genMsg("Command", message["Sender"], msg=str(self.state)))


            #keeps the connection alive
            await websocket.send(self.genMsg("PING", "Server"))
            print(bcolors.HEADER + "PING" + bcolors.ENDC)
            message = await websocket.recv()
    
    def toggle(self):
        self.state = not self.state
        if self.state:
            self.PIN.value(0)
        else:
            self.PIN.value(1)

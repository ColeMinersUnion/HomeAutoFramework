import asyncio
import websockets
import time
from random import randint
import json
from PrintColors import bcolors

class client:

    def __init__(self, ID):
        self.ID = ID
        self.others = []
        
    def start(self):
        asyncio.run(self.JoinAndVibe())

    async def JoinAndVibe(self):
        uri="ws://localhost:8080"

        async with websockets.connect(uri) as websocket:

            await websocket.send(self.genMsg("Join", "Server", msg=self.ID))
            async for message in websocket:
                closed = await self.Response(websocket, message)
                if closed:
                    break

    async def Response(self, websocket, message):
        message = json.loads(message)
        while(message["Type"] == "PONG" or message["Type"] == "Welcome" or message["Type"] == "Command" or message["Type"] == "New_User"):
            time.sleep(2)

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
                print(message["Message"])
        
            if(randint(0, 10) == 2 and len(self.others) > 0):
               await websocket.send(self.genMsg("Command", self.others[0], msg="Hey!"))
                
            if randint(0, 20) == 5:
                print(bcolors.BOLD + bcolors.FAIL + "About to close the websocket!" + bcolors.ENDC + bcolors.ENDC)
                return True


            await websocket.send(self.genMsg("PING", "Server"))
            print(bcolors.HEADER + "PING" + bcolors.ENDC)
            message = await websocket.recv()
            message = json.loads(message)

        if message["Type"] == "Close":
            return True

        quit()
        
    def genMsg(self, Tpe, Recvr, msg="PING"):
        newMsg = {"Type": Tpe, "Sender": self.ID, "Recipient": Recvr, "Message": msg}
        return json.dumps(newMsg)

    async def main(self):
        await asyncio.gather(self.JoinAndVibe())
            

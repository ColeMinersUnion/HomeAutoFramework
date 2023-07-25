import websockets
import asyncio
import time

class MyServer:

    def __init__(self, Domain, port) -> None:
        self.Domain = Domainimport websockets
import asyncio
import time
import json

class MyServer:

    def __init__(self, Domain, port) -> None:
        self.Domain = Domain
        self.port = port
        self.connections = {}


    def start(self):
        print("About to start the server")
        self.server = websockets.serve(self.handlerFunc, self.Domain, self.port)
        asyncio.get_event_loop().run_until_complete(self.server)
        asyncio.get_event_loop().run_forever()


    async def handlerFunc(self, websocket):
        print("The server is up and running")
        async for message in websocket:
            message = json.loads(message)
            if(message["Type"] == "Join" and len(self.connections) < 25):
                print("CONNECTION SUCCESSFUL")
                self.connections[message["Message"]] = websocket
                print("Got here!")
                await self.Pong(websocket, message)
                

    async def Pong(self, websocket, message):
        
        others = self.connections.keys()

        

        await websocket.send(self.genMsg("Welcome", list(self.connections)[-1], msg=list(others)))

        print("Got here just fine")

        message = await websocket.recv()
        message = json.loads(message)

        while (message["Type"] == "PING" or message["Type"] == "Command"):

            if(message["Type"] == "Command"):
                await self.Talk(message)

            time.sleep(2)
            await websocket.send(self.genMsg("PONG", message["Sender"]))
            print("PONG")
            message = await websocket.recv()
            message = json.loads(message)

            
        
            

    async def Talk(self, msg):
        ID = msg["Recipient"]
        websocket = self.connections[ID]
        message = msg["Message"]
        print("About to send a message")
        await websocket.send(self.genMsg("Command", ID, message, msg["Sender"]))
        print("sent the message")

    def genMsg(self, Tpe, Recvr, msg="PONG", Sendr="Server"):
        newMsg = {"Type": Tpe, "Sender": Sendr, "Recipient": Recvr, "Message": msg}
        return json.dumps(newMsg)



server = MyServer("localhost", 8080)
server.start()


""" TO-DO:


I also want to figure out how to send a receive messages to specific devices
I should be able to increase the delay between ping-pongs because I'm sending messages in between.
how do i rearrange the awaitable objects so messages have a higher urgency

Find a way to close connections without just forcibly breaking out of the connection.

"""

"""Done:
Ping-Pong
Integrated Messaging (Before JSON)

Implemeted JSON messaging instead of strings

"""
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


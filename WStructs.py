import asyncio
from websockets.server import serve
import json
from websockets.sync.client import connect

class WSclient:
    def __init__(self, IP, ServerIP):
        self.IP = IP


class controlled(WSclient):
    def __init__(self, id, tags=[], IP, ServerIP):
        super().__init__(IP, ServerIP)
        self.state = find_state()
        self.name = id
        self.tags = []

    def find_state():
        #check current
        return True

    def __str__(self):
        return self.name

    async def recieve(self):
        with connect(ServerIP) as websocket:
            msg = await websocket.recv()
            #error check and send react accordingly. This should be the only thing run on a client side
            #check for ON/OFF or EchoState
            if (msg == 'Echo_State'):
                state = find_state()
                websocket.send(state)




class control(WSclient):
    def __init__(self, tandem, IP, ServerIP):
        super().__init__(IP, ServerIP)
        self.tandem = tandem
        self.state

    def toggle(self): 
        temp = tandem.state
        tandem.state = !temp
        self.state = !temp

        with connect(ServerIP) as websocket:
            message = {"reciever": str(self.tandem),
                        "oper": "New_State",
                        "newState": self.state}
            websocket.send(json.dumps(message))

    def checkState(self):
        with connect(ServerIP) as websokcet:
            message = {"reciever": str(self.tandem), "oper": "Echo_State", "newState": None}
            websocket.send(json.dumps(message))
            state = websocket.recv()
            state = self.state
        return state

class controller:
    def __init__(self):
        self.controls = {}
        self.groups = {}
    
    def add(self, Tcontrol):
        key = Tcontrol.tandem.id
        self.controls[key] = Tcontrol

    def createGroup(self, newGroup):
        #check to make sure this group doesn't exist yet otherwise it'll delete the members of the group
        self.groups[newGroup] = []

    def addMembers(self, newMember, Group):
        self.groups[Group].append(newMember)
        self.newMember.tags.append(Group)

    def GroupToggle(self, Group):
        ToBeTog = self.groups[Group]
        for tog in ToBeTog:
            tog.toggle()

class Connections:
    def __init__(self):
        self.controllers = {}
        self.devices = {}
    
    def addDevice(self, ID, Device):
        self.devices[ID] = Device
    
    def addController(self, ID, Controller):
        self.controllers[ID] = Controller

import asyncio
import json
from websockets.sync.client import connect
import random
import string

class WSclient:
    def __init__(self, IP, ServerIP):
        self.IP = IP


class controlled(WSclient):
    def __init__(self, tags=[]):
        super().__init__()
        self.state = self.find_state()
        self.id = self.gen_name()
        self.tags = tags

    def find_state():
        #check current
        return True

    def gen_name():
        random.seed()
        return "CONTROLLED".join(random.choices(string.ascii_lowercase + string.ascii_digits, k=10))


    def __str__(self):
        return self.id

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
        self.state = self.checkState()
        self.id = tandem.id

    def toggle(self, ID): 
        temp = tandem.state
        tandem.state = !temp
        self.state = !temp

        with connect(ServerIP) as websocket:
            message = { "oper": "toggle",
                        "reciever": str(self.tandem),
                        "sender": self.id}
            websocket.send(json.dumps(message))

    def checkState(self, ID):
        with connect(ServerIP) as websokcet:
            message = { "oper": "Echo_State", "reciever": str(self.tandem), "sender": ID}
            websocket.send(json.dumps(message))
            state = websocket.recv()
            state = self.state
        return state

class controller:
    def __init__(self):
        self.controls = {}
        self.groups = {}
        self.ID = self.gen_name()

    def gen_name():
        random.seed()
        return "CONTROLLER".join(random.choices(string.ascii_lowercase + string.ascii_digits, k=10))
    
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


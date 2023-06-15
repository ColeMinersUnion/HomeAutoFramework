#Websocket Server
import asyncio
import json
from websockets.server import serve
global connections = {}

async def initialize(websocket, ID):
    connections[ID] = websocket
    event = {"oper": "message", "body", "You have successfully been connected to the Websocket"}
    websocket.send(json.dumps(event))    

    

async def echo_state(websocket, reciever)
    try:
        sendr = connections[sender]
        recvr = connections[reciever]
    except:
        event = {"oper": "message", "body", "One or more of the attempted connections have not been initialized."}
        websocket.send(json.dumps(event))
        return

    event{"oper":"echo_state", "body":None}
    
    recvr.send(json.dumps(event))
    reply = await recvr.recv()
    sendr.send(reply)

async def handler(websocket):
    message = await websocket.recv()
    event = json.loads(message)
    """
    event["oper"] can be the following:
        init - initailizes the connection, happens when you turn the app on or when a device is online and powered
        echo_state - forwards the message to tandem, tandem sends back a message about current state
        toggle - toggles the machine
    """
    if event["oper"] == "init":
        await initialize(websocket, event["sender"])
    else:
        #send an error message back to the controller
        #to-do organize error codes

async def main():
    async with serve(handler, '127.0.0.1', 8000):
        await asyncio.Future()

asyncio.run(main())

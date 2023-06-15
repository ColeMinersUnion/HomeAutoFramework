import asyncio
from websockets.sync.client import connect

def hello():
    with connect("ws://127.0.0.1:8000") as websocket:
        websocket.send("Hello world!")
        message = websocket.recv()
        print(f"Received: {message}")

hello()

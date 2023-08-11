import tkinter as tk
from Controller2 import Controller
import asyncio
import threading

class pseudo_example():

    def __init__(self, ID):
        self.root = tk.Tk()
        self.root.minsize(500, 500)
        self.controller = Controller(ID)
        self.joined = False        

        self.app()
        
        

    async def start(self):
        await self.controller.JoinAndVibe()
        self.root.after(1000, await self.Pings())

    def app(self,):
        self.start_button = tk.Button(self.root, text="start", command=lambda: self.create_await_funct())
        self.start_button.pack()

        self.toggle_button = tk.Button(self.root, text="Toggle", command=lambda: self.create_toggle())
        self.toggle_button.pack()

        self.testfield = tk.Label(self.root, text="output")
        self.testfield.pack()

        self.status = tk.Label(self.root, text="Status")
        self.status.pack()
        self.root.mainloop()

    def create_toggle(self):
        threading.Thread(target=lambda loop: loop.run_until_complete(self.await_toggle()),
                         args=(asyncio.new_event_loop(),)).start()
        self.start_button["relief"] = "sunken"
        self.start_button["state"] = "disabled"

    def create_await_funct(self):
        threading.Thread(target=lambda loop: loop.run_until_complete(self.await_funct()),
                         args=(asyncio.new_event_loop(),)).start()
        self.start_button["relief"] = "sunken"
        self.start_button["state"] = "disabled"

    async def Pings(self):
        await self.controller.Response()
        self.root.after(1000, await self.Pings())

    async def await_toggle(self):
        self.status["text"] = "toggling"
        self.root.update_idletasks()

        await self.controller.toggle()

        self.status["text"] = "status"
        self.root.update_idletasks()

    async def await_funct(self):
        self.testfield["text"] = "Joined"
        self.root.update_idletasks()

        if not self.joined:
            await self.start()
            self.joined = True

        self.testfield["text"] = "About to toggle"
        self.root.update_idletasks()


if __name__ == '__main__':
    pseudo_example("Cole's MacBook Air")

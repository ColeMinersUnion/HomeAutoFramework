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


    def app(self,):
        self.start_button = tk.Button(self.root, text="start", command=lambda: self.create_await_funct())
        self.start_button.pack()

        self.testfield = tk.Label(self.root, text="output")
        self.testfield.pack()
        self.root.mainloop()

    def create_await_funct(self):
        threading.Thread(target=lambda loop: loop.run_until_complete(self.await_funct()),
                         args=(asyncio.new_event_loop(),)).start()
        self.start_button["relief"] = "sunken"
        self.start_button["state"] = "disabled"

    async def await_funct(self):
        self.testfield["text"] = "Pinging"
        self.root.update_idletasks()

        if not self.joined:
            await self.controller.JoinAndVibe()
            self.joined = True
        else:
            await self.controller.Response()

        self.testfield["text"] = "About to toggle"
        self.root.update_idletasks()

        await self.controller.toggle()

        self.testfield["text"] = "toggled"
        self.root.update_idletasks()
        self.start_button["relief"] = "raised"
        self.start_button["state"] = "normal"


if __name__ == '__main__':
    pseudo_example("Cole's MacBook Air").app()

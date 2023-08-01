from tkinter import *
from tkinter import ttk
from ControllerClient import ControllerClient
import asyncio

class AsyncApp(Tk):
    def __init__(self, loop, controller, UpdateInterval = 0.01):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.tasks = []
        self.controller = controller
        self.tasks.append(loop.create_task(self.controller.JoinAndVibe()))
        self.tasks.append(loop.create_task(self.updater(UpdateInterval)))

    async def updater(self, interval):
        while True:
            self.update()
            await self.controller.Response()
            await asyncio.sleep(interval)

    def close(self):
        for task in self.tasks:
            task.cancel()
        self.loop.stop()
        self.destroy()


loop = asyncio.get_event_loop()
app = AsyncApp(loop, ControllerClient("Cole's-Macbook-Air"))

frame = Frame(app)
frame2 = Frame(app)
app.title("UI for Lights")
lbl = Label(frame, text="Here's my websocket User Interface", justify=LEFT)
start = Button(frame2, text="Toggle", command=lambda: app.controller.Toggle("ESP32"))
end = Button(frame2, text="Close Connection", command=lambda: app.controller.end())

frame.pack(padx=10, pady=20)
frame2.pack(padx=20, pady=10)

app.mainloop()
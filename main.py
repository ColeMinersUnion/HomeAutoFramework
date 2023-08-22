from kivy.app import App, async_runTouchApp
#from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.config import Config
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock, ClockBaseBehavior

#non kivy imports
from Controller2 import Controller
import threading
import asyncio
from functools import partial
from PrintColors import bcolors
import json

Config.set("graphics", "width", "500")
Config.set("graphics", "height", "300")





class RoundedCornerLayout(FloatLayout):
    """
    Goal is just to get a rounded rectangle with a button that joins to the server for now
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(0.6, 0.6, 0.6, 1)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[(40, 40), (40, 40), (40, 40), (40, 40)],)

        self.bind(pos=lambda obj, pos: setattr(self.rect, "pos", pos))
        self.bind(size=lambda obj, size: setattr(self.rect, "size", size))

        self.size_hint = (None, None)
        self.size = (400, 200)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.background_color = 0, 0, 0, 1

        
    


class ControlApp(Controller, App):

    def __init__(self, ID):

        
        with open ("Info.txt", 'r') as file:
            uri = file.readline()
        
        Controller.__init__(self, ID, uri)
        App.__init__(self)
        

    def build(self):
        btn = Button(text="JOIN SERVER", font_size="20sp", background_color=(0.5, 0, 0, 1),
                     color=(0.75, 0, 0, 1), size=(32, 32), size_hint=(0.2, 0.2), pos=(300, 250))
        btn.bind(on_press=self.callback)

        r = RoundedCornerLayout()
        r.add_widget(btn)
        return(r)

    def callback(self, event):
        threading.Thread(target=lambda loop: loop.run_until_complete(self.start()),
                         args=(asyncio.new_event_loop(),)).start()
        

    #def threadResponse(self, event):
        #threading.Thread(target=lambda loop: loop.run_until_complete(self.indef_Ping()), 
                         #args=(asyncio.new_event_loop(),)).start()
    
    async def start(self):
        await self.JoinAndVibe()
        while True:
            await asyncio.sleep(1)
            await self.Response()


#this will try to open a file, if the file is unable to open, it doesn't exist. So it makes a new file
try:
    open("Info.txt", "r")
except:
    with open("Info.txt", "w") as file:
        file.write("ws://localhost:8080")



App = ControlApp("Cole's MacBook Air")    

App.run()

"""
#DONE
1. Write the last used IP into a file for storage between programs. 
2. On Open, present with a connect button. this will thread into the connect and will join that way.

#TO-DO

3. Make a widget for any given connection in the others attribute
4. Whenever a new connection appears, add a widget. (idk)
5. Make the widget have a button to toggle
6. Be able to edit the widget, have a list of icons to choose from, and be able to rename (just on the GUI)
"""

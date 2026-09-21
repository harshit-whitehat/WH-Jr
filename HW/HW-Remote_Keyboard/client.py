import kivy
kivy.require("1.11.1")
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemandmulti')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.core.window import Window
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.gridlayout import GridLayout

import socket, json
from  threading import Thread

SERVER = None
PORT = 8000
IP_ADDRESS = "127.0.0.1"

BUFFER_SIZE = 4096

class MyApp(App):
  def build(self):
    layout = GridLayout(cols=1)
    keyboard = VKeyboard(on_key_up=self.key_up)
    self.label= Label(text ="Selected key: ",font_size="50sp")
    layout.add_widget(self.label)
    layout.add_widget(keyboard)
    return layout

  def key_up(self, keyboard, keycode, *args):
    global SERVER
    if isinstance(keycode, tuple):
      keycode = keycode[1]

    self.label.text = "Selected key: "+str(keycode)
    print(str(keycode))
    SERVER.send(str(keycode).encode('ascii'))
  
  def setup():
    try:
      global SERVER  
      SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      SERVER.connect((IP_ADDRESS, PORT))
      return True
    except:
      return False

  setup_thread = Thread(target=setup)
  setup_thread.start()    

if __name__== '__main__':
  MyApp().run()

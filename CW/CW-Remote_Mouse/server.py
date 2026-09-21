import socket, autopy
from  threading import Thread
from pynput.mouse import Button, Controller
from screeninfo import get_monitors

SERVER = None
PORT = 8000
IP_ADDRESS = input("Enter your computer IP address: ").strip()

screen_width = None
screen_height = None
mouse = Controller()

def getDeviceSize():
  global screen_height, screen_width
  for m in get_monitors():
    screen_width = int(str(m).split(",")[2].strip().split("width=")[1])
    screen_height = int(str(m).split(",")[3].strip().split("height=")[1])

def acceptConnections():
  while True:
    client_socket, addr = SERVER.accept()
    print(f"Connection established with {client_socket} : {addr}")

    thread1 = Thread(target=recvMsg, args=client_socket)
    thread1.start()

def recvMsg(cli_socket):
  global mouse
  while True:
    try:
      msg = cli_socket.recv(2048).decode()
      if msg:
        newMsg = eval(msg)
        if msg["data"] == "left_click":
          mouse.press(Button.left)
          mouse.release(Button.left)
        elif msg["data"] == "right_click":
          mouse.press(Button.right)
          mouse.release(Button.right)        
        else:
          xPos = newMsg["data"][0] * screen_width
          yPos = screen_height * (1 - (newMsg["data"][1] - 0.2) / 0.6)
          mouse.position = (int(xPos), int(yPos))
    except:
      pass

def setup():
  print("\n\t\t\t*** Welcome To Remote Mouse ***\n")

  global SERVER, PORT, IP_ADDRESS

  SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  SERVER.bind((IP_ADDRESS, PORT))
  SERVER.listen(10)

  print("SERVER IS WAITING FOR INCOMING CONNECTIONS...\n")
  getDeviceSize()
  acceptConnections()

setup()

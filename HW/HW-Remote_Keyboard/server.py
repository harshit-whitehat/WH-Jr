import socket
from pynput.keyboard import Key, Controller
from threading import Thread

keyboard = Controller()

PORT = 8000
IP_ADDRESS = "127.0.0.1"
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((IP_ADDRESS, PORT))
SERVER.listen(10)

def recvMsg(cli, addr):
  while True:
    try:
      msg = cli.recv(2048).decode()
      if msg:
        keyboard.press(msg)
        keyboard.release(msg)
        print(msg)
    except:
      pass

def acceptConn():
  while True:
    cli, addr = SERVER.accept()
    print(">>> New connection made")
    thr = Thread(target=recvMsg, args=(cli, addr))
    thr.start()

acceptConn()
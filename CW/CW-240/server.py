import socket
from threading import Thread

IP_ADDR = "127.0.0.1"
PORT = 8080
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP_ADDR, PORT))

def handleClients(cli, addr):
  print(f"{cli} has connected successfuly")

while True:
  server.listen(10)
  client, address = server.accept()
  if client:
    clients.append([client, address])
  
  cliThread = Thread(target=handleClients, args=(client, address))
  cliThread.start()

import socket

IP_ADDR = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((IP_ADDR, PORT))

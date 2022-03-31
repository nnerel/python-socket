import socket


HOST = '127.0.1.1'
PORT = 3333
ADDRESS = (HOST, PORT)
HEADER = 64
CHARSET = 'utf-8'
DISCONNECT_MESSAGE = '@DICCONNECT@'


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)
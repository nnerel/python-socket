import socket
import threading


HOST = socket.gethostbyname(socket.gethostname())
PORT = 3333
ADDRESS = (HOST, PORT)
HEADER = 64
CHARSET = 'utf-8'
DISCONNECT_MESSAGE = '@DICCONNECT@'


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDRESS)


def client_wrapper(connection, address):
    print("[NEW CONNECTION]")
    connected = True
    while connected:
        mess_length = connection.recv(HEADER).decode(CHARSET)
        if mess_length:
            mess_length = int(mess_length)
            mess = connection.recv().decode(CHARSET)

            if mess == DICCONNECT:
                connected = False

            print(f"[{address}]\n{mess}")

    connection.close()


def run_server():
    server.listen()
    print(f"[LISTENING] on {HOST!r}")
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=client_wrapper, args=(connection, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]  {threading.activeCount()-1}")


print("[SERVER STARTING]")
run_server()


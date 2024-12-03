import socket
import pickle
from datetime import datetime
from threading import Thread

BUFFER_SIZE = 1024  # 1kb


class ClientHandler(Thread):
    def __init__(self, connection: socket.socket, clients: list['ClientHandler'], client_data: dict):
        super().__init__(daemon=True)
        self.clients = clients
        self.connection = connection
        self.client_data = client_data
        self.start()

    def run(self):
        while True:

            if self.client_data[self.connection.getpeername()] == self.connection.getpeername():

                nick_in_bytes = self.recv()
                nick = pickle.loads(nick_in_bytes)['body']

                if nick not in list(self.client_data.values()):
                    self.client_data[self.connection.getpeername()] = nick
                    self.client_name = nick
                    break

                else:
                    self.send(pickle.dumps({'body': 'This username is already taken'}))

        while True:

            data_in_bytes = self.recv()
            data: dict = pickle.loads(data_in_bytes)

            for client in self.clients:  # type: ClientHandler
                packet = {**data, 'timestamp': datetime.now()}

                if client == self:
                    packet['body'] = f"From YOU: {packet.get('body')}"

                else:
                    packet['body'] = f"From {self.client_data[self.connection.getpeername()]}: {packet.get('body')}"
                data_in_bytes: bytes = pickle.dumps(packet)
                client.send(data_in_bytes)

    def recv(self) -> bytearray:
        result = bytearray()
        while True:
            data: bytes = self.connection.recv(BUFFER_SIZE)
            result.extend(data)
            if result.endswith(Server.STOP):
                break
        return result[:-3]

    def send(self, msg: bytes):
        self.connection.send(msg + Server.STOP)


class Server:
    STOP = b'///'

    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print('Socket created')
        self.sock.bind((host, port))
        print('Socket binded')
        self.sock.listen(1)
        print('Socket now listening')
        self.clients: list[ClientHandler] = []
        self.client_data: dict = {}

    def serve_forever(self):
        while True:
            print('Waiting for connection')
            client_socket, client_address = self.sock.accept()
            print('Connection from', client_address)
            self.client_data[client_address] = client_address
            self.clients.append(ClientHandler(client_socket, self.clients, self.client_data))


server = Server('localhost', 9000)
server.serve_forever()

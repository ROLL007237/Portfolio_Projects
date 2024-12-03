import socket
import pickle
from threading import Thread

BUFFER_SIZE = 1024


class Client:
    STOP = b'///'

    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket created')
        self.sock.connect((host, port))
        print('Socket connected\n')
        print('Welcome to ShitHole messenger\n'
              'to PM write /*username* *msg*\n'
              'Enter your nickname: ')

    def recv(self) -> bytearray:
        result = bytearray()
        received_bytes = 0
        while True:
            data: bytes = self.sock.recv(BUFFER_SIZE)
            received_bytes += len(data)
            result.extend(data)
            if result.endswith(Client.STOP):
                break

        return result[:-3]

    def send(self, msg: bytes):
        self.sock.send(msg + Client.STOP)
        print('already sent')

    def input_stream(self):
        while True:
            packet = dict(datatype='text', body='', optional=None)
            packet['body'] = input()
            self.send(pickle.dumps(packet))

    def output_stream(self):
        while True:
            answer_from_server: bytes = self.recv()
            answer: dict = pickle.loads(answer_from_server)
            print(answer.get('body'))

    def chatting(self):
        Thread(target=self.input_stream).start()
        Thread(target=self.output_stream).start()


client = Client('localhost', 9000)
client.chatting()

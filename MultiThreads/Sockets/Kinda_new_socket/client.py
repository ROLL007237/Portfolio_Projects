import socket
import pickle

BUFFER_SIZE = 1024

class Client:
	STOP = b'///'

	def __init__(self, host, port):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print('Socket created')
		self.sock.connect((host, port))
		print('Socket connected')

	def recv(self) -> bytearray:
		result = bytearray()
		received_bytes = 0
		while True:
			data: bytes = self.sock.recv(BUFFER_SIZE)
			print('bytes received:', len(data))
			received_bytes += len(data)
			result.extend(data)
			if result.endswith(Client.STOP):
				break
		print('TOTAL', received_bytes)
		return result[:-3]

	def send(self, msg: bytes):
		self.sock.send(msg + Client.STOP)
		print('already sent')


client = Client('localhost', 9000)
data_in_bytes: bytes = client.recv()
print('recieved', len(data_in_bytes))
data: dict = pickle.loads(data_in_bytes)
print(data)
print(type(data))
print(data.get('type'))
import socket
import pickle

BUFFER_SIZE = 1024  # 1kb

filepath = '/home/alex/apti.jpg'


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

	def serve_forever(self):
		while True:
			print('Waiting for connection')
			client_socket, client_address = self.sock.accept()
			print('Connection from', client_address)

			# with open(filepath, 'rb') as file:
			# 	image_in_bytes: bytes = file.read()
			my_super_protocol = {'type': 'text', 'body': 'adsfghjfhdsafdgtfhj sdgfhj'}
			bytes_to_send = pickle.dumps(my_super_protocol)
			self.send(client_socket, bytes_to_send)
			print('wait a data')

	def recv(self) -> bytearray:
		result = bytearray()
		while True:
			data: bytes = self.sock.recv(BUFFER_SIZE)
			result.extend(data)
			if result.endswith(Server.STOP):
				break
		return result[:-3]

	def send(self, client_socket, msg: bytes):
		d = bytearray(msg)
		sent = client_socket.send(d + Server.STOP)
		print('already sent', sent)


server = Server('localhost', 9000)
server.serve_forever()

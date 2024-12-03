import socket
# ipv4
# ipv6
# TCP SOCK_STREAM
# UDP SOCK_DGRAM
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print('Socket created')
BUFFER_SIZE = 5
sock.bind(('127.0.0.1', 9000))
print('Socket binded')

STOP = '///'

sock.listen(1)
print('Socket now listening')

print('Waiting for connection')
client_socket, client_address = sock.accept()

print('Connection from', client_address)
print(client_socket)

print('wait a data')

def recv(conn: socket.socket) -> str:
	result = ''
	while True:
		data: bytes = conn.recv(BUFFER_SIZE)
		print('received the data', data)
		text: str = data.decode('utf-8')
		result += text
		if len(data) < BUFFER_SIZE or result.endswith(STOP):
			break
	return result[:-3]

def send(conn: socket.socket, msg):
	msg += STOP
	conn.send(msg.encode('utf-8'))
	print('already sent')

print('result')
text = recv(client_socket).upper()
send(client_socket, text)
print('already sent')

client_socket.close()
import socket
# ipv4
# ipv6
# TCP SOCK_STREAM
# UDP SOCK_DGRAM
BUFFER_SIZE = 5 # SIZE OF A PACKET

STOP = '///' # STOP WORD

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

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

address = ('127.0.0.1', 9000)
sock.connect(address)
print('Socket connected')

send(sock, input("Write down your message"))



text: str = recv(sock)
print('got the msg!', text)

sock.close()
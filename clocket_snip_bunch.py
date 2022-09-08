
def get_data_from_srv():
	host = 
	port = 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host), (port))
	s.sendall(b'Hello World')
	data = s.recv(1024)
	s.close()
	return repr(data)


class Clocket:

    def __init__(self, socket):
        if sock is None:
            sock.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host="127.0.0.1", port=5007):
        self.sock.connect((host, port))


    def send_msg(self, msg):
    	msg =struct.pack('>I', len(msg)) + msg
    	self.sock.sendall(msg)


    def recv_msg(self):
    	raw_msglen = recvall(sock, 4)
    	if not raw_msglen:
    		return None
    	msglen = struct.unpack('>I', raw_msglen)[0]
    	return recvall(self.sock, msglen)

    def recvall(self, n):
    	data = ''
    	while len(data) < n:
    		packet = self.sock.recv(n - len(data))
    		if not packet:
    			return None
    		data += packet
    	return data

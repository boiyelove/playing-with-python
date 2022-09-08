import socket
import struct

class Slocket:

    def __init__(self, sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)):
        self.clients = ''
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host="127.0.0.1", port=5007):
        self.sock.bind((host, port))
        self.sock.listen(1)
        print ("Listening on port: "+str(port))
        while True:
        	client, sock_addr = self.sock.accept()
        	print ("Accepted connection from", sock_addr)
        	self.clients += ":::" + str(sock_addr)
        	while True:
                    data = self.recv_msg(client)
                    if data is None: break
                    reply = self.do_something(data)
                    self.send_msg(client, reply)
        	client.close()
        	print("Connection Closed")


    def send_msg(self, client, msg):
    	msg = struct.pack('>I', len(msg)) + msg
    	client.sendall(msg)


    def recv_msg(self,client):
    	raw_msglen = self.recvall(client, 4)
    	if not raw_msglen:
    		return None
    	msglen = struct.unpack('>I', raw_msglen)[0]
    	return self.recvall(client, msglen)

    def recvall(self, client, n):
    	data = ''
    	while len(data) < n:
    		packet = client.recv(n - len(data))
    		if not packet:
    			return None
    		data += packet.decode()
    	return data.encode()

    def do_something(self, data):
        b = self.clients
        return b.encode()

    


if __name__ == "__main__":
	new_client = Slocket()
	new_client.connect()









s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org". 80))


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 80))
serversocket.listen(5)

while True:
    (clientsocket, address) = serversocket.accept()
    ct = client_thread(clientsocket)
    ct.run()



class MySocket:

    def __init__(self, socket):
        if sock is None:
            sock.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))


    def mysend(self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def receive(self):
        chunk = []
        bytes_read = 0
        while bytes_read < MSGLEAN:
            chunk = self.sock.recv(min(MSGLEN = bytes_read, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunk.append(chunk)
            bytes.read = bytes_read + len(chunk)
        return b''.join(chunks)
            

import socket
import struct

class Clocket:

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host="127.0.0.1", port=5007):
        self.sock.connect((host, port))


    def send_msg(self, msg):
        feedback = False
        msg = struct.pack('>I', len(msg)) + msg.encode()
        self.sock.sendall(msg)

        
    def recv_msg(self):
        raw_msglen = self.recvall(4)
        if not raw_msglen:
            return None
        msglen = struct.unpack('>I', raw_msglen)[0]
        return self.recvall(msglen)

    def recvall(self, n):
        data = ''
        while len(data) < n:
            packet = self.sock.recv(n - len(data))
            if not packet:
                return None
            data += packet.decode()
        return data.encode()

    def close(self):
        return self.sock.close()


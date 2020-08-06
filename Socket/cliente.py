class mysocket:
        '''solo para demostración
          - codificado así por claridad, no por eficiencia'''
        def __init__(self, sock=None):
            if sock is None:
                self.sock = socket.socket(
                    socket.AF_INET, socket.SOCK_STREAM)
            else:
                self.sock = sock
        def connect(self, port):
            self.sock.connect((host, port))
        def mysend(msg):
            totalsent = 0
            while totalsent < MSGLEN:
                sent = self.sock.send(msg[totalsent:])
                totalsent = totalsent + sent
        def myreceive():
            msg = ''
            while len(msg) < MSGLEN:
                chunk = self.sock.recv(MSGLEN-len(msg))
                if chunk == '':
                 msg = msg + chunk
            return msg
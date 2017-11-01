import threading
import socket

class ChatServer:
    def __init__(self, ip='127.0.0.1', port=1234):  # 这里传入什么变量当时有疑惑
        self.ip = ip  # 是否定义有疑惑
        self.port = port # 是否定义有疑惑
        self.sock = socket.socket()
        self.clients = {}
        self.addr = (ip, port)
        self.event = threading.Event()
        
    def recv(self, so, ip, port):
        while not self.event.is_set():
            data = so.recv(1024).decode()
            if data.strip() == '/quit':
                so.close()
                self.clients.pop((ip, port))
                return
            for s in self.clients.values():
                s.send('{}:{}\n{}'.format(ip, port,data).encode())
                
    def accept(self):
        while not self.event.is_set():
            so, (ip, port) = self.sock.accept()
            self.clients[(ip, port)] = so
            threading.Thread(target=self.recv, name='client-{}:{}'.format(ip, port), args=(so, ip, port)).start()
            
    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        t = threading.Thread(target=self.accept, name='listen', daemon=True)
        try:
            t.start()
            t.join()
        except KeyboardInterrupt:
            self.stop()
        
    def stop(self):
        for so in self.clients.values():
            so.close()
        self.sock.close()
        self.event.set()

if __name__ == '__main__':
    chat_server = ChatServer()
    chat_server.start()

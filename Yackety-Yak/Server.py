import threading, socket, random
_receive_ = []
clients = []
s = socket.socket()
s.bind(('', 12345))
print("Bound")
s.listen()
message_count = 0
message = ''
count = 0
key = random.randint(0, 256)

def receive():
    global t1
    global message
    global message_count
    print("receive started!")
    c, addr = s.accept()
    c.send(str.encode(str(key + 10)))
    clients.append(c)
    _receive_.append(t1)
    print("Received connection!")
    t1 = threading.Thread(target=receive)
    t1.start()
    while True:
        message = str(c.recv(1024), "utf-8")
        message_count += 1
        for i in range(len(clients)):
            if clients[i] != c:
                clients[i].send(str.encode(str(addr[1])  + ' _:_ ' + message))

t1 = threading.Thread(target=receive)

t1.start()
while True:
    if count != message_count:
        count += 1

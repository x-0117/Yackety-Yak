import socket, threading
s = socket.socket()
s.connect((socket.gethostbyname('localhost'), 12345))
print("Connected!")
public_key = int(str(s.recv(1024), "utf-8")) - 10
def send():
    while True:
        message = list(input('>>'))
        for i in range(len(message)):
            message[i] = chr(ord(message[i]) ^ public_key)
        s.send(str.encode(''.join(message)))
threading.Thread(target=send).start()
while True:
    port, message1 = str(s.recv(1024), "utf-8").split(' _:_ ')
    message2 = list(message1)
    for i in range(len(message2)):
        message2[i] = chr(ord(message2[i]) ^ public_key)
    print(port, ':', ''.join(message2))

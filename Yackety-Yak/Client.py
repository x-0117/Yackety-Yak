import socket, _thread, base64
s = socket.socket()
s.connect((socket.gethostbyname('localhost'), 12345))
print("Connected!")
x = int(str(s.recv(2048), "utf-8"))
print("x = ", x)


def send():
    while True:
        message = input("\t\t\t\t")
        if message[:6] == "!file:":
            message = "!file:" + str(base64.b64encode(open(message[6:], 'rb').read()))
        print('_', message)
        a, l, flag = 0, len(message), 0
        while flag == 0:
            if l - a <= 1000:
                section = message[a:l] + '!end'
                flag = 1
            else:
                section = message[a:a + 1000]
            if a != 0:
                section = "!cont:" + section
            a += 1000
            l1 = list(message)
            for i in range(len(message)):
                l1[i] = chr(ord(l1[i]) ^ x)
            s.send(str.encode(''.join(l1)))
    

_thread.start_new_thread(send, ())
num = 0
while True:
    l1 = list(str(s.recv(2048), "utf-8"))
    for i in range(len(l1)):
        l1[i] = chr(ord(l1[i]) ^ x)
    reply = ''.join(l1)
    base = ''
    if reply[:6] == "!file:":
        num += 1
        base += base64.b64decode(reply[6:])
        if reply[-4:] == "!end":
            open("C:/Users/User/Desktop/Server/shit{}".format(num), 'ab').write(base64.b64decode(shit)
    elif reply[:6] == "!cont:":
        base += base64.b64decode(reply[6:])
        if reply[-4:] == "!end":
            open("C:/Users/User/Desktop/Server/shit{}".format(num), 'ab').write(base64.b64decode(shit)
    else:
        print(reply)
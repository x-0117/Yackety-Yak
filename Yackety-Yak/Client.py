import socket, threading, sys, time
destination = input("Specify Destination folder : ")
try:
    test = open(destination + "/test.txt", 'w')
    test.write("Checking the destination folder! You may delete this file!")
    test.close()
except:
    print("Folder not found or access denied! Default location : Location of the Client_chatbox.py file")
    destination = '.'
s = socket.socket()
s.connect((socket.gethostbyname('localhost'), 12345))
print("Connected!")
file_count = 0
transferred_file = open(destination + '/test.txt', 'ab')
public_key = int(str(s.recv(1024), "utf-8")) - 10
print(public_key)
def send():
    while True:
        message = list(input('>>'))
        if message[:6] == list("!file:"):
            print("Sending file!")
            try:
                file_content = open(''.join(message[6:]), 'rb').read()
                x = len(file_content)
                i, j = 0, min(1000, x)
                s.send(str.encode('0'))
                s.send(str.encode(''.join([chr(ord(i) ^ public_key) for i in "!file:"])))
                time.sleep(0.5)
                while j != x:
                    s.send(str.encode('1'))
                    s.send(file_content[i:j])
                    time.sleep(0.1)
                    i, j = j, min(j + 1000, x)
                s.send(str.encode("1"))
                s.send(file_content[i:j])
            except:
                print(sys.exc_info()[1])
                print("File not found! Have you provided the full path?")
            continue
        for i in range(len(message)):
            message[i] = chr(ord(message[i]) ^ public_key)
        s.send(str.encode('0'))
        s.send(str.encode(''.join(message)))
threading.Thread(target=send).start()
while True:
    flag = int(str(s.recv(1024), "utf-8"))
    received = s.recv(1024)
    if flag == 0:
        port, message1 = str(received, "utf-8").split(' _:_ ')
    if flag == 1:
        transferred_file = open(destination + '/file' + str(file_count), 'ab')
        transferred_file.write(received)
        transferred_file.close()
        continue
    message2 = list(message1)
    for i in range(len(message2)):
        message2[i] = chr(ord(message2[i]) ^ public_key)
    if message2 == list("!file:"):
        file_count += 1
        message2 = list("Receiving file" + str(file_count))
    print(port, ':', ''.join(message2))

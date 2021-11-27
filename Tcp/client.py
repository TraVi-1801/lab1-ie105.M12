import socket

#HOST cua server 
HOST = "192.168.153.128"
#PORT ket noi
PORT = 3000

context = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tao ket noi den server thong host
context.connect((HOST, PORT))

name = input('Enter your name: ')

context.sendall(bytes(name,"utf-8"))
data = context.recv(1024)
print(data.decode("utf-8"))
context.close()

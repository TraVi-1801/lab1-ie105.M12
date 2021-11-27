import socket
import ssl

#HOST cua server 
HOST = "192.168.153.128"
#PORT ket noi
PORT = 3000

context = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ssl.wrap_socket() dung de chuyen mot the hien socket.socket context thanh mot the hien ssl.SSLSocket
# context la mot the hien cua socket.socket va phải là SOCK_STREAM,  các loại socket khác không được hỗ trợ. 
# server_side the hien hanh vi may server hay client, neu server thi no bang true 
#keyfile="./client.key" va certfile="./client.pem" chua key va chung chi cua client
context = ssl.wrap_socket(context, keyfile="./client.key", certfile="./client.pem")

context.connect((HOST, PORT))

name = input('Enter your name: ')

context.sendall(bytes(name,"utf-8"))
data = context.recv(1024)
print(data.decode("utf-8"))
context.close()

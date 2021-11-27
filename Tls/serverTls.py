import socket
import ssl

HOST = "192.168.153.128"
PORT = 3000


context = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


context = ssl.wrap_socket(
        context, server_side = True, keyfile = "./server.key", certfile = "./server.pem"
)

context.bind((HOST,PORT))
context.listen(5)
conn, addr = context.accept()

print("Connected by", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    message = "Hello "+ data.decode("utf-8")
    conn.sendall(bytes(message,"utf-8"))
    context.close()

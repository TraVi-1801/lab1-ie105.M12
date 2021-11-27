import socket

# dia chi ip cua may server IPV4
HOST ="192.168.153.128"
# post ket noi
POST = 3000

# socket.socket() tao mot thuc the socket va co hai tham so 
# socket.AF_INET the hien dia chi ipv4
# socket.SOCK_STREAM giao thuc TCO huong ket noi
context = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind() 


context.listen(5)
content, addr = context.accept()

# in ra man hinh dia chi may client ket noi
print("Connected by", addr)
while True:
    # gan du lieu nhan tu client cho data
    data = content.recv(1024)
    if not data:
        break
    #data.decode("utf-8") giai ma du lieu
    message = "Hello " + data.decode("utf-8")
    # gui du lieu di cho may client
    content.sendall(bytes(message,"utf-8"))
    # dong ket noi
    context.close()

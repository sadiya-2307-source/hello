from socket import *
s=socket()
s.bind(('localhost',9999))
s.listen(5)
while 1:
    c1,addr=s.accept()
    c2,addr=s.accept()
    name=c1.recv(1024).decode()
    print(name)
    c2.send(bytes(name),'utf-8')
    name1=c2.recv(1024).decode()
    c1.send(bytes(name1),'utf-8')
    c1.close()
    c2.close()

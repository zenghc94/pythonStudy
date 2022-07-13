import socket

#创建套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#绑定地址
s.bind(('127.0.0.1', 6666))#双括号，要英文

#监听连接
s.listen(5) #数字5，我TM写的s
while True:
    print('等待客户发送信息。。。')
    #接受连接
    sock, addr = s.accept()
    #接受请求数据
    data = sock.recv(1024).decode('utf-8')
    print('服务端接受请求数据：'+ data)
    #发送响应数据
    sock.sendall(data.upper().encode('utf-8'))
    #关闭
    sock.close()
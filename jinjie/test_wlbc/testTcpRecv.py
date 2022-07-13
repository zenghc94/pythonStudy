# 客户端基本思路：
#
# 创建套接字，连接服务端
#
# 连接后发送、接收数据
#
# 传输完毕后，关闭套接字
#
# 具体代码实现如下：

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#连接服务端
s.connect(('127.0.0.1', 6666))
#向服务端发送数据
s.sendall(b"hello")
#接受服务端数据
data = s.recv(1024)
print('客户端接受响应数据：'+data.decode('utf-8'))
#关闭
s.close()

# 我们只需先运行服务端代码，再运行客户端代码即可。
# 客户端基本思路：
#
# 创建套接字
#
# 向服务端发送数据
#
# 接受服务端响应数据
#
# 具体代码实现如下：

import socket

#创建套接字
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#向服务端发送数据
s.sendto(b'hello  udp', ('127.0.0.1', 6666))#只能发送b字节啊，不能中文，只能ASCII
#接受服务端请求
data = s.recv(1024).decode('utf-8') #我还以为recv只能tcp得
# data = s.recvfrom(1024)[0].decode('utf-8') 可以这样

print('客户端接受响应数据：'+data)
#关闭
s.close()

# 同样的，我们还是先运行服务端代码，再运行客户端代码即可。
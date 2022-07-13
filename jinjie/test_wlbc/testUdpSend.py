# 2.3 UDP 方式
# 我们再来看一下如何通过 socket 以 UDP 方式进行通信。
#
# 服务端基本思路：
#
# 创建套接字，绑定套接字到 IP 与端口
#
# 接收客户端请求的数据
#
# 向客户端发送响应数据
#
# 具体代码实现如下：

import socket
#创建套间字

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定地址
s.bind(('127.0.0.1', 6666))#连个括号，元祖？？
while True:
    #接受数据
    data, addr = s.recvfrom(1024)
    print('服务端接受请求数据：' +data.decode('utf-8'))
    #响应数据
    s.sendto(data.decode('utf-8').upper().encode('utf-8'), addr)
    # s.sendto(data, addr)可以删除其他的配置，但是好像有问题upper是大写，其他是编码解码
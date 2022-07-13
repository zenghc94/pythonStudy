# Python 进阶（十）：网络编程
# 原创 py小二 Python小二 2020-03-07 08:34
# 图片
# 点击上方蓝字关注，学习 Python
# 1. 简介
# 网络编程主要的工作就是在发送端将信息通过指定的协议进行组装包，在接收端按照规定好的协议对包进行解析并提取出对应的信息，最终达到通信的目的。传输协议主要有 TCP 和 UDP，TCP 需要建立连接，是可靠的、基于字节流的协议，通常与 IP 协议共同使用；UDP 不需要建立连接，可靠性差，但速度更快。
#
# 网络编程有一个重要的概念 socket（套接字），应用程序可以通过它发送或接收数据，套接字允许应用程序将 I/O 插入到网络中，并与网络中的其他应用程序进行通信。
#
# Python 提供了如下两个 socket 模块：
#
# Socket：提供了标准的 BSD Sockets API，可以访问底层操作系统 Socket 接口的全部方法。
#
# SocketServer：提供了服务器中心类，可以简化网络服务器的开发。
#
# 2. 使用
# 2.1 API 介绍
# Python 中通过 socket() 函数来创建套接字对象，具体格式如下：
#
# socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
#
# family：套接字协议族，可以使用 AF_UNIX（只能用于单一的 Unix 系统进程间通信）、AF_INET（服务器之间网络通信）
#
# type：套接字类型，可以使用 SOCK_STREAM（面向连接的）、SOCK_DGRAM（非连接的）
#
# 套接字对象服务端方法：
#
# 方法	描述
# bind(address)	将套接字绑定到地址，在 AF_INET 下以元组 (host,port) 的形式表示地址
# listen([backlog])	开始监听 TCP 传入连接，backlog 指定在拒绝连接之前，操作系统可以挂起的最大连接数量，至少为1，大部分应用程序设为 5 就可以了
# accept()	接受 TCP 连接并返回 (conn,address)，conn 是新的套接字对象，可以用来接收、发送数据，address 是连接客户端的地址
# 套接字对象客户端方法：
#
# 方法	描述
# connect(address)	连接到 address 处的套接字，格式一般为元组 (hostname,port)，如果连接出错，返回 socket.error 错误
# connect_ex(address)	功能与 connect(address) 相同，但是成功返回 0，失败返回 errno 的值
# 套接字对象公用方法：
#
# 方法	描述
# recv(bufsize[, flags])	接受 TCP 套接字的数据，数据以字符串形式返回，bufsize 指定要接收的最大数据量，flag 提供有关消息的其他信息，通常可以忽略
# send(bytes[, flags])	发送 TCP 数据，将 string 中的数据发送到连接的套接字，返回值是要发送的字节数量，该数量可能小于 string 的字节大小
# sendall(bytes[, flags])	完整发送 TCP 数据，将 string 中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据，成功返回 None，失败则抛出异常
# recvfrom(bufsize[, flags])	接受 UDP 套接字的数据，与 recv() 类似，但返回值是 (data,address)，其中 data 是包含接收数据的字符串，address 是发送数据的套接字地址
# sendto(bytes, flags, address)	发送 UDP 数据，将数据发送到套接字，address 是形式为 (ipaddr,port) 的元组，指定远程地址，返回值是发送的字节数
# close()	关闭套接字
# getpeername()	返回连接套接字的远程地址，类型通常是元组 (ipaddr,port)
# getsockname()	返回套接字自己的地址，通常是一个元组 (ipaddr,port)
# setsockopt(level,optname,value)	设置给定套接字选项的值
# getsockopt(level, optname[, buflen])	返回套接字选项的值
# settimeout(value)	设置套接字操作的超时时间，单位是秒
# gettimeout()	返回当前超时时间
# fileno()	返回套接字的文件描述符
# setblocking(flag)	如果 flag 为 0，则将套接字设为非阻塞模式，否则将套接字设为阻塞模式（默认值）；非阻塞模式下，如果调用 recv() 没有发现任何数据或 send() 调用无法立即发送数据，那么将引起 socket.error 异常
# makefile()	创建一个与该套接字相关连的文件


# 2.2 TCP 方式
# 我们来看一下如何通过 socket 以 TCP 方式进行通信。
#
# 服务端基本思路：
#
# 创建套接字，绑定套接字到 IP 与端口
#
# 监听连接
#
# 不断接受客户端的连接请求
#
# 接收请求的数据，并向对方发送响应数据
#
# 传输完毕后，关闭套接字
#
# 具体代码实现如下：




'''
项目:代码实例
文件名:01-tcp客户端程序开发
制作人:"黄涛"
date:2022/3/29
'''
import socket
# 图片转字符画.创建客户端套接字
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.和服务端套接字建立连接
tcp_client_socket.connect(('192.168.0.102', 7000))
# 3.发送数据
tcp_client_socket.send("你好，我是客户端阿白".encode('utf-8'))
# 4.接收数据
# 接收数据, 这次接收的数据最大字节数是1024
recv_data = tcp_client_socket.recv(1024)
# 返回的是二进制数据
# 对其进行解码并打印
recv_content = recv_data.decode('utf-8')
print("接收服务端的数据为:", recv_content)
# 5.关闭客户端套接字
tcp_client_socket.close()
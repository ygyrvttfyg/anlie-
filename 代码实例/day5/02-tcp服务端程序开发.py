'''
项目:代码实例
文件名:02-tcp服务端程序开发
制作人:"黄涛"
date:2022/3/29
'''
import socket
# 图片转字符画.创建服务端套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置端口号复用的代码:
# 参数1: 表示当前套接字
# 参数2: 设置端口号复用选项
# 参数3: 设置端口号复用选项对应的值
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

# 2.绑定端口号
tcp_server_socket.bind(('', 9000))

# 3.设置监听
tcp_server_socket.listen(20)
# 括号里的参数表示最大等待建立连接的个数

# 4.等待客户端的连接请求
# 等待客户端建立连接的请求, 只有客户端和服务端建立连接成功代码才会解阻塞，代码才能继续往下执行
# 每次客户端和服务端连接成功都会返回一个新的套接字和客户端的ip，端口号
# tcp_server_socket只负责接收客户端的请求，收发数据使用返回的套接字
new_client, ip_port = tcp_server_socket.accept()
print('客户端的数据为：', ip_port)

# 5.接受客户端的数据
recv_data = new_client.recv(1024)
# 获取数据的长度
recv_data_length = len(recv_data)
print("接收数据的长度为:", recv_data_length)
# 对二进制数据进行解码
recv_content = recv_data.decode('gbk')
print("接收客户端的数据为:", recv_content)

# 6.发送数据到客户端
send_data = "ok, 问题正在处理中...".encode("gbk")
new_client.send(send_data)

# 7.关闭客户端的套接字
new_client.close()

# 8.关闭套接字
tcp_server_socket.close()
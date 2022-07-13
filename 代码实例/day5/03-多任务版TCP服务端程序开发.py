'''
项目:代码实例
文件名:03-多任务版TCP服务端程序开发
制作人:"黄涛"
date:2022/3/29
'''
import socket
import threading
# 处理客户端的请求操作函数
def handle_client_request(ip_port, new_client):
    # 循环接收客户端发送的数据
    while True:
        # 5.接受客户端的数据
        recv_data = new_client.recv(1024)
        if recv_data:
            # 获取数据的长度
            recv_data_length = len(recv_data)
            print("接收数据的长度为:", recv_data_length)
            # 对二进制数据进行解码
            recv_content = recv_data.decode('gbk')
            print("接收客户端的数据为:", recv_content, ip_port)

            # 6.发送数据到客户端
            send_data = "ok, 问题正在处理中...".encode("gbk")
            new_client.send(send_data)
        else:
            print("客户端下线了:", ip_port)
            break
    # 7.关闭客户端的套接字
    new_client.close()
# 图片转字符画.创建服务端套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置端口号复用的代码:
# 参数1: 表示当前套接字
# 参数2: 设置端口号复用选项
# 参数3: 设置端口号复用选项对应的值
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

# 2.绑定端口号
tcp_server_socket.bind(('', 9090))

# 3.设置监听, listen后的套接字是被动套接字，只负责接收客户端的连接请求
tcp_server_socket.listen(20)

while True:
    # 4.等待客户端的连接请求
    # 等待客户端建立连接的请求, 只有客户端和服务端建立连接成功代码才会解阻塞，代码才能继续往下执行
    # 每次客户端和服务端连接成功都会返回一个新的套接字和客户端的ip，端口号
    # tcp_server_socket只负责接收客户端的请求，收发数据使用返回的套接字
    new_client, ip_port = tcp_server_socket.accept()

    print("客户端连接成功:", ip_port)
    # 当客户端和服务端建立连接成功以后，需要创建一个子线程，不同子线程负责接收不同客户端的消息
    sub_tread = threading.Thread(target=handle_client_request, args=(ip_port, new_client))
    # 设置守护主线程,主线程退出，子线程销毁
    sub_tread.setDaemon(True)
    # 执行子线程
    sub_tread.start()


# 8.关闭套接字
# tcp_server_socket.close() # tcp服务端套接字可以不需要关闭，因为服务端程序需要一直运行

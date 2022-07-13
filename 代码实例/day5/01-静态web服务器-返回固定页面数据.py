'''
项目:代码实例
文件名:01-静态web服务器-返回固定页面数据
制作人:"黄涛"
date:2022/4/3
'''
import socket

if __name__ == '__main__':
    # 创建服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 设置端口号复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口
    tcp_server_socket.bind(('', 9000))
    # 设置监听
    tcp_server_socket.listen(128)
    while True:
        # 等待客户端连接
        new_client, ip_port = tcp_server_socket.accept()
        # 代码执行到此，说明连接建立成功
        recv_data = new_client.recv(4096)
        # 对数据进行解码
        recv_content = recv_data.decode('gbk')
        print(recv_content)

        # 打开文件读取文件中的数据
        with open("../web/static/index.html", "rb") as file:
            # 读取文件数据
            file_data = file.read()

        # 响应行
        response_line = "HTTP/图片转字符画.图片转字符画 200 OK\r\n"
        # 响应头
        response_header = "Server: PWS1.0\r\n"

        # 响应体
        response_body = file_data

        # 拼接响应报文
        response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
        # 发送数据
        new_client.send(response_data)
        new_client.close()
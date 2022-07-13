'''
项目:代码实例
文件名:静态Web服务器-面向对象开发
制作人:"黄涛"
date:2022/4/4
'''
import socket
import sys
import threading

# Web服务器类
class Httpwebserver(object):
    def __init__(self, port):
        # 创建服务端套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口号复用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口
        tcp_server_socket.bind(('', 9000))
        # 设置监听
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    # 处理客户端请求
    @staticmethod
    def handle_client_request(new_client):
        # 代码执行到此，说明连接建立成功
        recv_data = new_client.recv(4096)
        # 判断接受的数据是否为0
        if len(recv_data) == 0:
            print("关闭浏览器了")
            new_client.close()
            return
        # 对数据进行解码
        recv_content = recv_data.decode('gbk')
        print(recv_content)
        # 根据指定字符串进行分割， 最大分割次数指定2
        request_list = recv_content.split(" ", maxsplit=2)
        # 获取请求资源路径
        request_path = request_list[1]
        print(request_list)
        if request_path == '/':
            request_path = '/index.html'

        try:
            # 打开文件读取文件中的数据
            with open("static" + request_path, "rb") as file:
                # 读取文件数据
                file_data = file.read()
        except Exception as e:
            # 代码进行到这里，说明没有该请求的文件，返回404状态信息
            # 响应行
            response_line = "HTTP/图片转字符画.图片转字符画 404 NOT FOUND\r\n"
            # 响应头
            response_header = "Server: PWS1.0\r\n"
            with open('static/error.html', 'rb') as f:
                file_data = f.read()
            # 拼接响应报文
            response_data = (response_line + response_header + "\r\n").encode("utf-8") + file_data
            # 发送数据
            new_client.send(response_data)

        else:
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
        finally:
            # 关闭服务端与客户端的套接字
            new_client.close()
    # 启动web服务器进行工作
    def start(self):
        while True:
            # 等待客户端连接
            new_client, ip_port = self.tcp_server_socket.accept()
            # 当客户端和服务器建立连接程，创建子线程
            sub_thread = threading.Thread(target=self.handle_client_request, args=(new_client,))
            # 设置守护主线程
            sub_thread.setDaemon(True)
            # 启动子线程执行对应的任务
            sub_thread.start()


def main():
    # 判断命令行参数是否等于2,
    if len(sys.argv) != 2:
        print("执行命令如下: python3 xxx.py 8000")
        return

    # # 判断字符串是否都是数字组成
    if not sys.argv[1].isdigit():
        print("执行命令如下: python3 xxx.py 8000")
        return
    # 获取终端命令行参数
    port = int(sys.argv[1])
    # 创建web服务器对象
    webserver = Httpwebserver(port)
    # 启动web服务器
    webserver.start()

if __name__ == '__main__':
    main()

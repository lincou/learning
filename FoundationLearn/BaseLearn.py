import socket

def start_server():
    # 创建一个TCP/IP套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定到地址和端口
    server_address = ('localhost', 65432)  # 本地地址和端口
    server_socket.bind(server_address)

    # 启动监听
    server_socket.listen(1)
    print("服务器启动，等待客户端连接...")

    while True:
        # 等待客户端连接
        connection, client_address = server_socket.accept()
        try:
            print(f"连接来自 {client_address}")

            # 接收数据
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                print(f"接收到数据: {data.decode()}")
                # 发送数据回客户端
                connection.sendall(data)

        finally:
            connection.close()

if __name__ == "__main__":
    start_server()

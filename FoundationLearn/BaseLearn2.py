import socket

def start_client():
    # 创建一个TCP/IP套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接到服务器
    server_address = ('localhost', 65432)  # 本地地址和端口
    client_socket.connect(server_address)

    try:
        # 发送数据
        while True:
            message = input("请输入要发送的消息: ")
            if message == "exit" or message == "-1":
                print("退出发送。")
                break  # 退出循环
            print(f"发送数据: {message}")
            client_socket.sendall(message.encode())
            # 接收数据
            data = client_socket.recv(1024)
            print(f"接收到来自服务器的数据: {data.decode()}")
            

    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()

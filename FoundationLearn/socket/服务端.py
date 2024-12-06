import socket
import hashlib

AUTH_KEY = "123456"

def hash_key(key):
    return hashlib.sha256(key.encode('utf-8')).hexdigest()

def start_server():
    # 创建一个TCP/IP套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定到地址和端口
    server_address = ('localhost', 65535)  # 本地地址和端口
    server_socket.bind(server_address)

    # 启动监听
    server_socket.listen(5)
    print("服务器启动，等待客户端连接...")

        # 等待客户端连接       
    client_socket, addr = server_socket.accept()
    print(f"连接来自: {addr}")

    # 接收身份验证请求
    received_auth = client_socket.recv(1024).decode('utf-8')
    print(f"接收到的身份验证密钥: {received_auth}")

    # 验证身份
    if received_auth == hash_key(AUTH_KEY):
        print("身份验证成功，开始通信...")
        client_socket.send("身份验证成功".encode('utf-8'))
    else:
        print("身份验证失败，关闭连接。")
        client_socket.send("身份验证失败".encode('utf-8'))
        client_socket.close()

        # 此处可以添加后续的消息交流逻辑
        # 例如接收和响应客户端的消息
    while True:
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

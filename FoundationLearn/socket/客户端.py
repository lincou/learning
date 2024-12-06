import socket
import hashlib

AUTH_KEY = "1234567"

def hash_key(key):
    return hashlib.sha256(key.encode('utf-8')).hexdigest()


def start_client():
    # 创建一个TCP/IP套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接到服务器
    server_address = ('localhost', 65535)  # 本地地址和端口
    client_socket.connect(server_address)
    # 发送身份验证密钥
    auth_hash = hash_key(AUTH_KEY)
    client_socket.send(auth_hash.encode('utf-8'))

    # 接收服务器的身份验证响应
    response = client_socket.recv(1024).decode('utf-8')
    print(f"服务器响应: {response}")

    if response == "身份验证成功":
        # 进行后续的消息交流
        # 例如发送和接收其他数据
        print("可以进行后续的通信。")
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
    else:
        print("身份验证失败。")
        print("关闭连接。")
        client_socket.close()

if __name__ == "__main__":
    start_client()

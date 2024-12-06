import socket
import hashlib

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # 发送身份验证信息的哈希
    username = "admin1"
    password = "123456"
    hash_value = generate_hash(username, password)
    client_socket.sendall(hash_value.encode())

    response = client_socket.recv(1024).decode()
    print(response)

    if "成功" in response:
        # 进行数据通信
        while True:
            message = input("请输入要发送的消息（输入'exit'退出）：")
            if message.lower() == 'exit':
                break
            client_socket.sendall(message.encode())
            response = client_socket.recv(1024).decode()
            print(response)

    client_socket.close()

def generate_hash(username, password):
    # 使用SHA-256生成身份验证哈希
    combined = f"{username}:{password}".encode()
    return hashlib.sha256(combined).hexdigest()

if __name__ == "__main__":
    start_client()

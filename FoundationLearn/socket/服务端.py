import socket
import hashlib

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("服务器启动，等待连接...")

    conn, addr = server_socket.accept()
    print(f"连接来自: {addr}")

    # 身份验证
    received_hash = conn.recv(1024).decode()
    username = "admin"
    password = "123456"
    expected_hash = generate_hash(username, password)

    if received_hash == expected_hash:
        conn.sendall("身份验证成功！\n".encode())
        # 进行数据通信
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"收到消息： {data.decode()}")
            response = f"服务器收到您的消息: '{data.decode()}'"
            conn.sendall(response.encode())
    else:
        print("身份验证失败！\n")
        conn.sendall("身份验证失败！\n".encode())

    conn.close()
    server_socket.close()

def generate_hash(username, password):
    # 使用SHA-256生成身份验证哈希
    combined = f"{username}:{password}".encode()
    return hashlib.sha256(combined).hexdigest()

if __name__ == "__main__":
    start_server()

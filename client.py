import socket

# ① 클라이언트 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ② 서버의 IP와 포트 지정
HOST = '127.0.0.1'  # 같은 PC 내 서버
PORT = 5000         # 서버와 같은 포트

client_socket.connect((HOST, PORT))
print(f"🌟 서버({HOST}:{PORT})에 연결되었습니다.")

# ③ 메시지 전송
message = "안녕하세요, 서버님!"
client_socket.sendall(message.encode())
print(f"📤 서버로 전송: {message}")

# ④ 서버 응답 수신
data = client_socket.recv(1024).decode()
print(f"📥 서버 응답: {data}")

# ⑤ 연결 종료
client_socket.close()

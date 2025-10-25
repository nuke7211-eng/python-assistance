import socket

# ① 서버 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ② IP와 포트 설정
HOST = '127.0.0.1'  # 자기 자신(로컬)
PORT = 5000         # 당신이 정한 포트 번호

server_socket.bind((HOST, PORT))  # IP와 포트를 소켓에 바인딩
server_socket.listen()            # 연결 대기 상태로 전환
print(f"🌐 서버가 {PORT}번 포트에서 대기 중입니다...")

# ③ 클라이언트 연결 수락
client_socket, addr = server_socket.accept()
print(f"🔗 클라이언트 접속: {addr}")

# ④ 데이터 수신
data = client_socket.recv(1024).decode()
print(f"📩 클라이언트로부터 받은 메시지: {data}")

# ⑤ 응답 전송
reply = "서버가 잘 받았습니다. 반가워요!"
client_socket.sendall(reply.encode())

# ⑥ 소켓 닫기
client_socket.close()
server_socket.close()
print("🚪 서버 종료")

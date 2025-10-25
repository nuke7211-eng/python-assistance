import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))  # IP와 포트 지정 (여기서 5000이 포트 번호)
server.listen()

print("서버가 5000번 포트에서 대기 중입니다...")

conn, addr = server.accept()
print("클라이언트 연결:", addr)



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))  # 서버의 IP와 포트
client.sendall(b"안녕하세요, 서버님!")

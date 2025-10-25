import subprocess

def show_open_ports(port=None):
    try:
        # 기본 명령어
        cmd = ['netstat', '-ano']

        # 특정 포트를 지정했다면 필터 추가
        if port:
            cmd = ['netstat', '-ano', '|', 'findstr', str(port)]
            print(f"\n🔍 {port}번 포트를 사용하는 프로그램 찾는 중...\n")
        else:
            print("\n🌐 현재 열려 있는 포트 목록을 불러오는 중...\n")

        # 명령 실행
        result = subprocess.run(' '.join(cmd), shell=True, capture_output=True, text=True)
        print(result.stdout if result.stdout else "⚠️ 열려 있는 포트가 없습니다.")

    except Exception as e:
        print("🚫 오류 발생:", e)


def find_process_by_pid(pid):
    try:
        print(f"\n🔎 PID {pid}를 사용하는 프로그램 찾는 중...\n")
        cmd = f'tasklist | findstr {pid}'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(result.stdout if result.stdout else "⚠️ 해당 PID를 찾을 수 없습니다.")
    except Exception as e:
        print("🚫 오류 발생:", e)


if __name__ == "__main__":
    print("🌟 포트 탐색 마법사 🌟")
    print("1️⃣ 모든 포트 보기")
    print("2️⃣ 특정 포트로 검색")
    print("3️⃣ PID로 프로그램 찾기\n")

    choice = input("원하는 기능을 선택하세요 (1/2/3): ")

    if choice == '1':
        show_open_ports()
    elif choice == '2':
        port = input("검색할 포트번호를 입력하세요: ")
        show_open_ports(port)
    elif choice == '3':
        pid = input("검색할 PID를 입력하세요: ")
        find_process_by_pid(pid)
    else:
        print("⚠️ 올바른 선택이 아닙니다.")

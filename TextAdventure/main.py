def start_game():
    print("환영합니다! 간단한 텍스트 어드벤처 게임에 오신 것을 환영합니다.")
    print("당신은 어두운 숲 속에 서 있습니다. 앞으로 갈 방향을 선택하세요.")
    choice = input("1. 북쪽으로 간다\n2. 남쪽으로 간다\n> ")

    if choice == "1":
        print("북쪽으로 가다가 늑대를 만났습니다. 게임 오버!")
    elif choice == "2":
        print("남쪽으로 가다가 보물을 발견했습니다. 승리!")
    else:
        print("잘못된 선택입니다. 게임을 종료합니다.")

if __name__ == "__main__":
    start_game()

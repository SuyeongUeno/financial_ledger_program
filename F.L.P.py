#시작 금액
balance = 0
balance_0 = balance

#리스트
main = []

while True:
    print("====메뉴====")
    print("1. 입금")
    print("2. 출금")
    print("3. 잔액 보기")
    print("4. 거래 내역 보기")
    print("5. 종료")

    menu = input("메뉴를 선택하세요.")
#입금
    from datetime import datetime

    if menu == "1":    
        deposit = int(input("수익: "))
        N = datetime.today().strftime("%Y-%m-%d")
        balance += deposit
        main.append(["입금", deposit, balance, N])
        print("입금 완료!")

#출금
    elif menu =="2":
        withdraw = int(input("지출: "))
        if withdraw > balance:
            print("잔액 부족")
        else:
            N = datetime.today().strftime("%Y-%m-%d")
            balance -= withdraw
            main.append(["출금", withdraw, balance, N])
            print("출금 완료!")

#잔액 확인
    elif menu == "3":
        print("현재 잔액:", balance, "원")

#거래 내역
    elif menu == "4":
        for item in main:
            print(item)

#종료
    elif menu == "5":
        print("프로그램 종료.")
        break

#잘못된 메뉴 번호
    else:
        print("올바른 번호를 입력하세요.")
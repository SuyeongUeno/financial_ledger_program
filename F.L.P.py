#시작 금액
balance = 0
balance_0 = balance

#입금 금액
deposit = int(input("수익: "))

#출금 금액
withdraw = int(input("지출: "))

#작성일
N = str(input("작성일: "))

#입금
balance_1 = balance + deposit
balance += deposit

#출금
balance_2 = balance_1 - withdraw
balance -= withdraw

#리스트
main = []

#입금 거래 내역
deposit_list = ["입금",
                      "원금: " + str(balance_0) + "원",
                      (str(deposit) + "원"),
                      (str(balance_1) + "원"),
                      N]
main.append(deposit_list)

#출금 거래 내역
withdraw_list = ["출금",
                       "원금: " + str(balance_1) + "원",
                       (str(withdraw) + "원"),
                       (str(balance_2) + "원"),
                       N]
main.append(withdraw_list)
balance_0 = balance_2

#출력
print("===거래 내역===")
print("잔액: " + str(balance) + "원")
print(main[0][0],main[0][1],main[0][2],main[0][3],main[0][4])
print(main[1][0],main[1][1],main[1][2],main[1][3],main[1][4])
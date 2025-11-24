# Personal Finance Ledger – Python CLI Application  
### version_0.9.0  
📅 First created: 2025-11-23  
📅 Last updated: 2025-11-24

---

## 🚀 What’s New in version_0.9.0

This update introduces the first fully interactive CLI version of the ledger.

### ✔ Added Features  
- Added a menu-driven interface  
  - Deposit  
  - Withdraw  
  - Check current balance  
  - View transaction history  
  - Exit program  
- Transactions now support **multiple inputs** through a continuous loop (`while True`)
- Each transaction is recorded with:
  - Type (Deposit / Withdraw)
  - Amount  
  - Updated balance  
  - Date (entered by user)

### ✔ Improved Structure  
- Previous Version_0.8.0 one-time execution system removed  
- Replaced with a persistent loop that allows continuous operations  
- Data structure unified under a single `main` list  

### ✔ Version Tag  
This project is still in development and does not save data externally.  
Version_1.0.0 will be released when persistent file storage is added.

---

## 📌 Overview
Personal Finance Ledger is a Python-based CLI application that records income and expenses and automatically calculates updated balances.  
It was built to practice core Python fundamentals including input handling, arithmetic operations, list data structure usage, and console output formatting.

The program receives:
- Income amount
- Expense amount
- Date of transaction

Then it outputs:
- Updated balance
- Deposit and withdrawal history
- Original balance and post-transaction balance for each activity

---

## 🛠️ Tech Stack / Concepts Used
- Python 3
- Console-based user input (`input`)
- Variables & arithmetic operators
- List data structure
- String formatting

---

## ▶️ How to Run
```bash
python3 account_book_v1.py
```

---

## 🧾 Example Output (Text)

```text
====메뉴====
1. 입금
2. 출금
3. 잔액 보기
4. 거래 내역 보기
5. 종료
```

---

## 🚀 Future Improvements

Planned upgrades that will be applied through continued learning:

- Multiple transaction inputs (not limited to a single income and expense)
- Menu system with condition selection (deposit / withdrawal / view balance / view history / exit)
- Loop-based continuous execution instead of a single run
- Save and load transaction history from a file (CSV / JSON / TXT)

---

## 📌 Project Roadmap
Development is continually tracked and updated through the GitHub Project board.

🔗 Roadmap: https://github.com/<USERNAME>/<REPO>/projects/1

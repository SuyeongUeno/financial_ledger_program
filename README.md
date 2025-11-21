# Personal Finance Ledger – Python CLI Application
### version_0.8.0  
📅 First created: 2025-11-23

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

## 🧾 Example Output (Text)
===거래 내역===
잔액: 30000원
입금 원금: 0원 50000원 50000원 2025-11-23
출금 원금: 50000원 20000원 30000원 2025-11-23

## 🚀 Future Improvements

Planned upgrades that will be applied through continued learning:

Multiple transaction inputs (not limited to a single income and expense)

Menu system with condition selection (deposit / withdrawal / view balance / view history / exit)

Loop-based continuous execution instead of a single run

Save and load transaction history from a file (CSV / JSON / TXT)
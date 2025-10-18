# 🏦 Bank Account Simulator
# This Java project simulates a simple banking system with accounts, deposits, withdrawals,
# interest application, and transaction history.

# Features:
# 1. Each Account has:
#    - accountNumber : unique identifier
#    - accountHolder : name of the owner
#    - balance       : current account balance
#    - transactions  : a list of past deposits, withdrawals, and interest applied
#
# 2. Deposits: add money to the account
# 3. Withdrawals: remove money if sufficient balance exists
# 4. Interest Application: apply a monthly interest rate to the balance
# 5. Transaction History: print all actions on the account

# Example Usage:
#
# Account acc = new Account("12345", "Nour Bh", 1000.0)
# acc.deposit(500.0)             # Adds 500 to balance
# acc.withdraw(200.0)            # Subtracts 200 if enough balance
# acc.applyInterest(0.02)        # Applies 2% interest
# acc.printTransactions()        # Prints all deposits, withdrawals, and interest applied
#
# Expected Output:
#
# Deposit: +500.0, Balance: 1500.0
# Withdrawal: -200.0, Balance: 1300.0
# Interest Applied: +26.0, Balance: 1326.0

# Notes:
# - The project uses OOP principles: classes, objects, methods, and encapsulation
# - Transactions are stored using an ArrayList
# - Can be extended with multiple accounts, bank-level operations, fees, etc.
# - Strong typing ensures no invalid data can corrupt the account

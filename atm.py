"""-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[✅] 1. Header Docstring included with assignment info.
[✅] 2. ATM runs in a "while True" loop to remain awake.
[✅] 3. Main menu uses match-case logic for selections.
[✅] 4. Inputs are validated (e.g., .isdigit()) to prevent crashes (include try except)
[✅] 5. Logic prevents overdrafts and negative deposits.
[✅] 6. All currency is formatted to two decimal places (:.2f).
[✅] 7. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------"""

# 📦 Imports-----------------------------------------------------------
import time
import os
from datetime import datetime


def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")


os.system("cls") if os.name == "nt" else os.system("clear")

# ----------------------------------------------------------------------
bal = 1000.00
atm = True
local_now = datetime.now()
date = local_now.strftime("%A, %B %d, %Y")

while True:
    try:
        print(f"{date}")
        print(f"\tMENU:\n1.Balance\n2.Deposit\n3.Withdraw\n4.Transfer\n5.Exit")
        menu_ans = int(input(": "))

        while menu_ans > 0 and menu_ans < 5:
            match menu_ans:

                # 1 Balance
                case 1:
                    clear()
                    print(f"Balance: ${bal:,.2f}\n")
                    time.sleep(1)
                    con = input("press enter to return")
                    if con == "":
                        clear()
                        menu_ans = 0

                # 2 Deposit
                case 2:
                    clear()
                    print(f"Current balance: ${bal:,.2f}")
                    try:
                        deposit = float(input(f"Please specify amount to deposit: "))
                        if deposit < 1:
                            clear()
                            print("Error: must be more than 0")
                            time.sleep(3)
                            clear()
                        elif deposit > 0:
                            clear()
                            bal = bal + deposit
                            print(f"Deposited.\nNew balance: ${bal:,.2f}")
                            time.sleep(1)
                            con = input(f"\npress enter to return")
                            if con == "":
                                clear()
                                menu_ans = 0
                    except ValueError:
                        clear()
                        print("Error: please specify deposit amount in # form.")
                        time.sleep(3)
                        clear()

                # 3 Withdraw
                case 3:
                    clear()
                    print(f"Current balance: ${bal:,.2f}")
                    try:
                        withdraw = float(input(f"Please specify amount to withdraw: "))
                        if withdraw < 1:
                            clear()
                            print("Error: must be more than 0")
                            time.sleep(3)
                            clear()
                        elif withdraw > bal:
                            clear()
                            print("Error: cant withdraw more than current balance.")
                            time.sleep(3)
                            clear()
                        elif withdraw > 0:
                            clear()
                            bal = bal - withdraw
                            print(f"Withdrawn.\nNew balance: ${bal:,.2f}")
                            time.sleep(1)
                            con = input(f"\npress enter to return")
                            if con == "":
                                clear()
                                menu_ans = 0
                    except ValueError:
                        clear()
                        print("Error: please specify withdraw amount in # form.")
                        time.sleep(3)
                        clear()

                # 4 Transfer
                case 4:
                    clear()
                    print(f"Current balance: ${bal:,.2f}")
                    try:
                        receiver = input("Please enter account to transfer to: ")
                        sending = float(input(f"\nPlease enter amount to transfer: "))
                        if sending < 1:
                            clear()
                            print("Error: must be more than 0")
                            time.sleep(3)
                            clear()
                        elif sending > bal:
                            clear()
                            print("Error: cant transfer more than current balance.")
                            time.sleep(3)
                            clear()
                        elif sending > 0:
                            clear()
                            bal = bal - sending
                            print(
                                f"Transfered ${sending:,.2f} to {receiver}.\nNew balance: ${bal:,.2f}"
                            )
                            time.sleep(1)
                            con = input(f"\npress enter to return")
                            if con == "":
                                clear()
                                menu_ans = 0
                    except ValueError:
                        clear()
                        print(
                            "Error: please specify Transfer amount in # form and name of account to tranfer."
                        )
                        time.sleep(3)
                        clear()

                # 5 Exit
        if menu_ans == 5:
            clear()
            print("Goodbye...")
            time.sleep(3)
            clear()
            blank = input("")
        clear()
    except ValueError:
        clear()
        print("Error: please select option in # form.")
        time.sleep(3)
        clear()

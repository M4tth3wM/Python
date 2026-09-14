"""-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. All 4 inputs have 'while' loop validation.
[✅] 3. The Chaperone loop uses .upper() and correct Boolean logic.
[✅] 4. I have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------"""

# 📦 Imports-----------------------------------------------------------
import time
import os

os.system("cls") if os.name == "nt" else os.system("clear")

# ----------------------------------------------------------------------
user_name = input("Enter first & last name: ")
while user_name == "":
    print("❌ Error: Name cannot be blank")
    user_name = input("Enter first & last name: ")
print(f"\n Name: {user_name}\n")
time.sleep(1)
os.system("cls") if os.name == "nt" else os.system("clear")

chaperone = input("Volunteering chaperone? (Y/N): ").upper()
while chaperone != "Y" and chaperone != "N":
    print("❌ Error: Please enter Y or N")
    chaperone = input("Volunteering chaperone? (Y/N): ").upper()
print(f"\n Chaperone present: {chaperone}\n")
time.sleep(1)
os.system("cls") if os.name == "nt" else os.system("clear")

phone_num = input("Enter phone number: ")
while phone_num == "":
    print("❌ Error: Phone number cannot be blank")
    phone_num = input("Enter phone number: ")
print(f"\n Phone number: {phone_num}\n")
time.sleep(1)
os.system("cls") if os.name == "nt" else os.system("clear")

tickets = 0
while True:
    try:
        tickets = int(input("How many tickets?: "))
        if tickets > 0:
            break
        print("❌ Error: Must be at least 1 ticket")
    except ValueError:
        print("❌ Error: Please enter a number that must be an integer")
print(f"\n Tickets purchased: {tickets}\n")
time.sleep(1)
os.system("cls") if os.name == "nt" else os.system("clear")

"""Results"""

print(f"Name: {user_name}\n")
time.sleep(0.5)

if chaperone == "Y":
    print(f"Chaperone present: True\n")
elif chaperone == "N":
    print(f"Chaperone present: False\n")
time.sleep(0.5)

print(f"Phone number: {phone_num}\n")
time.sleep(0.5)

print(f"Tickes purchased: {tickets}")

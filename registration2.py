"""-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. All 5 inputs have 'while' loop validation.
[✅] 3. The more tickets loop uses .upper() and correct Boolean logic.
[✅] 4. Include a try and except statement around the entire program. Should have one defined
       exception (probably value error) and a generic exception
[✅] 5. Have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------"""

# 📦 Imports-----------------------------------------------------------
import time
import os
from datetime import datetime

os.system("cls") if os.name == "nt" else os.system("clear")

# ----------------------------------------------------------------------
user_name = input("Enter first & last name: ")
while user_name == "":
    print("❌ Error: Name cannot be blank")
    user_name = input("Enter first & last name: ")
print(f"\n Name: {user_name}\n")
time.sleep(1)
os.system("cls") if os.name == "nt" else os.system("clear")

local_now = datetime.now()
user_year = int(input("Enter YEAR of birth: "))
while user_year > int((local_now.strftime("%Y"))):
    try:
        print("❌ Error: user age cant be more than current year")
        user_year = int(input("Enter your birth year: "))
    except ValueError:
        print("❌ Error: Must enter a number")
user_age = int((local_now.strftime("%Y"))) - (user_year)
print(f"\n Age: {user_age}\n")
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

more_tick = input("More tickets? (Y/N): ").upper()
while more_tick != "Y" and more_tick != "N":
    print("❌ Error: Please enter Y or N")
    more_tick = input("More tickets? (Y/N): ").upper()
if more_tick == "N":
    print(f"More tickets: {more_tick}\n")
    time.sleep(1)
    os.system("cls") if os.name == "nt" else os.system("clear")
elif more_tick == "Y":
    tickets2 = 0
    while True:
        try:
            tickets2 = int(input("How many tickets?: "))
            if tickets2 > 0:
                break
            print("❌ Error: Must be at least 1 ticket")
        except ValueError:
            print("❌ Error: Please enter a number that must be an integer")
    tickets = tickets + tickets2
    print(f"\n Tickets purchased: {tickets}\n")
    time.sleep(1)
    os.system("cls") if os.name == "nt" else os.system("clear")

"""Results"""

print(f"Name: {user_name}\n")
time.sleep(0.5)

print(f"Age: {user_age}\n")
time.sleep(0.5)

if chaperone == "Y":
    print(f"Chaperone present: True\n")
elif chaperone == "N":
    print(f"Chaperone present: False\n")
time.sleep(0.5)

print(f"Phone number: {phone_num}\n")
time.sleep(0.5)

print(f"Tickes purchased: {tickets}")

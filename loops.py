"""-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. Task 1: While Loop (The Nagging Kid)
        - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[✅] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[✅] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------"""

# 📦 Imports-----------------------------------------------------------
import time
import os

# ----------------------------------------------------------------------

os.system("cls") if os.name == "nt" else os.system("clear")

# ℹ️ Variables---------------------------------------------------------
nagging = True
bottles = 99
# ----------------------------------------------------------------------

# ✖️🖨️ Logic/Prints----------------------------------------------------
print(f"\tGoing for a drive...\n")
time.sleep(1)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while nagging:
    print("Are we there yet?")
    answer = input(":")
    if answer == "yes":
        nagging = False
        asking = True
        print("YAY!...")
        time.sleep(2.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
    elif answer == "Yes":
        nagging = False
        asking = True
        print("YAY!...")
        time.sleep(2.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
    elif answer == "y":
        nagging = False
        asking = True
        print("YAY!...")
        time.sleep(2.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
    elif answer == "Y":
        nagging = False
        asking = True
        print("YAY!...")
        time.sleep(2.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
    else:
        time.sleep(0.5)
        os.system("cls") if os.name == "nt" else os.system("clear")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ❗I did sit through all of the beer wall to see if it worked correctly

while asking:
    answer2 = input("\tPart 2 (y/n)")

    if answer2 == "y":
        asking = False
        time.sleep(0.5)
        os.system("cls") if os.name == "nt" else os.system("clear")

        for i in range(99, 0, -1):

            if bottles > 1:
                print(f"{bottles} bottles of beer on the wall~\n")
                time.sleep(1)
                print(f"{bottles} bottles of beeeeer~\n")
                time.sleep(1)
                print("Take one down~\n")
                time.sleep(0.5)
                print("Pass it around~\n")
                time.sleep(0.5)
                bottles = int(bottles - 1)
                print(f"{bottles} bottles of beer on the wall~")
                time.sleep(1.5)
                os.system("cls") if os.name == "nt" else os.system("clear")

            elif bottles == 1:
                print(f"{bottles} bottle of beer on the wall~\n")
                time.sleep(1)
                print(f"{bottles} bottle of beeeeer~\n")
                time.sleep(1)
                print("Take one down~\n")
                time.sleep(0.5)
                print("Pass it around~\n")
                time.sleep(0.5)
                bottles = int(bottles - 1)
                print(f"{bottles} bottles of beer on the wall~")
                time.sleep(1.5)
                os.system("cls") if os.name == "nt" else os.system("clear")
        print(f"{bottles} bottles of beer on the wall~")

    elif answer2 == "n":
        asking = False
        print("You drive past the bar...")
        time.sleep(1)
        print("Really...")
        time.sleep(1.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
        asking = True

# 💬 Final comments----------------------------------------------------
"""Almost forgot to make it non-plural when it reaches 1 on bottles of beer"""
# ----------------------------------------------------------------------

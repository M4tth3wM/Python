"""-----------------------------------------------------------------------
ASSIGNMENT 6B: THE LOCKED CALENDAR
-----------------------------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. MONTHS is defined as a constant tuple ().
[✅] 3. Program uses a for loop to display each month.
[✅] 4. 'try' and 'except' blocks catch a TypeError.
[✅] 5. Comments explain why the modification failed.
-----------------------------------------------------------------------"""

# 📦 Imports-----------------------------------------------------------
import time
import os


def clr():
    os.system("cls") if os.name == "nt" else os.system("clear")


os.system("cls") if os.name == "nt" else os.system("clear")
# ----------------------------------------------------------------------

# 📝 Lists-------------------------------------------------------------
MONTHS = (
    "January",
    "Febuary",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)
# ----------------------------------------------------------------------

# 🖨️ Prints/MainCode----------------------------------------------------
cal = True
while cal:
    try:

        print(f"\tMonths of the year:")
        for month in MONTHS:
            print(month)
            time.sleep(0.025)

        # 5 attempts to change something in calender
        change = input()
        clr()
        MONTHS.append(change)
        MONTHS.remove("January")
        MONTHS.pop()
        MONTHS = change
        MONTHS = ("Buaray ", "doofuary")
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # failed attempt to change because of tuple
    except AttributeError:
        clr()
        print("doesnt except changes.")
        time.sleep(3)
        clr()
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

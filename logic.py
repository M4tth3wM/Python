"""-----------------------------------------------------------------------
[✅] 1. Header Docstring included with assignment title.
[✅] 2. Ask user for two integers (num1 and num2).
[✅] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[✅] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[✅] 5. Code is clean and uses descriptive variable names.
[✅] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------"""

# 📦 Imports-----------------------------------------------------------
import time
import os

# ----------------------------------------------------------------------

os.system("cls") if os.name == "nt" else os.system("clear")

# ℹ️ Variables---------------------------------------------------------
num1 = float(input("Input a number: "))
num2 = float(input("Input a second number: "))
# ----------------------------------------------------------------------

time.sleep(0.5)
os.system("cls") if os.name == "nt" else os.system("clear")

# ➕🖨️ Calculations/Prints---------------------------------------------
if num1 > 0:
    print(f"{num1:,} is bigger than 0")
elif num1 == 0:
    print(f"{num1:,} is equal to 0")
elif num1 < 0:
    print(f"{num1:,} is lower than 0")
# ~~~~~~~~~~~~~~~
if num2 > 0:
    print(f"{num2:,} is bigger than 0")
elif num1 == 0:
    print(f"{num2:,} is equal to 0")
elif num2 < 0:
    print(f"{num2:,} is lower than 0")
# ~~~~~~~~~~~~~~~
if num1 > 100:
    print(f"\n{num1:,} is bigger than 100")
elif num1 == 100:
    print(f"\n{num1:,} is equal to 100")
elif num1 < 100:
    print(f"\n{num1:,} is lower than 100")
# ~~~~~~~~~~~~~~~
if num2 > 100:
    print(f"{num2:,} is bigger than 100")
elif num1 == 100:
    print(f"{num2:,} is equal to 100")
elif num2 < 100:
    print(f"{num2:,} is lower than 100")
# ~~~~~~~~~~~~~~~
if num1 % 2 == 0:
    print(f"\n{num1:,} is even")
else:
    print(f"\n{num1:,} is odd")
# ~~~~~~~~~~~~~~~
if num2 % 2 == 0:
    print(f"{num2:,} is even")
else:
    print(f"{num2:,} is odd")
# ~~~~~~~~~~~~~~~
if num1 == num2:
    print(f"\n{num1:,} is equal to {num2:,}")
else:
    print(f"\n{num1:,} is not equal to {num2:,}")
# ----------------------------------------------------------------------

# 💬 Final comments----------------------------------------------------
"""No major comments"""
# ----------------------------------------------------------------------

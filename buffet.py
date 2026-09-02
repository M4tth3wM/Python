"""-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator (Daily Specials)
DATE: [09/02/26]
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask the user for their age (convert to int) and the day of the week (convert to string).
2. Calculate the base price using if/elif/else:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Use a match/case statement to handle special daily rules based on the day entered:
   - Tuesday: Children through age 12 are half price!
   - Sunday: Drinks are free!
   - Other days: Standard buffet pricing in effect.
4. Print the final price formatted as currency and display any applicable daily special notices.
-----------------------------------------------------------------------"""

# 📦 Imports-----------------------------------------------------------
import time
import os

# ----------------------------------------------------------------------

os.system("cls") if os.name == "nt" else os.system("clear")

# ℹ️ Variables---------------------------------------------------------
user_age = int(input("What is your age?: "))
week_day = input(
    "What day of the week is it? (please spell it out full with lowercase): "
)
price = 0.00
# ----------------------------------------------------------------------

print("\nThank you for your input...")
time.sleep(1)
os.system("cls") if os.name == "nt" else os.system("clear")

# ✖️ Logic-------------------------------------------------------------
if user_age < 1:
    price = float(0.00)
elif user_age >= 1 and user_age <= 11 and week_day == "tuesday":
    price = float(user_age * 1.00 / 2)
elif user_age >= 1 and user_age <= 11:
    price = float(user_age * 1.00)
elif user_age == 12 and week_day == "tuesday":
    price = float(16.95 / 2)
elif user_age >= 12 and user_age <= 64:
    price = float(16.95)
elif user_age >= 65:
    price = float(12.95)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
def day_effect(week_day):
    match week_day.lower():
        case "tuesday":
            return "Children through age 12 are half price!"
        case "sunday":
            return "Drinks are free!"
        case _:
            return "Standard buffet pricing in effect."


# ----------------------------------------------------------------------

# 🖨️ Prints-------------------------------------------------------------
print(f"Age: {user_age}")
print(f"Day of the week: {week_day}\n")
time.sleep(0.5)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(day_effect(week_day))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
time.sleep(0.5)
print(f"Total: \033[4m${price:,.2f}\033[0m\n\n")
# ----------------------------------------------------------------------

# 💬 Final comments----------------------------------------------------
"""Had some trouble with the Match/Case commands and didnt quite know if I did it correctly but tried my best. tried to also make it look clean but I couldnt quite get your answer on how to do the (import time lines) loop thing correctly and I'll be testing it on my own time to figure it out. learned how to underline text from searching on my own"""
# ----------------------------------------------------------------------

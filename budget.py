"""-----------------------------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. Ask user for Monthly Income (float).
[✅] 3. Ask user for 5 DIFFERENT expense amounts (float).
[✅] 4. Calculate Total Expenses and Remaining Balance.
[✅] 5. Calculate Percentage of Income Spent.
[✅] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------"""

# 📦 Imports-----------------------------------------------------------
import time
import os

# ----------------------------------------------------------------------

os.system("cls") if os.name == "nt" else os.system("clear")

# ℹ️ Variables---------------------------------------------------------
monthly = float(input("Monthly Income($): "))
rent = float(input("Rent($): "))
water_bill = float(input("Water bill($): "))
gas_bill = float(input("Gas bill($): "))
electric_bill = float(input("Electric bill($): "))
groceries = float(input("Groceries($): "))
# ----------------------------------------------------------------------

os.system("cls") if os.name == "nt" else os.system("clear")

# ➕ Calculations------------------------------------------------------
expense_total = rent + water_bill + gas_bill + electric_bill + groceries
after_rent = monthly - rent
after_water = after_rent - water_bill
after_gas = after_water - gas_bill
after_electric = after_gas - electric_bill
after_groceries = after_electric - groceries
# ----------------------------------------------------------------------

os.system("cls") if os.name == "nt" else os.system("clear")

# 🖨️ Prints------------------------------------------------------------
print(f"Monthly: ${monthly:,.2f}")
print("---------------------------")
time.sleep(1)
print(f"Rent: ${rent:,.2f}")
time.sleep(0.25)
print(f"Water bill: ${water_bill:,.2f}")
time.sleep(0.25)
print(f"Gas bill: ${gas_bill:,.2f}")
time.sleep(0.25)
print(f"Electric bill: ${electric_bill:,.2f}")
time.sleep(0.25)
print(f"Groceries: ${groceries:,.2f}")
print("---------------------------")
time.sleep(1.5)
print(f"Expenses: ${expense_total:,.2f}")
print("---------------------------")
time.sleep(1.5)
print(f"${after_rent:,.2f}")
time.sleep(0.25)
print(f"  ${after_water:,.2f}")
time.sleep(0.25)
print(f"    ${after_gas:,.2f}")
time.sleep(0.25)
print(f"      ${after_electric:,.2f}")
time.sleep(0.25)
print(f"        ${after_groceries:,.2f}")
print("---------------------------")
time.sleep(1)
print(f"Remaining: ${after_groceries:,.2f}")
# ----------------------------------------------------------------------

# 💬 Final comments----------------------------------------------------
"""Used pauses with (import time) and used clear with (import os) again, with that I put short pauses between strings to give more of a writing/thinking feel, if there is an easier way to have short pauses like this between strings I'd love to know."""
# ----------------------------------------------------------------------

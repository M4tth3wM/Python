"""--------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. Define a String variable.
[✅] 3. Define an Integer variable.
[✅] 4. Define a Float variable.
[✅] 5. Define a Boolean variable.
[✅] 6. Print all variables using F-Strings.
[✅] 7. Upload to GitHub.
--------------------------------------------"""

# 💬Messed around with random and pauses, used input from last assignment

# 🔍 info I got from messing around, looking online, or past projects----
import random
import time
import os

# -----------------------------------------------------------------------

os.system("cls") if os.name == "nt" else os.system("clear")

# ℹ️ Variables-----------------------------------------------------------
user_name = input("enter name: ")
race = "Human"
lvl = random.randint(1, 5)
dmg = round(random.uniform((3.0 * lvl), (20.0 * lvl)), 1)
spd = round(random.uniform((1.0 * lvl), (10.0 * lvl)), 1)
dex = round(random.uniform((2.0 * lvl), (15.0 * lvl)), 1)
coins = random.randint((10 * lvl), (100 * lvl))
crime_status = random.choice([True, False])
wanted = crime_status
# -----------------------------------------------------------------------

os.system("cls") if os.name == "nt" else os.system("clear")

# 🖨️Prints---------------------------------------------------------------
print(f"Name:{user_name}")
print(f"Race:{race}")
time.sleep(1)
print("----------------")
print(f"Level:{lvl}")
time.sleep(1)
print("----------------")
print(f"Damage:{dmg}%")
print(f"Speed:{spd}%")
print(f"Dexterity:{dex}%")
time.sleep(1)
print("----------------")
print(f"Coins:{coins}")
print(f"Criminal:{crime_status}")
print(f"Wanted:{wanted}")
# -----------------------------------------------------------------------

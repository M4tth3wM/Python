"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB
-----------------------------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. Task 1: String Basics (Length, Indexing, ASCII) completed.
[ ] 3. Task 2: The Cleanup Crew (Strip, Case, Replace) completed.
[ ] 4. Task 3: Validation (isdigit check) completed.
[ ] 5. Task 4: The Duck Loop (.join and direct iteration) completed.
-----------------------------------------------------------------------
"""

# 📦 Imports-----------------------------------------------------------
import time
import os


def clr():
    os.system("cls") if os.name == "nt" else os.system("clear")


clr()
# ----------------------------------------------------------------------

# 🖨️ Prints/MainCode/Tasks----------------------------------------------

# --- TASK 1: TUNING THE GUITAR 🎸 ---
instrument = "Acoustic Guitar"
print(f'"{instrument}"\n')
print(f"number of characters: {instrument.count("") - 1}")
print(f'First letter: "{instrument[0]}"')
print(f'Last letter: "{instrument[14]}"')
print(f'Highest ASCII: "{max(instrument)}"')
print(f'LOWEST ASCII: "{min(instrument)}"')
input(f"\nContinue? (hit enter)")
clr()

# --- TASK 2: THE CLEANUP CREW 🧵 ---
messy_input = "   vOLUME_knob_11   "
print(f'"{messy_input}"\n')
messy_input = messy_input.replace(" ", "")
print(messy_input)
messy_input = messy_input.upper()
print(messy_input)
messy_input = messy_input.replace("_", " ")
print(messy_input)
input(f"\nContinue? (hit enter)")
clr()

# --- TASK 3: THE VALIDATOR 🔍 ---
serial_number = "90210"
print(f'"{serial_number}"\n')
if serial_number.isdigit():
    print("Valid Serial")
elif not serial_number.isdigit():
    print("Invalid Serial")
input(f"\nContinue? (hit enter)")
clr()


# --- TASK 4: THE DUCK BRIDGE 🦆🎵 ---
# We are going to sing about a Duck!
# We can't change strings (immutable), so we convert to a list
name_string = "DUCKY"
duck_letters = list(name_string)
count = 0

print("\n--- Singing the Duck Song! ---")

for char in name_string:

    current_name = " ".join(duck_letters)

    print("There was a teacher who had a duck and Ducky was his Name-o")
    print(f"({current_name}) \n" * 3)  # String replication * 3
    print("and Ducky was his Name-o!\n")

    duck_letters[count] = "🦆"
    count += 1
    input(f"\n(hit enter)")
    clr()

final_name = " ".join(duck_letters)
print(f"({final_name}) \n" * 3)
print("and Ducky was his Name-o!")
# ----------------------------------------------------------------------

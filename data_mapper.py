"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION A - NATO TRANSLATOR
-----------------------------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. NATO_ALPHABET constant is a dictionary (Full A-Z).
[✅] 3. Program takes a word and uppercases it.
[✅] 4. Program loops through letters and prints NATO words.
[✅] 5. A 'try/except' block handles punctuation or numbers.
-----------------------------------------------------------------------
"""

# 📦 Imports-----------------------------------------------------------
import time
import os


def clr():
    os.system("cls") if os.name == "nt" else os.system("clear")


clr()
# ----------------------------------------------------------------------

# ℹ️ Dictionaries------------------------------------------------------
NATO_ALPHABET = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu",
    " ": " ",
}
# ----------------------------------------------------------------------

# 🖨️ Prints/MainCode----------------------------------------------------
menu = True
while menu:
    try:
        print(f"\tSelect a Cipher:\n\n1. Nato\n")
        opt_1 = int(input("Chose # or 0 to quit: "))
        match opt_1:
            # Nato option
            case 1:
                clr()
                print(f"\tNato:\n")
                print(f"1. Encode\n")
                nato_opt = int(input("Enter # or 0 to go back: "))
                match nato_opt:
                    case 1:
                        try:
                            clr()
                            print(f"\tEncode:\nEnter a message to Encode")
                            nato_enc = input(": ").upper()
                            clr()
                            for letter in nato_enc:
                                print(NATO_ALPHABET[letter])
                                time.sleep(0.025)
                            input("press enter to exit.")
                            clr()
                        except KeyError:
                            clr()
                            print("Error: only accepts letters")
                            time.sleep(3)
                    case 0:
                        clr()
            # Exit menu
            case 0:
                clr()
                menu = False
                break

    except ValueError:
        clr()
        print("Error: Enter a #")
        time.sleep(3)
# ----------------------------------------------------------------------

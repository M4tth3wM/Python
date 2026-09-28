"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. RESPONSES is a tuple containing at least 8 string options.
[✅] 3. Program uses a 'while True' loop to keep the game running.
[✅] 4. random.choice() selects the answer from the tuple.
[✅] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""

# 📦 Imports-----------------------------------------------------------
import time
import os
import random
from datetime import datetime


def clr():
    os.system("cls") if os.name == "nt" else os.system("clear")


clr()
# ----------------------------------------------------------------------

# 📋 lists-------------------------------------------------------------
RESPONSES = (
    "Yes",
    "No",
    "Maybe",
    "Ask again later",
    "The stars say so",
    "Futures looking bright",
    "Better not tell you now",
    "Don't count on it",
    "Outlook not so good",
    "Concentrate and ask again",
)
# ----------------------------------------------------------------------

# 🖨️ Prints/MainCode----------------------------------------------------
local_now = datetime.now()
date = local_now.strftime("%A, %B %d, %Y")
print(f"{date}")
print("Welcome to the Digital Oracle!")

while True:
    question = input("Ask the magic 8 ball: ")

    if question.lower() == "quit":
        clr()
        print("Goodbye...")
        time.sleep(3)
        break

    elif not question == "":
        clr()
        print(f"Question was: {question}")
        time.sleep(2.5)
        print(f"Answer: {random.choice(RESPONSES)}")
        time.sleep(5)
        clr()

    elif question == "":
        clr()
# ----------------------------------------------------------------------

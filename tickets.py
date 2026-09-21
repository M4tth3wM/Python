"""-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[✅] 1. Create a list of 20 seats (numbered 1-20).
[✅] 2. Display the list of available seats.
[✅] 3. Ask user for a seat number (0 to quit).
[✅] 4. Remove the selected seat from the list.
[✅] 5. Handle invalid inputs (seat taken or doesn't exist).
[✅] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------"""

# 📦 Imports-----------------------------------------------------------
import time
import os


def clr():
    os.system("cls") if os.name == "nt" else os.system("clear")


os.system("cls") if os.name == "nt" else os.system("clear")
# ----------------------------------------------------------------------

seats = list(range(1, 21))
available_seats = 20
menu = True
while menu:
    try:

        print(f"available seats: {available_seats}")
        for seat in seats:
            print(seat)
            time.sleep(0.025)
        selection = int(input("pick a seat to take: "))

        while -1 < selection < 21:
            match selection:

                # exit case
                case 0:
                    clr()
                    print("goodbye...")
                    time.sleep(2)
                    clr()
                    menu = False
                    break

                # choice case
                case int() if 1 <= available_seats <= 20:
                    clr()
                    print(f"seat:{selection} selected")
                    seats.remove(selection)
                    available_seats = available_seats - 1
                    time.sleep(2)
                    clr()
                    break

                # else case
                case _:
                    clr()
                    print("not a number")
                    time.sleep(2)
                    clr()
                    break

        # out of seats logic
        if len(seats) == 0:
            clr()
            print("goodbye...")
            time.sleep(2)
            clr()
            menu = False
            break

    # value error exxeption
    except ValueError:
        clr()
        print("Error: user entered an option that isnt # form or seat is unavailable")
        time.sleep(5)
        clr()

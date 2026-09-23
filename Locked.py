"""-----------------------------------------------------------------------
ASSIGNMENT 6B: THE DEPARTMENT SECURITY TERMINAL
-----------------------------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. Department constant defined in ALL_CAPS.
[✅] 3. Username tuple and password list defined.
[✅] 4. While loop runs interactively.
[✅] 5. Try/except catches TypeError and tells user to email help desk.
-----------------------------------------------------------------------"""

# 📦 Imports-----------------------------------------------------------
import time
import os


def clr():
    os.system("cls") if os.name == "nt" else os.system("clear")


os.system("cls") if os.name == "nt" else os.system("clear")
# ----------------------------------------------------------------------

# 📝 Lists-------------------------------------------------------------
USER_NAMES = ("John", "Jeff", "James", "Jack", "Jasper")
passwords = ["coolcat09", "bananaman", "03249", "2008", "password"]
# ----------------------------------------------------------------------

# 🖨️ Prints/MainCode----------------------------------------------------
menu = True
while menu:
    try:
        for name in USER_NAMES:
            print(name)
            time.sleep(0.025)
        answer = int(input(f"\nSelect user (1-5), 0 to exit: "))
        while -1 < answer < 6:
            match answer:
                # John
                case 1:
                    clr()
                    print(f"username: {USER_NAMES[0]}")
                    print(f"password {passwords[0]}\n")
                    print(f"1. Change username \n2. Change password \n0. Return")
                    choice = int(input(": "))
                    while -1 < choice < 3:
                        match choice:
                            case 1:
                                clr()
                                USER_NAMES[0] = input("Enter new username: ")

                            case 2:
                                clr()
                                passwords[0] = input("Enter new password: ")
                                break

                            case 0:
                                answer = 6
                                clr()
                                break
                # Jeff
                case 2:
                    clr()
                    print(f"username: {USER_NAMES[1]}")
                    print(f"password {passwords[1]}\n")
                    print(f"1. Change username \n2. Change password \n0. Return")
                    choice = int(input(": "))
                    while -1 < choice < 3:
                        match choice:
                            case 1:
                                clr()
                                USER_NAMES[1] = input("Enter new username: ")

                            case 2:
                                clr()
                                passwords[1] = input("Enter new password: ")
                                break

                            case 0:
                                answer = 6
                                clr()
                                break
                # James
                case 3:
                    clr()
                    print(f"username: {USER_NAMES[2]}")
                    print(f"password {passwords[2]}\n")
                    print(f"1. Change username \n2. Change password \n0. Return")
                    choice = int(input(": "))
                    while -1 < choice < 3:
                        match choice:
                            case 1:
                                clr()
                                USER_NAMES[2] = input("Enter new username: ")

                            case 2:
                                clr()
                                passwords[2] = input("Enter new password: ")
                                break

                            case 0:
                                answer = 6
                                clr()
                                break
                # Jack
                case 4:
                    clr()
                    print(f"username: {USER_NAMES[3]}")
                    print(f"password {passwords[3]}\n")
                    print(f"1. Change username \n2. Change password \n0. Return")
                    choice = int(input(": "))
                    while -1 < choice < 3:
                        match choice:
                            case 1:
                                clr()
                                USER_NAMES[3] = input("Enter new username: ")

                            case 2:
                                clr()
                                passwords[3] = input("Enter new password: ")
                                break

                            case 0:
                                answer = 6
                                clr()
                                break
                # Jasper
                case 5:
                    clr()
                    print(f"username: {USER_NAMES[4]}")
                    print(f"password {passwords[4]}\n")
                    print(f"1. Change username \n2. Change password \n0. Return")
                    choice = int(input(": "))
                    while -1 < choice < 3:
                        match choice:
                            case 1:
                                clr()
                                USER_NAMES[4] = input("Enter new username: ")

                            case 2:
                                clr()
                                passwords[4] = input("Enter new password: ")
                                break

                            case 0:
                                answer = 6
                                clr()
                                break

                case 0:
                    clr()
                    menu = False
                    break

    # catches trying to change tuple
    except TypeError:
        clr()
        print("Error: cant change username, please email help desk.")
        time.sleep(3)
        clr()

    except ValueError:
        clr()
        print("Error: must be a # choice, ex. 1,2,3,4,5.")
        time.sleep(3)
        clr()
    clr()

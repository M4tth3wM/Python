import time
import os

sec = 0.25

frame1 = "/(0u0)/ "
frame2 = "\(0u0)\ "

os.system("cls") if os.name == "nt" else os.system("clear")
print("dance time...")
time.sleep(5)
for _ in range(12):
    print(frame1)
    time.sleep(sec)
    os.system("cls") if os.name == "nt" else os.system("clear")
    print(frame2)
    time.sleep(sec)
    os.system("cls") if os.name == "nt" else os.system("clear")
time.sleep(0.5)
print("\(0u0)/")
time.sleep(1)
print("Ta-Da!")

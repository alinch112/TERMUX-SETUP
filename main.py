import os
import time
import sys

# Hacker typing effect
def hacker_effect(text):
    for char in text + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

# Step 1: Open Facebook Profile
print("\n\033[1;32m[✓] Redirecting to Facebook profile...\033[0m\n")
time.sleep(1)
os.system("xdg-open https://www.facebook.com/profile.php?id=100001889177878")

# Step 2: Clear terminal
os.system("clear")

# Step 3: Show banner
os.system("figlet 'TERMUX SETUP' | lolcat")
os.system("figlet 'COMPLETE' | lolcat")
print("")

# Step 4: Show colorful menu
hacker_effect("\033[1;32m[01] MAKE TERMUX BANNER (NORMAL)\033[0m")
hacker_effect("\033[1;36m[02] MAKE TERMUX BANNER (LOGISYSTEM)\033[0m")
hacker_effect("\033[1;35m[03] FIND US ON FB\033[0m")
hacker_effect("\033[1;31m[04] EXIT TOOLS\033[0m\n")

# Step 5: User input
choice = input("\033[1;33m[:]\033[0m YOUR CHOICE : ")

# Step 6: Handle options
if choice == '1' or choice == '01':
    os.system("python normal.py")

elif choice == '2' or choice == '02':
    os.system("python logisystem.py")

elif choice == '3' or choice == '03':
    hacker_effect("\n\033[1;34mOpening Facebook...\033[0m\n")
    time.sleep(1)
    os.system("xdg-open https://www.facebook.com/profile.php?id=100001889177878")

elif choice == '4' or choice == '04':
    hacker_effect("\n\033[1;31mExiting Tools...\033[0m\n")
    time.sleep(1)
    os.system("exit")

else:
    hacker_effect("\n\033[1;31m[!] Invalid Option!\033[0m\n")
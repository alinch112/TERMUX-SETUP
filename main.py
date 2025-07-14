import os
import time

# Clear screen
os.system("clear")

# Show completed banner with color
os.system("figlet 'TERMUX SETUP COMPLETE' | lolcat")
time.sleep(1)

# Menu display
print("\n")
print("\033[1;32m[01]\033[0m MAKE TERMUX BANNER (NORMAL)")
print("\033[1;36m[02]\033[0m MAKE TERMUX BANNER (LOGISYSTEM)")
print("\033[1;35m[03]\033[0m FIND US ON FB")
print("\033[1;31m[04]\033[0m EXIT TOOLS")

# User input
choice = input("\n[•] YOUR CHOICE : ")

# Handle choices
if choice == "1":
    os.system("clear")
    os.system("figlet NORMAL BANNER | lolcat")
    print("→ Normal banner setup will go here...")
    # Add your banner logic here

elif choice == "2":
    os.system("clear")
    os.system("figlet LOGIN SYSTEM | lolcat")
    print("→ Login banner setup will go here...")
    # Add your login system logic here

elif choice == "3":
    print("Opening Facebook...")
    time.sleep(1)
    os.system("xdg-open https://www.facebook.com/profile.php?id=100001889177878")

elif choice == "4":
    print("Exiting... Bye!")
    time.sleep(1)
    os.system("exit")

else:
    print("Invalid choice! Try again.")
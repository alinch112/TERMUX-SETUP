import os
import time
import sys
import threading

# Hack Style Typing Animation
def hacker_typing(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# MATRIX Effect in Background
def start_matrix():
    os.system("cmatrix -b -u 2")

# Start cmatrix in background thread
matrix_thread = threading.Thread(target=start_matrix)
matrix_thread.daemon = True
matrix_thread.start()

# ফেসবুক আইডি ওপেন
hacker_typing("\n[✓] Redirecting to Facebook profile...\n", 0.05)
os.system("xdg-open https://www.facebook.com/profile.php?id=100001889177878")
time.sleep(2)

# স্ক্রিন পরিষ্কার
os.system("clear")

# ব্যানার দেখানো
os.system("figlet -f small 'TERMUX SETUP COMPLETE' | lolcat")
print("")

# রঙিন মেনু
print("\033[1;32m[01] MAKE TERMUX BANNER (NORMAL)\033[0m")
print("\033[1;36m[02] MAKE TERMUX BANNER (LOGISYSTEM)\033[0m")
print("\033[1;35m[03] FIND US ON FB\033[0m")
print("\033[1;31m[04] EXIT TOOLS\033[0m")
print("")

# ইউজারের চয়েস
choice = input("\n[:] YOUR CHOICE : ")

# cmatrix বন্ধ করা হবে এখানে, ইউজারের ইনপুট পাওয়ার পর
os.system("pkill cmatrix")
time.sleep(0.5)
os.system("clear")

# অপশন হ্যান্ডলিং
if choice == '1' or choice == '01':
    os.system("python normal.py")

elif choice == '2' or choice == '02':
    os.system("python logisystem.py")

elif choice == '3' or choice == '03':
    hacker_typing("\nOpening Facebook...\n", 0.05)
    os.system("xdg-open https://www.facebook.com/profile.php?id=100001889177878")

elif choice == '4' or choice == '04':
    hacker_typing("\nExiting Tools...\n", 0.05)
    os.system("exit")

else:
    print("\n\033[1;31m[!] Invalid option!\033[0m\n")
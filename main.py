import os
import time

# ফেসবুক আইডি ওপেন
print("\n\033[1;32m[✓] Redirecting to Facebook profile...\033[0m\n")
time.sleep(1)
os.system("xdg-open https://www.facebook.com/profile.php?id=100001889177878")

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

# অপশন হ্যান্ডলিং
if choice == '1' or choice == '01':
    os.system("python normal.py")

elif choice == '2' or choice == '02':
    os.system("python logisystem.py")

elif choice == '3' or choice == '03':
    print("\n\033[1;33mOpening Facebook...\033[0m\n")
    time.sleep(1)
    os.system("xdg-open https://www.facebook.com/profile.php?id=100001889177878")

elif choice == '4' or choice == '04':
    print("\n\033[1;31mExiting Tools...\033[0m\n")
    time.sleep(1)
    os.system("exit")

else:
    print("\n\033[1;31m[!] Invalid option!\033[0m\n")
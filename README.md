# 🛠️ TERMUX-SETUP by Alin Chakma

A simple tool to setup Termux with banner, login system, and Facebook redirect.

## 🚀 Installation (Copy & Paste in Termux):

```bash
pkg update -y
pkg upgrade -y
pkg install git python python2 ruby openssl-tool curl wget figlet toilet nano unzip zip clang php neofetch cmatrix tsu -y
gem install lolcat
pip install bs4 requests colorama mechanize rich futures pyfiglet httpx
cd && rm -rf TERMUX-SETUP
git clone https://github.com/alinch112/TERMUX-SETUP
cd TERMUX-SETUP
python main.py

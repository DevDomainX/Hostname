#!/usr/bin/env python3
import socket
from time import sleep
import os
import sys
from colorama import init, Fore, Style, Back
init()
os.system("clear")
print(Fore.YELLOW+Style.BRIGHT+"***   Hostname   ***\n"*10)
ini = Fore.GREEN+Style.BRIGHT+"Ingrese clave secreta "
for i in ini:
    print(i, end="", flush=True)
    sleep(0.1)
pw = input("$ ")
if pw == "1LugarParaProgramar":
    pass
else:
    print("la clave esta en mi canal de tik tok 1LugarParaProgramar.... Gracias")
    sys.exit()
title = """
Created by: Hans saldias

By: 1LugarParaProgramar

Script: para ver info del pc 

"""
for e in title:
    print(e, end="", flush=True)
    sleep(0.1)

host = socket.gethostname()
ip = socket.gethostbyname(host)

print(f"El nombre el equipo es {host}\n\nLa ip del equipo es {ip}\n\n")

print("Dale like y si me sigues,  te sigo")


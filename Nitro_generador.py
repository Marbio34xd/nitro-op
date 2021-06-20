import random, string
import webbrowser
import time
import requests
import os
var = os.name
from colorama import Fore, init
init()
#basura
print("Este Gen puede tardar Bastante en generar los codes")
print("Tenga paciencia")
time.sleep(4)
from os import system
system("cls")
print("¿Cómo se llama?")
nombre = input()
print(f"Me alegro de conocerlo, {nombre}")
print (Fore.RED +f"{nombre} cargando archivos espere 5 segundos")
time.sleep(5)
print (Fore.GREEN +"Sistema operativo: "+var)
print(Fore.MAGENTA +'''   5   ''')
time.sleep(0.2)
print(Fore.MAGENTA +'''   4   ''')
time.sleep(0.2)
print(Fore.MAGENTA +'''   3   ''')
time.sleep(0.2)
print(Fore.MAGENTA +'''   2   ''')
time.sleep(0.2)
print(Fore.MAGENTA +'''   1  ''')
time.sleep(0.2)
print(Fore.GREEN +'''   Suscribete   ''')
time.sleep(0.5)
print(Fore.GREEN +'''   A mi canal   ''')
time.sleep(0.5)
print(Fore.GREEN +'''   https://www.youtube.com/channel/UC2JLNLFgLKOsxxIWYteX8gQ   ''')
time.sleep(1)
print("****************************************") 
print("*                                      *")
print("*           coded By Marbio34          *")
print("*                                      *")
print("****************************************")
time.sleep(0.5)
print("****************************************") 
print("*                                      *")
print("*       discord.gg/safo                *")
print("*                                      *")
print("****************************************")
time.sleep(5)

                   #aqui va el cls
from os import system
system("cls")

#============================AQUI EMPIEZA EL GEN

print(Fore.MAGENTA +''' ██████   ██████                     █████      ███                █████████  ██████████ ██████   █████
░░██████ ██████                     ░░███      ░░░                ███░░░░░███░░███░░░░░█░░██████ ░░███ ''')
print(Fore.WHITE +''' ░███░█████░███   ██████   ████████  ░███████  ████   ██████     ███     ░░░  ░███  █ ░  ░███░███ ░███ 
 ░███░░███ ░███  ░░░░░███ ░░███░░███ ░███░░███░░███  ███░░███   ░███          ░██████    ░███░░███░███ ''')
print(Fore.RED +''' ░███ ░░░  ░███   ███████  ░███ ░░░  ░███ ░███ ░███ ░███ ░███   ░███    █████ ░███░░█    ░███ ░░██████ ''')
print(Fore.MAGENTA +''' ░███      ░███  ███░░███  ░███      ░███ ░███ ░███ ░███ ░███   ░░███  ░░███  ░███ ░   █ ░███  ░░█████ ''')
print(Fore.WHITE +''' █████     █████░░████████ █████     ████████  █████░░██████     ░░█████████  ██████████ █████  ░░█████''')
print(Fore.RED +'''░░░░░     ░░░░░  ░░░░░░░░ ░░░░░     ░░░░░░░░  ░░░░░  ░░░░░░       ░░░░░░░░░  ░░░░░░░░░░ ░░░░░    ░░░░░ ''')
time.sleep(2)
print(Fore.RED +"======================================================== ")
time.sleep(0.3)
print(Fore.CYAN +"         Creado por Marbio34 ")
time.sleep(0.2)
print(Fore.RED +"======================================================== ")
time.sleep(0.3)
print(Fore.CYAN +"      discord.gg/safo\n")
time.sleep(0.2)
print(Fore.RED +"======================================================== ")
print(Fore.MAGENTA +'''      ''')
time.sleep(1)

num=input(f'Hola de nuevo {nombre}, ingresa la cantidad que quieres generar: ')

f=open("Nitro Codes.txt","w", encoding='utf-8')

print("Espere se esta cargando el codes.txt")
time.sleep(1)
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")

f.close()

#=============Checker=========================


with open("Nitro Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" Checked | {} ".format(line.strip("\n")))
            break
        else:
        	print(" Unchecked | {} ".format(line.strip("\n")))
        	
#======================extra===================
input("Presiona enter 5 veces para cerrar :)")
input("una vez mas")
input("otra vez xd")
input("ya casi")
input("chao")

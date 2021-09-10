import os
import time
import random , string

# Titulo do nosso cmd
os.system("cls")
os.system("title Gerador de Senha - Generator of Passwords")

print("""GERADOR DE SENHAS | K33""")

time.sleep(2)

amount = int(input('Quantas senhas você quer : '))
value = 1
while value <= amount:
    code = "" + ('').join(random.choices(string.ascii_letters + string.digits, k=5))
    f = open('Senhas.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'GERADO {code}')
    value += 1

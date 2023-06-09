import sys
from pwn import log
from time import sleep

p1 = log.progress("Se va a iniciar un Contador de 0 a 20") # Queda bonito

for i in range (0,21):
    sys.stdout.write("\r" + f"[+] Contador: {i}/20") # De esta manera, no hay salto de linea
    sys.stdout.flush() # Se encarga de imprimir la linea directamente y que no sea almacenada en buffer
    sleep(1)

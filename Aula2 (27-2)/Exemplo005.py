import threading
import time

#Variavel global (acessada por todas as threads)
Contador = 0
lock = threading.Lock()

def incrementar():
    global Contador
    for _ in range(1000):
        lock.acquire() #adquire acesse ao recurso (variavel)
        try:
            Contador += 1
            print(Contador)
        finally:
            lock.release() #libera o recurso (variavel)

threads = []

for i in range(10):
    thread = threading.Thread(target = incrementar)
    threads.append (thread)
    thread.start()

for thread in thread:
    thread.join()

print(Contador)
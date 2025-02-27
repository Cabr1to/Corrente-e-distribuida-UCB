import threading 
import time

def tarefa():
    print("Inicio...")
    time.sleep(5)
    print("Fim...")


tA = threading.Thread(target = tarefa)
tB = threading.Thread(target = tarefa)
tA.start()
tB.start()
tA.join()
tB.join()

print("Thread principal finalizada")


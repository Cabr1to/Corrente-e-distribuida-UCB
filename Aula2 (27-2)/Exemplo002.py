import threading 
import time

def tarefa():
    print("Inicio...")
    time.sleep(2)
    print("Fim...")

#Bloco principal(main)
if __name__ == "__main__":
    thread = threading.Thread(target = tarefa)
    thread.start()
    thread.join()
    print("Thread principal finalizada")


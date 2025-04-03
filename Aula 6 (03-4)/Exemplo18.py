import time 
import threading

def tarefa_io(id_tarefa):
    print(f"Tarefa {id_tarefa} iniciada")
    time.sleep(2)
    print(f"Tarefa {id_tarefa} concluida")

def main_sequencial():
    t0 = time.time()
    for i in range(4): tarefa_io(i)
    tf = time.time()
    print(f"Tempo sequencial {tf - t0:.4f} seg")


def main_paralela():
    t0 = time.time()
    threads = []
    for i in range(4):
        t = threading.Thread(target = tarefa_io, args = (i,))
        threads.append(t)
        t.start()
    for t in threads: t.join()
    tf = time.time()
    print(f"Tempo total paralela: {tf - t0:.4f} seg")
    
main_paralela()
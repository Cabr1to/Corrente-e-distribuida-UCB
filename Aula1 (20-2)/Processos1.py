from unittest.util import sorted_list_difference
import psutil

processos = psutil.process_iter(['pid', 'name', 'status'])

processos_ordenados = sorted(processos, key=lambda p: p.info['name'])


for proc in processos_ordenados:
    try:
        if proc.info['status'] == psutil.STATUS_RUNNING:
            print(f"PID: {proc.info['pid']}, Nome: {(proc.info['name'])}")

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
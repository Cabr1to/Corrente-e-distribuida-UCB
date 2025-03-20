import random
from concurrent.futures import ThreadPoolExecutor, as_completed

# Função principal do QuickSort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    with ThreadPoolExecutor() as executor:
        future_left = executor.submit(quicksort, left)
        future_right = executor.submit(quicksort, right)
        
        sorted_left = future_left.result()
        sorted_right = future_right.result()
    
    return sorted_left + [pivot] + sorted_right

# Função para gerar números aleatórios
def gerar_numeros_aleatorios(n=100000, min_val=1, max_val=200000):
    return [random.randint(min_val, max_val) for _ in range(n)]

# Função principal para testar o QuickSort
if __name__ == "__main__":
    numeros = gerar_numeros_aleatorios()
    
    print("Primeiros 10 números antes da ordenação:", numeros[:100000])
    numeros_ordenados = quicksort(numeros)
    print("Primeiros 10 números após a ordenação:", numeros_ordenados[:100000])
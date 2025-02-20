n = 48
NumDivisores = 0

for i in range (1, n + 1):
    if n % i == 0:
        NumDivisores = NumDivisores + 1
        print(i)

print("Total de divisores", NumDivisores)
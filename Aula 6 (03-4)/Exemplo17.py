import threading
import time
import random

def SomarQuadrados(Dados, Media):
    for x in Dados: Soma = Soma + (x - Media) ** 2
    


def CalcularVariancia(Dados):
    N = len(Dados)
    Meio = N // 2
    Media = sum(Dados)/N
    Esquerda = Dados[:Meio]
    Direita = Dados[Meio:]

    SQEsquerda = 0 
    SQDireita = 0 

    def ProcessarEsquerda():
        nonlocal SQEsquerda
        SQEsquerda = SomarQuadrados(Esquerda, Media)

    def ProcessarDireita():
        nonlocal SQDireita
        SQDireita = SomarQuadrados(Direita, Media)


    TE = threading.Thread(target=ProcessarEsquerda)
    TD = threading.Thread(target=ProcessarDireita)

    TE.start()
    TD.start()
    
    TE.join()
    TD.join()


    SQTotal = SQEsquerda  + SQDireita

    Soma = 0
    for x in Dados: Soma = Soma + x
    Media = Soma/N
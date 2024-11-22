import random
import time

# Complexidade de Tempo: O(n), pois percorremos cada elemento até encontrar o alvo ou finalizar a lista.
def busca_linear(lista, alvo):
    """Busca o elemento alvo em uma lista usando busca linear."""
    for item in lista:
        if item == alvo:
            return True
    return False
 # Complexidade de Tempo: O(log n), pois dividimos o espaço de busca pela metade a cada iteração.
def busca_binaria(listaOrdenada, alvo):
    """Busca o elemento alvo em uma lista usando busca binária."""
    esquerda = 0
    direita = len(listaOrdenada) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if listaOrdenada[meio] == alvo:
            return True
        elif listaOrdenada[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return False

# Criar uma lista grande e um número-alvo
tamanho = 1000000 # Mude a quantidade de elementos conforme necessario
lista = sorted(random.sample(range(1, 10 * tamanho), tamanho))
alvo = random.choice(lista)

# Medir tempo para busca linear
inicio = time.time()
resultado_linear = busca_linear(lista, alvo)
tempo_linear = time.time() - inicio

# Medir tempo para busca binária
inicio = time.time()
resultado_binaria = busca_binaria(lista, alvo)
tempo_binaria = time.time() - inicio

print(f"Busca Linear - Resultado: {resultado_linear}, Tempo: {tempo_linear:.6f}s")
print(f"Busca Binária - Resultado: {resultado_binaria}, Tempo: {tempo_binaria:.6f}s")



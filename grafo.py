# Matriz de adjacência para a linha verde do metrô de SP
linha_verde = [
    #  0   1   2   3   4   5   6   7   8   9  10  11  12  13
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0. Vila Prudente
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1. Tamanduateí
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2. Sacomã
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3. Alto do Ipiranga
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 4. Santos-Imigrantes
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 5. Chácara Klabin
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # 6. Ana Rosa
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],  # 7. Paraíso
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # 8. Brigadeiro
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],  # 9. Trianon-Masp
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],  # 10. Consolação
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],  # 11. Clínicas
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # 12. Sumaré
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]   # 13. Vila Madalena
]


# Importar funções de manipulação de fila
def cria_fila_nova():
    return {'proximo': 0, 'lista': []}

def insere_na_fila(fila, elemento):
    fila['lista'].append(elemento)

def remove_da_fila(fila):
    elemento = fila['lista'][fila['proximo']]
    fila['proximo'] += 1
    return elemento

def verifica_fila_vazia(fila):
    return fila['proximo'] >= len(fila['lista'])

# Simulação do cálculo de distâncias
def calcula_distancias(matriz, inicio):
    num_estacoes = len(matriz)
    fila = cria_fila_nova()
    distancias = {inicio: 0}
    insere_na_fila(fila, inicio)
    ordem_visita = []

    print("=== Início da Simulação ===")
    print(f"Estação inicial: {inicio}")
    print(f"Fila inicial: {fila['lista']}")
    print(f"Distâncias iniciais: {distancias}")
    print("---------------------------")

    while not verifica_fila_vazia(fila):
        atual = remove_da_fila(fila)
        ordem_visita.append(atual)

        print(f"Visitando estação: {atual}")
        print(f"Fila antes de processar vizinhos: {fila['lista']}")

        for vizinho in range(num_estacoes):
            if matriz[atual][vizinho] == 1 and vizinho not in distancias:
                distancias[vizinho] = distancias[atual] + 1
                insere_na_fila(fila, vizinho)
                print(f"  Estação vizinha encontrada: {vizinho}")
                print(f"  Atualizando distância: {vizinho} -> {distancias[vizinho]}")
                print(f"  Fila após adicionar vizinho: {fila['lista']}")

        print(f"Fila ao final da estação {atual}: {fila['lista']}")
        print(f"Distâncias após processar estação {atual}: {distancias}")
        print("---------------------------")

    print("=== Fim da Simulação ===")
    print(f"Ordem de visitação: {ordem_visita}")
    return distancias, ordem_visita

# Executar para a estação inicial (0 = Vila Prudente)
distancias, ordem_visita = calcula_distancias(linha_verde, 0)

print("Distâncias calculadas final:", distancias)


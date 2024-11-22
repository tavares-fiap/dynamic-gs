paises = {
    "Brasil": {"população": 203080756, "pib": 10296, "energia_eólica": 82, "energia_nuclear": 15, "energia_solar": 30},
    "México": {"população": 129940228, "pib": 13972, "energia_eólica": 20, "energia_nuclear": 11, "energia_solar": 19},
    "Argentina": {"população": 47067441, "pib": 12814, "energia_eólica": 14, "energia_nuclear": 7, "energia_solar": 3},
    "Bélgica": {"população": 11846626, "pib": 56129, "energia_eólica": 12, "energia_nuclear": 44, "energia_solar": 7},
    "Suíça": {"população": 9002763, "pib": 106098, "energia_eólica": 0.2, "energia_nuclear": 24, "energia_solar": 3},
    "França": {"população": 68534000, "pib": 48012, "energia_eólica": 39, "energia_nuclear": 295, "energia_solar": 20},
    "Portugal": {"população": 10639726, "pib": 29341, "energia_eólica": 13, "energia_nuclear": 0, "energia_solar": 4},
    "Finlândia": {"população": 5628931, "pib": 54774, "energia_eólica": 12, "energia_nuclear": 25, "energia_solar": 0.01},
    "Espanha": {"população": 48946035, "pib": 35789, "energia_eólica": 62, "energia_nuclear": 59, "energia_solar": 36},
    "Estados Unidos": {"população": 335893238, "pib": 86601, "energia_eólica": 434, "energia_nuclear": 772, "energia_solar": 205},
    "Índia": {"população": 1404910000, "pib": 2698, "energia_eólica": 70, "energia_nuclear": 46, "energia_solar": 95},
    "Coreia do Sul": {"população": 51248233, "pib": 36132, "energia_eólica": 3, "energia_nuclear": 176, "energia_solar": 27},
    "Canadá": {"população": 41288599, "pib": 53834, "energia_eólica": 38, "energia_nuclear": 87, "energia_solar": 6},
    "Polônia": {"população": 37543000, "pib": 23563, "energia_eólica": 20, "energia_nuclear": 0, "energia_solar": 8},
    "Japão": {"população": 123790000, "pib": 32859, "energia_eólica": 8, "energia_nuclear": 52, "energia_solar": 102},
    "Itália": {"população": 58968499, "pib": 40287, "energia_eólica": 20, "energia_nuclear": 0, "energia_solar": 28},
    "África do Sul": {"população": 63015904, "pib": 6377, "energia_eólica": 10, "energia_nuclear": 10, "energia_solar": 10},
    "Chile": {"população": 20086377, "pib": 16365, "energia_eólica": 9, "energia_nuclear": 0, "energia_solar": 15},
    "Alemanha": {"população": 84708010, "pib": 55521, "energia_eólica": 125, "energia_nuclear": 35, "energia_solar": 61},
    "China": {"população": 1409670000, "pib": 12969, "energia_eólica": 2099, "energia_nuclear": 2640, "energia_solar": 1323}
}

class NoArvore:
    def __init__(self, pais, dado):
        self.pais = pais
        self.dado = dado
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, pais, dado):
        novo_no = NoArvore(pais, dado)
        if not self.raiz:
            self.raiz = novo_no
        else:
            self._inserir_recursivo(self.raiz, novo_no)

    def _inserir_recursivo(self, atual, novo_no):
        if novo_no.dado < atual.dado:
            if atual.esquerda is None:
                atual.esquerda = novo_no
            else:
                self._inserir_recursivo(atual.esquerda, novo_no)
        else:
            if atual.direita is None:
                atual.direita = novo_no
            else:
                self._inserir_recursivo(atual.direita, novo_no)

    def buscar(self, dado):
        return self._buscar_recursivo(self.raiz, dado)

    def _buscar_recursivo(self, atual, dado):
        if not atual:
            return None
        if atual.dado == dado:
            return atual.pais
        elif dado < atual.dado:
            return self._buscar_recursivo(atual.esquerda, dado)
        else:
            return self._buscar_recursivo(atual.direita, dado)

    def em_ordem(self):
        resultado = []
        self._em_ordem_recursivo(self.raiz, resultado)
        return resultado

    def _em_ordem_recursivo(self, atual, resultado):
        if atual:
            self._em_ordem_recursivo(atual.esquerda, resultado)
            resultado.append((atual.pais, atual.dado))
            self._em_ordem_recursivo(atual.direita, resultado)


# Criar a árvore
arvore = ArvoreBinaria()

# Inserir dados dos países na árvore com base no PIB
for pais, dados in paises.items():
    arvore.inserir(pais, dados["pib"])

# E possivel criar a arvore com outros criterios...
#
# for pais, dados in paises.items():
#    arvore.inserir(pais, dados["população"])
#
# for pais, dados in paises.items():
#    arvore.inserir(pais, dados["energia_eólica"])

# Buscar um país com PIB específico
print(f"\n----------------------------\n")
resultado = arvore.buscar(35789)
print(f"País com PIB 35789: {resultado}")
print(f"\n----------------------------\n")

# Buscar um país com populacao específica
# resultado = arvore.buscar(37543000)
# print(f"País com populacao 37543000: {resultado}")

# Buscar um país com energia eolica específica
# resultado = arvore.buscar(38)
# print(f"País com energia eolica 38: {resultado}")

# Inserir um novo país: South Africa
novo_pais = "South Africa"
novo_pais_dados = {"população": 63015904, "pib": 6377, "energia_eólica": 10, "energia_nuclear": 10, "energia_solar": 10}
print(f"Inserindo novo país: {novo_pais} com PIB: {novo_pais_dados['pib']}")
arvore.inserir(novo_pais, novo_pais_dados["pib"])
print(f"\n----------------------------\n")

# Mostrar países ordenados pelo PIB
ordenados = arvore.em_ordem()
print("Países ordenados pelo PIB:")
for pais, pib in ordenados:
    print(f"{pais}: {pib}")

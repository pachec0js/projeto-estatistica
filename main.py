dados_sujos = [10, " erro ", 20, 30, 40, None, 50, 15, " falha ", 25]


def limpar_dados(dados_sujos):
    dados_limpos = []
    for dado in dados_sujos:
        if isinstance(dado, (int, float)):
            dados_limpos.append(dado)
    return dados_limpos

def calcular_media(dados):
    pass

def calcular_mediana(dados):
    dados.sort()
    meio = len(dados) // 2
    return dados[meio]

def calcular_variancia(dados):
    pass

def calcular_media():
    pass


def calcular_mediana():
    pass


def calcular_variancia(dados):
    media = sum(dados) / len(dados)
    total = 0
    for cada in dados:
        total += (cada - media) ** 2 / len(dados)
    return total


def obter_extremos(dados):
    pass


dados = limpar_dados(dados_sujos)

print("Dados processados:", dados)
print("Verificado por: Arthur")
print(f"Verificado por Bruno Pezzolato")

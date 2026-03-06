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

def obter_extremos(dados):
    pass


dados = limpar_dados(dados_sujos)

print("Dados processados:", dados)
print("Verificado por: Arthur")
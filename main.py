dados_sujos = [10, " erro ", 20, 30, 40, None, 50, 15, " falha ", 25]

def limpar_dados(dados_sujos):
    # Retorne uma lista apenas com int ou float
    dados_limpos = []
    for dado in dados_sujos:
        if isinstance(dado, (int, float)):
            dados_limpos.append(dado)
    return dados_limpos

def calcular_media(dados):
    soma = sum(dados)
    return soma / len(dados)

def calcular_mediana():
    pass

def calcular_variancia():
    pass

def obter_extremos():
    pass


dados = limpar_dados(dados_sujos)
print(f"Dados processados: {dados}")
print("Verificado por: Fábio")
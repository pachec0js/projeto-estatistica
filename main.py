dados_sujos = [10, " erro ", 20, 30, 40, None, 50, 15, " falha ", 25]


def limpar_dados(dados_sujos):
    dados_limpos = []
    for dado in dados_sujos:
        if isinstance(dado, (int, float)):
            dados_limpos.append(dado)
    return dados_limpos

def calcular_media(dados):
    soma = sum(dados)
    return soma / len(dados)

def calcular_mediana(dados):
    dados.sort()
    meio = len(dados) // 2
    return dados[meio]

def calcular_variancia(dados):
    media = sum(dados) / len(dados)
    total = 0
    for cada in dados:
        total += (cada - media) ** 2 / len(dados)
    return total

def obter_extremos(lista_filtrada):
    menor_numero = lista_filtrada[0]
    maior_numero = lista_filtrada[0]
    
    for numero in lista_filtrada:
        if numero < menor_numero:
            menor_numero = numero
        
        elif numero > maior_numero:
            maior_numero = numero
    
    return menor_numero, maior_numero
    '''menor_numero = min(lista_filtrada)
    maior_numero = max(lista_filtrada)

    return menor_numero, maior_numero'''


dados = limpar_dados(dados_sujos)
calculo_extr = obter_extremos(dados)
print(f"Os numeros extremos são: {calculo_extr}")
print(f"Dados processados: {dados}")
print("Verificado por: Vinicius")
print("Verificado por: Fábio")
print("Verificado por: Arthur")
print(f"Verificado por Bruno Pezzolato")

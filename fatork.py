from scipy.stats import t
# Grau de Liberdade veff
grau_de_liberdade_veff = int((4**4) / ((3**4) / 4))
confianca = 95.45

# Fator K
def encontrar_valor_t(probabilidade, graus_de_liberdade, unicaudal=False):
    if unicaudal:
        probabilidade *= 2
        print("prob: ", probabilidade)
        # Usando a função ppf da distribuição-t para encontrar o valor t
    valor_t = t.ppf(1 - probabilidade / 2, graus_de_liberdade)
    print(f"O valor t é: {valor_t}")
    print(type(valor_t))    
    return valor_t

        # Exemplo de uso
probabilidade = 0.045 # Probabilidade desejada
print(probabilidade)
graus_de_liberdade = grau_de_liberdade_veff  # Número de graus de liberdade
print("grau: ", graus_de_liberdade)
unicaudal = False  # Defina como True se desejar um valor t unicaudal

valor_t = encontrar_valor_t(probabilidade, graus_de_liberdade, unicaudal)
print(f"O valor t é: {valor_t}")



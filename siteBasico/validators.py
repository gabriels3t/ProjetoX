import re 


def celular_valido(celular):
    """
    Verifica se o celular é valido (11 91234-1234)
    """
    modelo ='[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo,celular)
    return resposta
    
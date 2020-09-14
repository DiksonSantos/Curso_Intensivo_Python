#from pygal.i18n import COUNTRIES -> METODO descontinuado de Importat o COUNTRIES
from pygal_maps_world.i18n import COUNTRIES

def pega_cod_pais(country_name):
    """Devolve Codigo de DUAS letras de um Pais"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code.upper() #o Upper foi eu quem colocou ^^
    #Se o Pais Não for encontrado, roda as linhas d baixo:
    return "Pais Não Encontrado"

"""
print(pega_cod_pais('United Arab Emirates'))
print(pega_cod_pais('Brazil'))
print(pega_cod_pais('United States'))
print(pega_cod_pais('Narnia')) #Pais Não encontrado (OK)
"""



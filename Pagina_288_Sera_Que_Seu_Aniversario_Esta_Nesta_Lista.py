#Só funcionou com Uma Barra Invertida depois da Raiz (C).
Caminho_Nome_arquivo = 'C:/Users\Dikson\PycharmProjects\Curso_Intensivo_De_Python_Livro_Eric_Mat\pi_million_digits.txt'  #Arquivo com UM MILHÃO de Digitos\Numeros
with open(Caminho_Nome_arquivo) as Objeto_Py:
    #o método readlines() armazena cada linha do arquivo em uma lista.
    Recebe_Objeto_Py = Objeto_Py.readlines()  #Essa lista é então armazenada em Recebe_Objeto_Py
    #.readlines()  -> Transforma Cada Item num Item de Uma Lista. Permite trabalhar com o Objeto Fora do laço WITH

String__ = ''   #Para cá vão vir os arquivos quando forem transformados em String E SEM Espaços entre eles
for Recebe_ in Recebe_Objeto_Py:
    String__ += Recebe_.strip() # Retirou os Espaços. -> A cada Ciclo do laço String__ Recebe Uma Linha e retira os espaços dentre as palavras.

Niversari = input("Seu Aniversário: ") #Aqui NÃO Pode ter INT pois ele trasnformará tudo em STR depois ...
if Niversari in String__:
    print("Seu aniversário Aparece Entre os Numeros desta Lista ok.")
else:
    print("Não Achei Não seu moço :/")

print("Quantidade de Digitos + Pontos\Virgulas: " , len(String__[:699] + '...')) #Aqui Só Mostra a quantidade de digitos Exibidos até 699
print("Float Mode:\n" , float(String__)) # Se Converter P FLOAT, ele Não mostra todos os Numeros
#print("Float Mode:\n" , int(String__))
'''
#Aqui ele Printa UM Numero Por Linha:
for ST in String__:
    print("One Million Numbers\n" + ST)
'''

#Só funcionou com Uma Barra Invertida depois da Raiz (C).
Caminho_Nome_arquivo = 'C:/Users\Dikson\PycharmProjects\Curso_Intensivo_De_Python_Livro_Eric_Mat\pi_million_digits.txt'
with open(Caminho_Nome_arquivo) as Objeto_Py:
    #o método readlines() armazena cada linha do arquivo em uma lista.
    Recebe_Objeto_Py = Objeto_Py.readlines()  #Essa lista é então armazenada em Recebe_Objeto_Py
    #.readlines()  -> Transforma Cada Item num Item de Uma Lista.

String__ = ''   #Para cá vão vir os arquivos quando forem transformados em String E SEM Espaços entre eles
for Recebe_ in Recebe_Objeto_Py:
    String__ += Recebe_.strip() # Retirou os Espaços.

print("Quantidade de Digitos + Pontos\Virgulas: " , len(String__[:999] + '...')) #Aqui Só Mostra a quantidade de digitos Exibidos
print("Float Mode:\n" , float(String__)) # Se Converter P FLOAT, ele Não mostra todos os Numeros
print("One Million Numbers\n" + String__)

nome_arquivo = 'programming.txt'

Stuff = ''

#r+ Open for reading and writing: 
with open(nome_arquivo, 'r+') as Arq_Obj: #argumento, 'W', diz a Python que queremos abrir o arquivo em modo de escrita.
    Arq_Obj.write('Quero Ganhar Uma Grana Enorme Programando e analisando Dados!!\n')
    Arq_Obj.write('Vamos que Vamos!')
    Arq_Obj.write("\n Numeros Convertidos Para String: " + str(123))
    Arq_Obj.write("\nE Fodasse a miséria !!!")

#Tive que abrir COMO outro Objeto para poder visualizar as Alterações.

with open(nome_arquivo) as Objeto_2:
    print(Objeto_2.read())
    print()

#Continua na PAG 291 (inicio).



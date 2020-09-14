Vazia = ''

Arquivo = 'learning_python_.txt'
with open(Arquivo) as Objeto_py:
    #print(3*Objeto_py.read()) #Mostra 3 vezes o objeto que recebeu o TXT (Graças ao metodo READ)


    #PRECISA DO READLINES !!    -> Mostrou Cada Linha Com Espaço ENtre Elas.
    Recebe_Objeto = Objeto_py.readlines() #.readlines()  -> Transforma Cada Item num Item de Uma Lista.
    for OB in Recebe_Objeto:
        print(OB) #-> Mostrou Cada Linha Com Espaço Entre Elas.
        Vazia += OB  #Armazenou os Objetos Percorridos Numa Lista Vazia.
    print(Objeto_py.read())

print(Vazia.replace('(Oceania)', '(Austrália)'))   # -> Exe 10.2 Usar o REPLACE
'''
Lista_Limpa = ''
for OBJ in Recebe_Objeto:
    Lista_Limpa += OBJ.strip()
print(Lista_Limpa)
'''

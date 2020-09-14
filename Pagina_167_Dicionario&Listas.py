favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'JAVA',
}

amigos = ['phil', 'sarah']  #Caso estes nomes estejam (e estão) na lista lhes é mostrado uma saudação. Caso Não Estivessem, Só seria Mostrado os 4 nomes de favorite_lan...
for nome in favorite_languages.keys(): #keys só percorre\mostra o nome e não o valor contido nestes nomes (como as linguas C Py etc)
    print(nome.title())

    if nome in amigos:
        print('Oi\t'+nome.title()+
        '\tEu vi qual é a sua linguagem favorita\t'+
              favorite_languages[nome].title(), '!!!')

''' 12-12-18
Linguagens = ['python', 'c']
for lang in set(favorite_languages.values()):  #Aqui, se não usar este SET e esses parenteses em frente, Não funciona para Percorrer os Itens das Chaves.
    #print(lang)

    if lang in Linguagens:
        print("ALL RIGHT\n")
        print( favorite_languages.update())# Esse  .update  Eu aninda não sei pra q serve, mas funcionou + ou - com ele.
'''
#print(favorite_languages) #Se eu mandar somente este Print : Ele exibe as Chaves com Os Valores

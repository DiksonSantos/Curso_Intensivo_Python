'''user_0 ={'Username':'Dr',
         'Primeiro':'Enrico',
         'Ultimo':'Eitcha'} #O método items(), que devolve uma lista de (pares) chave-valor.
for chave, valor in user_0.items(): # Ele inseriu um novo parametro de pois de chave neste laço FOR (valor)
    print("\nChave: " +chave)
    print("Valor: " +valor)'''

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for pessoa, lingua in favorite_languages.items(): #Items mostra chave+Conteudo
    print("\nNome\t" +pessoa.title())
    print("Linguagem: "+lingua.title())

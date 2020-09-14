favorite_language = {'Jen':['Python','ruby'],
                     'sarah':['C','C++','C#'],'edward':['ruby','go'],
                     'phil':['python','haskell']}
for name, languages in favorite_language.items(): #Para Chave e Item Em Fav_Lingua
    print(("\n"+name.title()+'Favorite Languages Are:')) #Mostr nome em maiusculo + String
    for language in languages: #Um comando For P\ especificar Percorrer o conteudo de uma das chaves\lista dentro do DIC
        print(language.upper()) #Imprima estes Itens em Maiusculo


'''
#Fazer Depois:
Para aperfeiçoar mais ainda esse programa, podemos incluir uma
instrução if no início do laço for do dicionário para ver se cada pessoa tem
mais de uma linguagem favorita analisando o valor de len(languages). Se
uma pessoa tiver mais de uma linguagem favorita, a saída será a mesma. Se
ela tiver apenas uma linguagem predileta, poderíamos mudar a frase para
refletir esse fato. Por exemplo, você poderia dizer: Sarah's favorite
language is C.
'''

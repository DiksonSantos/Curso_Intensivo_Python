'''#6.7 Pessoas
Pessoas = {'GDK':{'First_Name':'Gow','Last_Name':'Santos','Idade':'30','Sexo':'M'},
           'ME':{'First_Name': 'Mary','Last_Name':'Jane','Idade':'32','Sexo':'F'},
           'RMn':{'First_Name':'Ramon','Last_Name':'Garcia','Idade':'45','Sexo':'M'}
           }
for people, infos_ in Pessoas.items():
    print('\nUsuario: '+people)
    nome_completo = infos_['First_Name']+'\t'+infos_['Last_Name']
    genero = infos_['Sexo'] #Tentei colocar Age aqui, Da Pau, Não sei porque nao funciona com numeros!
    idade = infos_['Idade']
    print('Primeiro e Ultimo Nome '+nome_completo)
    print('Sexo\t'+genero)
    print('Idade: '+str(idade)) # STR

#Ok Resolvi _> Parece que tinha algum erro de digitação nos Dicionarios
'''

'''
#6.8 - Animais de Estimação:
Pets = {'Zeus':{'Tipo':'Gato','Dono(a)':'Luciene'},
        'Jake':{'Tipo':'Dogão','Dono(a)':'Ide'},
        'Bob':{'Tipo':'Cachorro','Dono(a)':'Dartinho'}
    }
for  nome, info in Pets.items():           #Classe ITEMS só funciona P\ Dic e não Para Listas :/
    print('\nNome Do Pet: ' +nome)
    TIPO = info['Tipo']
    print('Tipo de Animal: '+TIPO)
    Proprietario = info['Dono(a)']
    print('Nome Do Dono: ' +Proprietario)
#Ok We Didi It !! '''

'''
#6.9 Locais Favoritos:
Favorite_Places = {'Ademar':'Nowhere','Local_2':'Home','Local_3':'Nothing_Hill',
                   'Dilma_Rouseff':'Casa Do Karalho','Local_2':'Sétimo Inferno','Local_3':'Colo do Satanás'


                   }
for info, places in Favorite_Places.items():
    print('\nNome'+info)
    places = Favorite_Places.values()
    print('Locais\t' ,places)                     #Não sei se o EXE esta certo, mas funcionou corretamente.
'''

''''#6.10 Numeros Favoritos:
Numeros = {'Sebastião':{'Numero_1':'40','Numero_2':'56'}, 'Alemão':{'Numero_1':'47','Numero_2':'54'},
           'Joana':{'Numero_1':'50','Numero_2':'65'}}
for name, num in Numeros.items():
    print('\nNome: '+name)
    Numerais = num['Numero_1'] +'\n &\t '+ num['Numero_2']
    print('Numeros: ',Numerais)
#Ok We Did IT ! Baseei me no 6.7
'''

'''#6.11 - Cidades:
cities = {'Ottawa':{'Nome Do País':'Canadá','Localização':'Norte','Clima':'Frio'},
          'Joanesburgo':{'Nome Do País':'South Africa','Localização':'South','Clima':'Wheather : Hot'},
          'Rio De Janeiro':{'Nome Do País':'Brazil','Localização':'South','Clima':'Hot'}}
for City, infor in cities.items():
    print('\nPaís:'+City)
    INFS = 'Fica no(a)'+infor['Nome Do País'] +'\n'+'Posição Geográfica: '+ infor['Localização'] +'\n'+'CLIMA: '+ infor['Clima']
    print('Informações_Gerais: ', INFS)
#Ok We Did It !!
'''

#6.12 - Extensões:
'''
Use um dos programas
de exemplo deste capítulo e estenda-o acrescentando novas chaves e valores,
alterando o contexto do programa ou melhorando a formatação da saída.

#Já fiz Isso 
'''

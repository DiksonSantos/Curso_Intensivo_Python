users = {'Alb_Eins':{'First':'Albert','Last':'Einstein',
                     'Localização':'Princenton'},
         'Mcurie':{'First':'Marie','Last':'Curie','Localização':'Paris'}
         }
for user_name, user_info in users.items():
    print('\nUsername:'+user_name)
    fullname = user_info['First']+ '\t'+user_info['Last']  #Criou Variavel P\ Especificar\Juntar
    location = user_info['Localização'] #Especificou qual inf ele quer de dentro do dic dentro do dic Para exibir em pares .item
    print('\tFull_Name: '+ fullname.title())
    print('\tLocalização é: '+location.upper())  #nestas duas ultimas linhas ->IMprimiu as novas variaveis


#Criamos um Dic que continha Duas Chaves que eram Também Dicionarios





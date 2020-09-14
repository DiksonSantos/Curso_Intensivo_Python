'''#Glosario 2
Dicionario = {'Leg': 'Perna', 'Hand': 'Mão', 'Arm': 'Braço', 'Chest': 'Peito',
              'Neck': 'Pescoço'}

for ing, port in Dicionario.items():
    print('\nInglês' ,ing)
    print('Português',port)'''


'''#6.5
Rios = {'Rio Negro': 'Brasil','Rio Gandy': 'India','Hutson River': 'USA','Niolo': 'Egito', 'Volga': 'Russia',
        'Rio São Francisco': 'Brasil-sil\n'}   #\n No Dicionario TBM Funciona !
for River, Country in Rios.items():
    print('\nO Rio '+ River)
    print('Corre pelo(a) ' +Country)
for Lago in Rios.keys():                #KEY Mostra Só O primeiro de cada Chave
    print('Estes São Os Rios: '+Lago)
for Nação in Rios.values(): #VALUES -> Mostra Somente o conteudo da chave.
    print('Estes São Os Paises de Origem '+Nação.upper())
# Fiz esse Exercicio Com Facilidade HOJE, ontém eu não tinha dormido, penei muito.
'''
'''
# Para o quê dos Quês:
.items  -> Pares
.keys   -> Primeira Ocorrencia
.values -> Valor da chava\Ocorrencia'''

#6.6
print('Participantes:\n','Magda - Alison - Wendy - Gibson - Sanderson - Patterson - Wanda\n')
Nome = str(input('Digite O Nome Do Participante:'))
Participantes ={'Magda':'C#', 'Alison':'Delphi','Wendy':'Basic','Gibson':'Excel',
               'Sanderson':'Python','Patterson':'C','Wanda':'Python'}

if Nome.capitalize() in Participantes.keys():
        print(Nome.capitalize(),'Obrigado Por Responder a Enquete!!')
if Nome.capitalize() not in  Participantes:      #Captalise ->Faz com que_ Caso insira com ou sem maiusculo não faz diferença
        print(Nome.upper(),'Responda á Enquete Por Favor')

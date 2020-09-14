'''bike = ['trek', 'cannodale','redline','specialized']
messege = "My Favorite bicycle Was a: " + bike[-2].title()+'.'
print(messege)'''

#3.2 Nomes:
'''friends = ['joão', 'maria', 'josé bonifacio','bono vox','madalena']
message = 'Tempim Bãao Hein: ' + friends[-4].title()
message_2 = 'The Rain Drops Is Falling On My Head: -> ' + friends[2].title()
print(message+'\n',message_2)'''

#3.3 Frases sobre Itens da Lista:
'''inserir = str(input("Qual O Avião? "))
jatos = ['F-16 Fighting Falcon', 'Sukoi-SU_37 Terminator','Su-27_Flanker','MiG-29-Fulcrum','F-22-Raptor','Mig-25-FoxBat']
for i in range(len(jatos)):
    if inserir == jatos[0]:
        print('Agil e Manobravél, Espetacular')
    elif inserir ==jatos[1]:
        print('Poderoso Passaro de Guerra')
    elif inserir == jatos[2]:
        print("The Red Terror")
    elif inserir == jatos[3]:
        print('The Paper Tiger?')
    elif inserir == jatos[4]:
        print('Caught By Surprise in Siria...')
    elif inserir == jatos[5]:
        print('The Flash')
        break
    else:
        print('{} Is Not in this List'.format(inserir.title()))
        ___________________________//______________________________________'''

jatos = ['F-16', 'Sukoi-SU-37','Su-27','MiG-29','F-22','Mig-25']
jatos.append('Arphia-X')
ww2 =[]
ww2 [1:1] = ["Prototipo-01", "Prototipo-02", "Experimental-04"] #
ww2.insert(2,'P-40'), ww2.insert(3,'ZERO') , ww2.insert(4,'MIG-1')
print(jatos,"\n",ww2)
'''O Insert demostrou Prioridade\superioridade sobre os parametros de inserção [1:1]
(que são posições indicadas de onde eles devem ser colocados na lista
Então: Os Parametros\posições [2:2 ou neste caso 1:1] ocupam somente as posições
que não forem reivindicadas pelo comando INSERT. Este ultimo sempre terá prioridade
na inserção de dados em listas'''

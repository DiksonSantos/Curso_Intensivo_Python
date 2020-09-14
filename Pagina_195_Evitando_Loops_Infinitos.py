'''x = 1
while x <= 5:
    x = x + 1   #Ou x+ = 1
    print(x)'''

'''
ingredientes = []

boas_vindas = '\nInserir Os Ingredientes: '
boas_vindas += '\n Montar Pizza: '
chave = 'Fim'
ready = 'Pronto'
entrada = input(boas_vindas)
ingredientes.append(entrada)
while entrada != chave:
    entrada = input(boas_vindas)
    break
if entrada == ready:
    print('Pizza Concluida')
    breakpoint()
'''

'''
# 7.4 - Ingredientes para Uma Pizza  - Pagina 196
boas_vindas = '\nInserir Os Ingredientes: '
boas_vindas += '\n Montar Pizza: '
ready = True
ingredientes = []
while ready:
    message = input(boas_vindas)
    print(message+'\tSerá Adicionado Á Pizza')
    ingredientes.append(message)
    if  message == 'Fim:':
        active = False
        break   # Sem Esse Break Aqui, o Programa Continua Perguntando 'Qual Ingrediente ' ...
        print('Pizza Concluida' )
print('Seus Ingredientes Foram {}'.format(ingredientes)+'\tBom Apetite')
#Funcionou Perfeitamente EU FIZ ISSO !!! UHHUUU
'''

'''
#7.5 - iNGRESSOS pARA cINEMA:
idade = 0
while idade == 0:
        idade = int(input('Digite Sua Idade: '))
        if idade <3 :
            print('Ingresso Gratuito')

        if idade >3 and idade <= 12 :
            print('Ingrasso Custam 10 US Dolares ')
        elif idade > 15:
            print('Ingressos Custam 15 Dolares')
        break
#Sucesso !!! Uhuu
'''

'''# 7.6 - Três Saidas:
prompt = 'Ola Insira Exit Se Quiser Sair'
active = True
while active:
    message = input(prompt)
    if  message == 'Exit':
        active = False
        break
    print('Game Over')
#Se for só Isso mesmo é Uma mera copia de um exercicio passado com a simples adição do Break :/
'''

# 7.7 - Infinito:
x = 1
while x <= 5:
    #x = x + 1   #Ou x+ = 1
    print(x)
# Ok We Did It. Um Laço que nunca termina . Muito Facil!

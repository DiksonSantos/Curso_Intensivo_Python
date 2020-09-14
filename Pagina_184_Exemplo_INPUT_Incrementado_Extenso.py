prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += '\nWhat Do You Wish Sir? '    #Através deste metodo aqui você pode acrescentar quantas linhas quiser. -> Var += "Frase
prompt += "\nWhat is your first name? "
name = str(input(prompt))     #Acrecentei por minha conta este STR
print("\nHello, " + str(name) + "!")  #Se Não Repetir o STR Aqui em baixo o programa Não Funciona !

'''
# Pagina 185 -> Convertendo o valor de variaveis.

age = input('How Old Are You') #Recebe um valor Python trata-o como STR
age = int(age)                              #  ->   Aqui a variavel é convertida com este metodo
age >= 18 #Aqui é tratado como Numerica
True # O Resultado OK 
'''


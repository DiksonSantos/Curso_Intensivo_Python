

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active: #Enquanto active estiver True Printe a Mensagem
    message = input(prompt)
    if  message == 'quit': #Se a mensagem for = quit a Var active se torna Falsa
        active = False
    print('Game Over')
else:
    print(message)

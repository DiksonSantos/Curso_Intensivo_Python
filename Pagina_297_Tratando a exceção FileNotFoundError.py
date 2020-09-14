
nome_arq = 'ce.txt'
try:
    with open(nome_arq) as n_obj:
        conteudo = n_obj.read()
except FileNotFoundError: #CUIDADO COM O PREENCHIMENTO AUTOMATICO ...
    Mensagem = "Desculpe '" + nome_arq + "' Não Encontrado Ou Não Existe :/"
    print(Mensagem)
    #pass


'''
filename = 'ce.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

'''


def print_models(unprinted_designs, completed_models):
    """Simula a impressão de cada design, até que não haja mais nenhum.
Transfere cada design para completed_models após a impressão."""

    while unprinted_designs: # Ou -> Enquanto a Lista Unprinted Design existir...
        current_design = unprinted_designs.pop() # Current Design Foi Criada para Receber Unprinted_Design (Que é a Lista Inicial\Cheia.
            # Simula a criação de uma impressão 3D a partir do design
        print("Printing model: " + current_design)
        completed_models.append(current_design) #completed_models Recebeu o que passou por Current_Design


def show_completed_models(completed_models):
    """Mostra todos os modelos impressos."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']

completed_models = []

print_models(unprinted_designs, completed_models) # ISTO É UMA FUNÇÃO QUE IMPRIME, E NÃO UM PRINT !
show_completed_models(completed_models) #ISTO TAMBÉM ! OU, FAZ O QUE ESTA NO INTERIOR DA FUNÇÃO , QUE É IMPRIMIR
#SE FOSSE SOMAR, AI PRECISARIA DE UM PRINT EXTERNO PARA MOSTRAR O RESULTADO DA SOMA, MAS ESTA FUNÇÃO JÁ É ISSO.


#Este codigo é uma das maiores confusões\complicações que eu ja vi
#Disseram que iria deixar o codigo mais eficiente -> Ou mais confuso ? Mais confuso
#Acho esse codigo simplesmente Uma Bagunça em Relação ao anterior, Isso sim.

''' 06-12-18 -> Hoje com a cabeça mais descansada vevo que isso é um joguete bobo de ficar
 inserindo e Retirando 
informações de Listas Diferentes, apenas isto.
'''

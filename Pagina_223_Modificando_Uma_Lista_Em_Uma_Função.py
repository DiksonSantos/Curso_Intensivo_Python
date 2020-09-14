

#O Que faz o .pop() -> removes and returns the last item in the list.
#Começar com alguns Designs que devem Ser Impressos


unprinted_designs = ['Iphone Case', 'Robot Pendant(Robo_Pendente)','Dodecahedron (Poliedro de Doze Faces)']
completed_models = []

#Simula A Impressão de cada Design, até que não Haja Mais Nenhum
#Transfere cada Design Para Completed_Models após a impressão
while unprinted_designs:
    current_design = unprinted_designs.pop()

    #Simula a criação de uma impressão a partir do design
    print("Imprimindo Modelo: " +current_design)
    completed_models.append(current_design) # Rapaz! -> Recebeu a segunda Lista que por sua vez recebeu a primeira Lista.

#Exibe todos os modelos finalizados
print('\nOs Modelos a seguir Foram Impressos: ')
for completed_model in completed_models: # O For Vai percorrer todos os Itens da Lista
    print(completed_model) #Os Itens Individuais de Completed_Models


'''
06-12-18 -> ESTE CODIGO FAZ A MESMA COISA QUE O CODIGO DA PAG 224, MAS NA 224 FOI TERCEIRIZADO Á FUNÇÕES 
'''

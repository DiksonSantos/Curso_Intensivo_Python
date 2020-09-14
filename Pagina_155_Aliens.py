'''Lista =['Novo']
#alien_1 = {'Color':'Green','Pontos': Lista}
alien_0 = {'Color':'Green','Points': [5,6,6,7]} # Se ao inves de uma lista colocasse só um numero tbm da certo
#print(alien_0['Color'])
print(alien_0['Points'] ,'\n',alien_0['Color'])
#print(alien_1['Pontos'])'''

'''Eu coloquei # Mas se tirar Funciona Tudo tbm'''
#__________________________

alien_0 = {'Color':'Green','Points': 5}
new_points = alien_0['Points']
#print("You just earned " + str(new_points) + " points!")

alien_0['x_position'] = 0 #Esta Linha e a de baixo é como se fossem um Append das lisatas
alien_0['y_position'] = 25  #...Mas são para dicionarios
print(alien_0)

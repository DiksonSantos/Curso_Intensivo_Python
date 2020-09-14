#Velô do verdinho
alien_0 = {'X_Position':1, 'Y_Position': 25, 'Speed': 'Fast'} #Ao inves de 1 poderia ser qualquer outra Posição, Assim como Medium Slow Etc...
print('Posição Original = '+ str(alien_0['X_Position']))
# Mova o Alien para a Direita, Determine a distancia que o verdinho deve se deslocar de
#acordo com a sua velocidade Atual

if alien_0['Speed'] == 'Slow':
    x_increment =10
elif alien_0['Speed'] == 'Medium':
    x_increment = 20
elif alien_0['Speed'] == 'Fast':
    x_increment = 40
else:
    x_increment = 30
# A nova posição é a posição antiga somada ao incremento.
alien_0['X_Position'] = alien_0['X_Position'] + x_increment

print('Nova_Posição = ' +str(alien_0['X_Position']))  # Ou seja Pos Origi = 0 + Incremento =2


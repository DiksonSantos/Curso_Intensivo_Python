'''
#8.6 Nomes de Cidades
Cidade = str(input('Cidade: '))
Pais = str(input('País'))

def city_country(cidade=Cidade, pais=Pais):
    print(Cidade.upper()+'\n' +Pais.upper())
    #print(''+Pais.upper())


city_country(Cidade,Pais)
#Esta Função Almentou o tamanho das letras. OK
'''

'''
#8.7 Album:
for p in range(1,2):
    Artista = str(input('Nome Do Cantor: '))
    Album = str(input('Disco: '))
    Numero = int(input('Numero De Faixas: '))

def make_album(Cantor,LP):
    Dados ={'name':Cantor,'Record':LP}
    if Numero:
        Dados ['Faixa'] = Numero
    return  Dados             #Sem o Return ele não mostra nada no print Ou mostra NONE

Mostrar = make_album(Artista,Album)
print(Mostrar)
'''


#8.8 Albuns Dos Usuarios:
'''def make_album(artist, title_, tracks=0): # Como Track Vai receber Um Valor Numerico, ele colocou o valor 0, No outro Exercicio foi colocado ''
    """Construir Um Dicionario COntendo Informações SObre Um ALbum"""
    album_dicionario = {'Artista':artist.title(), 'Titulo': title_.title()}
    if tracks:
        album_dicionario['Faixas'] = tracks
    return album_dicionario
# Preparando Os Prompts.
Titulo_Prompt = '\n Em Que ALbum Você Esta Pensando? : '
Artista_Prompt = 'Quem é o Cantor?? '

#Deixe o Usuario saber Como Sair.
print('Digite Sair Para Encerrar')

while True:
    Titulo = input(Titulo_Prompt)
    if Titulo == 'Sair':
        break
    Artista = input(Artista_Prompt)
    if Artista == 'Sair':
        break
        
album = make_album(Artista, Titulo )
print(album)'''
# COmparei os dois Codigos. Mas o que eu Digitei inexplicavelemnte não funciona direito, Não se sabe por qual Maldito Motivo!
#____________________________


def make_album(artist, title, tracks: int = 0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = int(tracks)
    return album_dict

# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "
tracks__ = "Quantas Faixas: "

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break

    Faixas = input(tracks__)
    if artist == 'quit':
        break

    album = make_album(artist, title, Faixas)
    print(album)


print("\nThanks for responding!")

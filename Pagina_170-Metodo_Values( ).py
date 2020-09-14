favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
'Andy': 'python',
'Homer':'Java_Script'
}
print("The following languages have been mentioned:")
#O SET Não deixa ser Printado\Mostrado valores Repetidamente.
for lingua in set(favorite_languages.values()):  #Só mostra o que esta Contido em cada Chave.
    print(lingua.title())

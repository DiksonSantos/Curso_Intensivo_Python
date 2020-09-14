favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

if 'erin' not in favorite_languages.keys():
    print('Erin De sua opnião!')

for nome in sorted(favorite_languages.keys()):
    print(nome.title()+ '\tObrigado por dar Sua Opnião')
print('A ORDEM DAS INICIAIS FORAM E - J - P - S  -> ORDEM ALFABETICA')

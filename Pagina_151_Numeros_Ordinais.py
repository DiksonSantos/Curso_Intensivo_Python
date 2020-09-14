#5.11
num = ['1','2','3','4','5','6','7','8','9']
sufixo = ['st', 'nd', 'rd','th']
for nume in num:
    if '1' in nume:
        print(nume+sufixo[0])
    if '2' in nume:
        print(nume+sufixo[1])
    if '3' in nume:
        print(nume+sufixo[2])
for numero in num:
    if numero != '1' and numero != '2' and numero !='3':
        print(numero+sufixo[3])


    '''elif num !='1' and num != '2' and num!='3':
        print(num.pop(0)+sufixo[3])'''
    '''elif num!= '1' and num != '2' and num != '3' :
        print(nume[3:7]+sufixo[3])'''


#Cont Pg:152
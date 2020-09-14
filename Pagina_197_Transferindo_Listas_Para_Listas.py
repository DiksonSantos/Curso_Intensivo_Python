unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users: #While foi retirando usuarios do ultimo para o primeiro
#Enquanto a lista não esvaziar ele não para
    current_user = unconfirmed_users.pop() #Curr_Usr Foi criada P armazenar os Users vindos da unconfirmed_users (É Uma SWAP)

    print('Verifying_User:' + current_user.title()) #A cada laço que um novo nome é Add, ele é exibido aqui.
    confirmed_users.append(current_user) #conf_usr Foi criada P receber os elementos que passaram pela Curr_Usr
print('\nThe Following Users have been Confirmed: ')
for confirmed_user in confirmed_users: #Percorre a lista conf_usr (que acabou de receber os Current_Usrs
    print(confirmed_user.title())

#https://pythonhelp.wordpress.com/2013/06/26/brincando-com-listas/
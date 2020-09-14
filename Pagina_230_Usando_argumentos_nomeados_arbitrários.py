


def construir_Perfil(Primeiro, Ultimo, **user_info):
    Perfil = {}
    Perfil["Primeiro_Nome"] = Primeiro      #Para trabalhar com Este Primeiro Parametro e o Segundo
    Perfil["Ultimo_Nome"] = Ultimo          #É Desta Maneira.
    for chave, valor in user_info.items():  #Para trabalhar com O Chave + Valor, é Desta Aqui.
        Perfil[chave] = valor  #Acredito que Nesta Linha se Define a Forma\Sequencia Como as Informações Serão Organizadas (chave: Valor)
    return Perfil
Perfil_De_Usuario = construir_Perfil("Dikson", "Santos",Local = "Salto", Area="Ciencia_De_Dados", Idade= 31) #o 31 Com ou sem Aspas, FUNCIONA
'''A Varivel a Cima Recebe a Função com o Nome Dikson que esta associado ao Primeiro Parametro da Função (Que se chama 
"Primeiro"), Santos que esta associado ao segundo (Que se chama "Ultimo"), 
->  Local, Area, e Idade estão Em **USER_INFO  
A Diferença Deste Para o 229 , é que Neste Podemos Armazenar CHAVE+VALOR, no 229, só poderia ser armazenado VALORES.
Esta função será apropriada, não importa quantos pares chave-valor adicionais sejam
fornecidos na chamada da função.
'''

print(Perfil_De_Usuario)

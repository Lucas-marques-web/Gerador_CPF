import random 

menu = '''
****** Gerador de CPF ******

Digite o número para: 

[1] Gerar CPF com marcação
[2] Gerar CPF sem marcação
[3] Sair 

****************************

Digite aqui: '''

while True:
    opção = input(menu)  # Solicita a entrada do usuário

    if opção == '1':  # Opção para gerar CPF com marcação
        cpf_gerado = ""  # Reinicia a variável para gerar um novo CPF

        # Loop para gerar cada dígito do CPF
        for numero in range(0, 11):
            if numero == 3 or numero == 6:  # Adiciona ponto após o terceiro e o sexto dígitos
                cpf_gerado += '.'
                cpf_gerado += str(random.randint(0, 9))
            elif numero == 9:  # Adiciona hífen após o nono dígito
                cpf_gerado += '-'
                cpf_gerado += str(random.randint(0, 9))
            else:  # Gera um dígito numérico aleatório para os demais casos
                cpf_gerado += str(random.randint(0, 9))

        print(f'\nO CPF gerado é: {cpf_gerado}')  # Exibe o CPF gerado na tela
    
    elif opção == '2':  # Opção para gerar CPF sem marcação
        cpf_gerado = ""  # Reinicia a variável para gerar um novo CPF

        # Loop para gerar cada dígito do CPF
        for numero in range(0, 11):
            cpf_gerado += str(random.randint(0, 9))  # Gera um dígito numérico aleatório

        print(f'\nO CPF gerado é: {cpf_gerado}')  # Exibe o CPF gerado na tela

    elif opção == '3':  # Opção para sair do programa
        break  # Encerra o loop e finaliza o programa
    
    else:  # Opção inválida
        print('Opção inválida')  # Exibe uma mensagem de erro

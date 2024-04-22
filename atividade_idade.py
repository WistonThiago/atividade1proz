def inserirDados():
    data = False
    while (data == False):
        try:
            nome = str(input("Digite o seu nome completo: "))
            year = int(input("Digite o ano de seu nascimento: "))
            if (year < 1922):
                print("Aceitamos apenas anos maiores que 1922 e menores que 2021. Tente novamente!")
            elif (year > 2021):
                print("Aceitamos apenas anos menores que 2021 e maiores que 1922, tente novamente.")
            else:
                print(f"Seu nome é {nome}.")
                print(f"Você nasceu no ano de {year}.")
                break
        except:
            print("Você digitou uma entrada inválida, tente novamente!")
inserirDados()
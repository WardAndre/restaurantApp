import os

restaurantes = []

def exibir_nome_programa():
    print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
""")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def finalizar_app():
    os.system('clear')
    print("Finalizando o app\n")

def opcao_invalida():
    print("Opção inválida\n")
    input("Digite uma tecla para voltar ao menu principal: ")
    main()

def cadastrar_restaurante():
    os.system("clear")
    print("Cadastro de novos restaurantes\n")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")
    input("Digite uma tecla para voltar ao menu principal: ")
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            print("Listar restaurantes")
        elif opcao_escolhida == 3:
            print("Ativar restaurante")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system("clear")
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()
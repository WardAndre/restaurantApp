import os

restaurantes = [{"nome": "Pizza", "categoria": "Italiana", "ativo": False},
                {"nome": "Cheesecake", "categoria": "Doce", "ativo": True},
                {"nome": "Sushi", "categoria": "Japonesa", "ativo": True}]

def exibir_nome_programa():
    print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
""")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar / desativar restaurante")
    print("4. Sair\n")

def finalizar_app():
    exibir_subtitulo("Finalizando o app")

def voltar_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()

def opcao_invalida():
    print("Opção inválida")
    voltar_menu_principal()

def exibir_subtitulo(texto):
    os.system("clear")
    linha = "*" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurante():
    """
    Essa função é responsável por cadastrar um novo restaurante
    Inputs:
    - Nome do restaurante
    - Categoria
    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    """
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_restaurante}: ")
    dados_restaurante = {"nome": nome_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")
    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes")
    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status")
    for i in restaurantes:
        nome = i["nome"]
        categoria = i["categoria"]
        ativo = "ativado" if i["ativo"] else "desativado"
        print(f". {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    voltar_menu_principal()

def ativar_desativar_restaurante():
    exibir_subtitulo("Alterar status do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o status: ")
    restaurante_encontrado = False
    for i in restaurantes:
        if nome_restaurante == i["nome"]:
            restaurante_encontrado = True
            i["ativo"] = not i["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if (
                i)["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")
    voltar_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            ativar_desativar_restaurante()
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
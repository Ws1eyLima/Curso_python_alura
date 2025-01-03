import os

restaurantes = [ "Pizza", "Lanche"]


def exibir_nome_do_programa():
    print("""
    Sabor Express
    -------------------------
    [1] Cadastrar Restaurante
    [2] Listar Restaurante
    [3] Ativar Restaurante
    [0] Sair
    """)

def cadastrar_restaurante():
    os.system("cls")
    print("Cadastro de novos Restaurante\n")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    print(f"O Restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    input("Digite Enter para voltar ao menu principal: ")
    main()

def listar_restaurante(): 
    os.system("cls")
    print("Listagem de Restaurante\n")
    for index, restaurante in enumerate(restaurantes):
        print(f"{index + 1} - {restaurante}")
    print("\n")
    input("Digite Enter para voltar ao menu principal: ")
    main()

def finalizar_app():
    os.system("cls")
    print("Encerrando o App\n")

def opcao_invalida():
    input("Digite uma tecla para voltar ao menu principal: ")
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            print("Ativar Restaurante")
        elif opcao_escolhida == 0:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    os.system("cls")
    exibir_nome_do_programa()
    escolher_opcao()

if __name__ == "__main__":
    main()
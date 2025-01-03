import os

def exibir_nome_do_programa():
    print("""
    Sabor Express
    -------------------------
    [1] Cadastrar Restaurante
    [2] Listar Restaurante
    [3] Ativar Restaurante
    [0] Sair
    """)

def finalizar_app():
    os.system("cls")
    print("Encerrando o App\n")

def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opção: "))

    if opcao_escolhida == 1:
        print("Cadastrar Restaurante")
    elif opcao_escolhida == 2:
        print("Listar Restaurante")
    elif opcao_escolhida == 3:
        print("Ativar Restaurante")
    else:
        finalizar_app()


def main():
    exibir_nome_do_programa()
    escolher_opcao()

if __name__ == "__main__":
    main()
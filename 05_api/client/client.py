from client_controller import ClientController

def main():
    client = ClientController()
    while True:
        print("\nOpções:")
        print("1. Listar todos os cursos")
        print("2. Obter detalhes de um curso")
        print("3. Criar um novo curso")
        print("4. Atualizar um curso existente")
        print("5. Excluir um curso")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            client.listar_cursos()
        elif opcao == "2":
            client.obter_curso()
        elif opcao == "3":
            client.criar_curso()
        elif opcao == "4":
            client.atualizar_curso()
        elif opcao == "5":
            client.excluir_curso()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

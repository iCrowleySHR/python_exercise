from src.functions import verifyEmail
 
def main():
    print("Digite um email: ")
    email = input()

    if verifyEmail(email):
        print("\nEmail válido")
    else:
        print("\nEmail inválido")


if __name__  == "__main__":
    main()
    input('\nPressione Enter para sair...')
from src.functions import sum, subtract, multiplication, division

def main():
    print('Digite o primeiro valor')
    n1 = float(input())

    print('Digite o segundo valor')
    n2 = float(input())

    resultado = show_results(n1, n2)
    print(resultado)

def show_results(n1, n2):
    result = (
        f"Soma: {sum(n1, n2)}\n"
        f"Subtração: {subtract(n1, n2)}\n"
        f"Vezes: {multiplication(n1, n2)}\n"
        f"Divisão: {division(n1, n2)}\n"
    )
    return result

if __name__ == "__main__":
    main()
    input("\n Pressione Enter para sair...")
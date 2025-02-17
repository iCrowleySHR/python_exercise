from src.functions import eachLetter, printPrefixes, printPrefixesInLine

def main():
    print("Digite um nome")
    name = input()

    result = (
        f"\n===== Cada Letra Separada =====\n"
        f"{eachLetter(name)}\n"
        f"================================\n"
        f"\n===== Prefixos em Linhas =====\n"
        f"{printPrefixes(name)}\n"
        f"================================\n"
        f"\n===== Prefixos na Mesma Linha =====\n"
        f"{printPrefixesInLine(name)}\n"
    )

    print(result)

if __name__ == "__main__":
    main()
    input("\n Pressione Enter para sair...")
from src.functions import eachLetter, printPrefixes, printPrefixesInLine

def main():
    print("Digite um nome")
    name = input()

    result = (
        f"{eachLetter(name)}"
        f"\n================================ \n"
        f"{printPrefixes(name)}"
        f"\n================================ \n"
        f"{printPrefixesInLine(name)}"
    )

    print(result)

if __name__ == "__main__":
    main()
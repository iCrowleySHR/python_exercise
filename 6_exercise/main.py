from random import choice, sample

def main():
    print("Sorteio de números de 1 a 10")
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print(choice(my_list))
    print(sample(my_list, 5))
    print(sample(my_list, 10))


if __name__ == "__main__":
    main()
    input("\n Pressione Enter para sair...")
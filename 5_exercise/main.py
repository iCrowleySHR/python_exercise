from src.functions import createColumn, createLine

def main():
   
   print("Quantos valores na primera linha? ")
   userLine = int(input())
   
   print("Quantas colunas?")
   userColumn = int(input())
   
   line = createLine(userLine)
   result = createColumn(userColumn, line)
   print(result)

if __name__  == "__main__":
    main()
    input('\nPressione Enter para sair...')
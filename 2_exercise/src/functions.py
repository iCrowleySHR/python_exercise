def eachLetter(name):
    for x in range(len(name)):
        print (name[x])

def printPrefixes(name):
    for x in range(len(name)):  
        for y in range(x + 1): 
            print(name[y])
        print("\n")

def printPrefixesInLine(name):
    for x in range(len(name)):  
        for y in range(x + 1): 
            print(name[y], end='')
        print('\n') 


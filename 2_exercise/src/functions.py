def eachLetter(name):
    value = ""
    for x in name:
        value += x + "\n"
    return value.strip()  # Remove a última quebra de linha desnecessária

def printPrefixes(name):
    value = ""
    for x in range(len(name)):  
        value += "".join(name[:x + 1]) + "\n"
    return value.strip()

def printPrefixesInLine(name):
    return " ".join(name[:x + 1] for x in range(len(name)))
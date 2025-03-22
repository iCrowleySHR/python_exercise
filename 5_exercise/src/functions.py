def createLine(x):
    value = []
    
    for item in range(x):
        value.append(item)
    return value

def createColumn(column, value):
    format = ""
    for item in range(column):
        format += ''.join(str(value)) + '\n'
    return format
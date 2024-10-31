from functools import reduce

def printTable(results: dict):
    lengths = calculateTableColumnsSize(results)
    for column in results.keys():
        sep = lengths[column]
        print(column.rjust(sep), end="  ")
    print()
    lineSeparatorLength = reduce(lambda x, y : x + y, lengths.values()) + len(lengths)
    lineSeparator = "-" * lineSeparatorLength
    print(lineSeparator)
    i = 0
    while i < len(results["n"]):
        for (column, data) in results.items():
            sep = lengths[column]
            print(str(data[i]).rjust(sep), end="  ")
        print()
        i += 1

def calculateTableColumnsSize(results: dict):
    lengths = {}
    for (column, data) in results.items():
        stringLength = calculateColumnStringLength(column, data)
        lengths[column] = stringLength
    return lengths

def calculateColumnStringLength(column, data):
    columnStringLength = len(column)
    elementStringMaxLength = 0
    for element in data:
        elementStringLength = len(str(element))
        elementStringMaxLength = max(elementStringMaxLength, elementStringLength)
    stringLength = max(columnStringLength, elementStringMaxLength)
    return stringLength
    
columns = 20
start = 30
end = 5000


def row(row, columns):
    string = ""
    j = 0
    while j < columns:
        string += chr(row + j) + " "
        j += 1
    return string


def rows(start, end, columns):
    i = start
    while i < end:
        string = row(i, columns)
        print(string)
        i += columns


rows(start, end, columns)

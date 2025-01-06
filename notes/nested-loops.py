# Nested loops are loops inner another loops

rows = int(input(" Number of rows: "))
columns = int(input(" Number of Columns: "))
symbol = input(" Choose a symble: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()
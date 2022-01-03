def printTable(table):
    x = []
    for i in range(len(table[0])):
        for j in range(len(table)):
            x.append(table[j][i])
    for i in range(len(x)):
        if (i+1)%3!=0:
            print(x[i],end=' ')
        else:
            print(x[i])        

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
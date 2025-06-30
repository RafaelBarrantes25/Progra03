amogus = [[1,2,3],
          [4,5,6],
          [7,8,9]]

i = 0 
j = 0
lista = []
for j in range(len(amogus)):
    i = 0
    for i in range(len(amogus[0])):
        lista += [amogus[i][j]]


print(lista)
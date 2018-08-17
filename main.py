num = input()  #Number of Transactions
table = []
members = 4     #Number of Members

for i in range(int(num)):
    table.append(list(map(int, input().split())))
    
for i in range(int(num)):
    construct = []
    sum = 0
    for j in range(0, members):
        sum += table[i][j]
    for j in range(0, members):
        each = sum/members
        table[i][j] -= each 
#    for j in range(0, members):
#        if(table[i][j] > 0):
#           string = "M{} pays M{}, M{}, M{} {} {} {} Respectively".format(j+1, 1, 2, 3, )
#        else:
#                construct.append(j)
    print(table[i])
    
#print(table)

'''Sample Input:
4
100 150 0 500
50 75 100 200
10 10 10 10
50 0 700 50

Output:
M4: 
{'M2': 37.5, 'M1': 87.5, 'M3': 187.5}
M4: 
{'M2': 31.25, 'M1': 56.25, 'M3': 6.25}
{'M4': 0.0, 'M2': 0.0, 'M1': 0.0, 'M3': 0.0}
M3: 
{'M2': 200.0, 'M1': 150.0, 'M4': 150.0}
'''

num = input()   #Number of Transactions
table = []
members = 4     #Number of Members

for i in range(int(num)):
    table.append(list(map(int, input().split())))
    
for i in range(int(num)):
    dic = {}
    k = 1
    construct = []
    sum = 0
    for j in range(0, members):
        sum += table[i][j]
    for j in range(0, members):
        each = sum/members
        table[i][j] = each - table[i][j]
        if(table[i][j] >= 0):
            dic["M"+str(k)] = table[i][j]
            k += 1
        else:
            print("M"+str(k)+": ")
            k += 1        
    print(dic)

list_N =[]
for i in range(9):
    N=int(input())
    list_N.append(N)
A= list_N.index(max(list_N))+1
print(max(list_N),A)
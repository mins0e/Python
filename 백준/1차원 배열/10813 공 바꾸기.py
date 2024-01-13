N,M=map(int,input().split())
basket=[0]*N
for x in range(N+1):
    basket[x-1] = x

for x in range(M):
    i,j =map(int,input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
#for x in range(N):
#    print(basket[x],end=' ') 
print(*basket)  


    
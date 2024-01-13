N,M=map(int,input().split())
basket= [0]*N
for i in range(M):
    i,j,k = map(int,input().split())
    for x in range(i,j+1):
        basket[x-1]=k
# i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다는 뜻이다.      
for i in range(N):
    print(basket[i],end=' ')
    
    
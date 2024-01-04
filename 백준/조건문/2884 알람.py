A,B= map(int,input().split())

if B>=45:
    print(A, B-45)
elif B<=45:
    if A-1 == -1:
        A=24
        print(A-1, 60-(45-B))
    else:
        print(A-1, 60-(45-B))
    
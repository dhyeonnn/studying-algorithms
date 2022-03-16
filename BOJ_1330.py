# 1330번: 두 수 비교하기

a,b=map(int,input().split())
print(['><'[a<b],'=='][a==b])
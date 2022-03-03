'''짝수와 홀수의 판별은 2로 나눴을 때 나머지가 0인가 1인가? 로 알 수 있고

"*" 하나로 생각하는게 아니라 "* " 과 " *" 이렇게 공백과 별을 하나로 생각해서 출력하려고 해보면 됩니다!
'''

n = int(input())

for i in range(n):
    if i % 2 == 0:
        print("* " * n)
    else:
        print(" *" * n)

# n = int(input())
# line = "* " * n

# for i in range(n):
#     print(line)
#     line = line[::-1]

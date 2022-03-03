# 2562번: 최댓값

'''
num_list = []
for numbers in range(9):
    num_list.append(int(input()))

print(num_list)
print(max(num_list))
print(num_list.index(max(num_list))+1)
'''

num_list = [int(input()) for numbers in range(9)]

print(max(num_list))
print(num_list.index(max(num_list))+1)

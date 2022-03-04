# 946 : 기타 자료형 - 자가진단 6

capital = dict()
number = int(input())

for i in range(number):
    country, city = input().split()
    capital[country] = city

which_country = input()
print(capital[which_country] if which_country in capital else 'Unknown Country')
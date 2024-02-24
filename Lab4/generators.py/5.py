#ex5
def Generate(n):
    while n >= 0:
        yield n
        n -= 1

num = int(input())
for number in Generate(num):
    print(number)
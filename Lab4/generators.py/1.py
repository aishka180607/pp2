#ex1
def Generate(n):
    for i in range(1, n + 1):
        yield i**2

num = int(input())
for square in Generate(num):
    print(square, end = " ")

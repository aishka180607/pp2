#ex2
def Generate_Even(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

def main():
    even_num = Generate_Even(n)
    print(*even_num, sep = ", ")

n = int(input())
if __name__ == "__main__":
    main()
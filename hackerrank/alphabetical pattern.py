def print_rangoli(size):
    for i in range(n):
        for j in range (i,2*n-3):
            print("-",end="")
        for j in range (i+1):
            print("*",end="")
        for j in range(i):
            print("*",end="")
        for j in range(2*n-3,i,-1):
            print("-",end="")
        print()

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
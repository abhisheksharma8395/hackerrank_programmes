if __name__ == '__main__':
    b = int(input())
    array1 = map(int, input().split())
    array2 = list(set(array1))
    array2.sort()
    print(array2[-2])   
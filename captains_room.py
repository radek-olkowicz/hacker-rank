if __name__ == '__main__':
    K = int(input())
    arr = [int(item) for item in input().split()]
    print((sum(set(arr))*K-sum(arr))//(K-1))

        
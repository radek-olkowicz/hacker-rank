if __name__ == '__main__':
    #A = list(map(int, input().split()))
    #B = list(map(int, input().split()))
    A = [1, 2, 3]
    B = [9, 8, 7]
    print([(a, b) for a in A for b in B])
    print(*[(a, b) for a in A for b in B])
from collections import Counter

if __name__ == '__main__':
    X = int(input())
    store = Counter(map(int, input().split(" ")))
    N = int(input())
    total = 0
    for _ in range(N):
        order = list(map(int, input().split()))
        if (order[0] in store.elements()):
            total += order[1]
            store.subtract(Counter([order[0]]))
    print(total)
    
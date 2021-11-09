
if __name__ == '__main__':
    N, X = list(map(int, input().split()))
    arr = []
    for _ in range(X):
        #arr.append(list(map(float, "89 90 78 93 80".rstrip().split())))
        #arr.append(list(map(float, "90 91 85 88 86".rstrip().split())))
        #arr.append(list(map(float, "91 92 83 89 90.50".rstrip().split())))
        arr.append(list(map(float, input().rstrip().split())))

    for avg in [sum(x)/len(x) for x in list(zip(*arr))]:
        print(avg)
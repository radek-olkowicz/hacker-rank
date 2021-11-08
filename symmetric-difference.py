
if __name__ == '__main__':
    M = int(input())
    a_set = set(map(int, input().split()))
    N = int(input())
    b_set = set(map(int, input().split()))
    for item in sorted(list((a_set.union(b_set)).difference(a_set.intersection(b_set)))):
        print(item)


from collections import defaultdict

if __name__ == '__main__':    
    input_params = list(map(int, input().split()))
    A = defaultdict(list)
    for N in range(input_params[0]):
        item = input()
        A[item].append(N+1)
    B = []
    for _ in range(input_params[1]):
        B.append(input())
    for b in B:
        if(len(A[b])>0):
            print(" ".join(map(str, A[b])))
        else:
            print(-1)

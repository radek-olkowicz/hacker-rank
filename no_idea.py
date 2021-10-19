if __name__ == '__main__':
    m, n = input().split()
    inputs = list(map(int, input().split()))    
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    score = 0
    for item in inputs:
        if item in A:
            score += 1
        if item in B:
            score -= 1
    print(score)
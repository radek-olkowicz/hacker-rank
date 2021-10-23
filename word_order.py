from collections import OrderedDict

if __name__ == '__main__':
    words = OrderedDict()
    N = int(input())
    for _ in range(N):
        word = input()
        if word in words.keys():
            words[word] += 1
        else:
            words[word] = 1
    print(len(words))
    print(*words.values())
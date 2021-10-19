n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    command = input()
    if (command == "pop"):
        s.pop()
    else:
        comm, num = command.split()
        if (comm == "discard"):
            s.discard(int(num))
        if (comm == "remove"):
            s.remove(int(num))
print(sum(s))
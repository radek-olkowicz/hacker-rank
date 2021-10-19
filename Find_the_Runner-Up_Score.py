def runner_up(input_arr):
    sorted = input_arr
    sorted.sort(reverse=True)
    print(sorted)
    max = sorted[0]
    for item in sorted:
        if item<max:
            print(item)
            break

if __name__ == '__main__':
    #n = int(input())
    #arr = map(int, input().split())

    arr = [2, 3, 6, 6, 5]
    runner_up(arr)
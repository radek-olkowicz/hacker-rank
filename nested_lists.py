def second_lowest(input_list):
    scores = []
    for item in input_list:
        scores.append(item[1])
        scores.sort()
    first = scores[0]
    i = 1
    while scores[i] == first:
        i += 1
    second = scores[i]
    names = []
    for item in input_list:
        if second == item[1]:
            names.append(item[0])
    names.sort()
    for name in names:
        print(name)



if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    second_lowest(records)

        
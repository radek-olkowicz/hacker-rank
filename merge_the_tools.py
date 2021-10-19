def dedup(input):
    arr = []
    tmp = ""
    for ch in input:
        if ch not in arr:
            tmp += ch 
            arr.append(ch)
    return tmp

def merge_the_tools(string, k):
    # your code goes here
    parts = int(len(string)/k)
    words = []
    for i in range(parts):
        words.append(string[int(i*k):int((i+1)*k)])
    for item in words:
        print(dedup(item))

if __name__ == '__main__':
    #string, k = input(), int(input())
    string = "AABCAAADA"
    k = 3
    merge_the_tools(string, k)
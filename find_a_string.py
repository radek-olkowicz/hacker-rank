def count_substring(string, sub_string):
    if(len(sub_string) > len(string)):
        return 0
    counter = 0
    for i in range(len(string)-len(sub_string)+1):
        print(string[i:i+len(sub_string)])
        if string[i:i+len(sub_string)] == sub_string:
            counter += 1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
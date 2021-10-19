
def swap_case(s):
    tmp_output = ""
    for ch in s:
        if(ch.isupper()):
            tmp_output += ch.lower()
        else:
            tmp_output += ch.upper()

            
    return tmp_output

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
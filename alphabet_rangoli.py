def print_rangoli(size):
    if size == 1:
        print("a")
    else:
        A = ord("a")
        canvas = []
        H = 2*size - 1
        W = (2*size - 2)*2 + 1
        em = "--"
        for y in range(size):
            tmp_line = ""
            for x in range(size):
                if (x+y+2 > size):
                    modifier = size-1-x + size-1-y                
                    tmp_line += chr(A+modifier)
                    if (x < size-1):
                        tmp_line += "-"
                else:
                    tmp_line += em
            suff = tmp_line[:-1]
            tmp_list = list(suff)
            tmp_list.reverse()
            suff = "".join(tmp_list)
            tmp_line += suff

            canvas.append(tmp_line)
        for y in range(size-1, 0, -1):
            canvas.append(canvas[y-1])
        for line in canvas:
            print(line)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
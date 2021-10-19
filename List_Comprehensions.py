def list_comp(x, y, z, n):
    list_of_lists = [[xx, yy, zz] for xx in range(x+1) for yy in range(y+1) for zz in range(z+1)]
    output_list = list(filter(lambda item: item[0]+item[1]+item[2] != n, list_of_lists))
    print(output_list)




if __name__ == '__main__':
    x = 1
    y = 1
    z = 2
    n = 3
    list_comp(x, y, z, n)
if __name__ == '__main__':
    N = int(input())
    field_len = str(len("{0:b}".format(N)))
    for i in range(1, N+1):
        format_s = "{0:>" +field_len+ "d}" + " {0:>" +field_len+ "o}" + " {0:>" +field_len+ "X}" + " {0:>" +field_len+ "b}"
        print(format_s.format(i, i, i, i))

if __name__ == '__main__':
    N = int(input())

    proc_list = []
    for i in range(N):
        comm = input()
        if comm == "pop":
            proc_list.pop()
        else:
            if comm == "print":
                print(proc_list)
            else:
                if comm == "sort":
                    proc_list.sort()
                else:
                    if comm == "reverse":
                        proc_list.reverse()
                    else:
                        comm_s = comm.split()
                        if comm_s[0] == "remove":
                            proc_list.remove(int(comm_s[1]))
                        else:
                            if comm_s[0] == "append":
                                proc_list.append(int(comm_s[1]))
                            else:
                                if comm_s[0] == "insert":
                                    proc_list.insert(int(comm_s[1]), int(comm_s[2]))
                                


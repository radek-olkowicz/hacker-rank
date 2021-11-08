from functools import reduce

def find_per(input_dict, query):
    tmp_list = input_dict[query]    
    print('%.2f'%round(sum(tmp_list)/len(tmp_list), 2)) 

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    find_per(student_marks, query_name)

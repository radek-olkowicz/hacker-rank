def minion_game(string):
    game_vowels = "aeiou"
    kev = 0
    stu = 0
    for i in range(len(string)):
        tmp_sum = len(string)-i
        if(string[i].lower() in list(game_vowels)):
            kev += tmp_sum
        else:
            stu += tmp_sum
    if (kev > stu):
        print("Kevin {}".format(kev))
    else:
        if(stu > kev):
            print("Stuart {}".format(stu))
        else:
            print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
if __name__ == '__main__':
    
    students_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        students_list.append([name,score])
    
    score_list = []
    for score in students_list:
        score_list.append(score[1])

    score_list = sorted(list(set(score_list)))

    second_places = []
    for students in students_list:
        if students[1] == score_list[1]:
            second_places.append(students[0])

    second_places = sorted(second_places)
    for seconds in second_places:
        print(seconds)
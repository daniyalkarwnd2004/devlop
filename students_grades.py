def number_mark():
    collection_of_quiz = 0
    midterm_summation = 0
    the_end_of_the_semester = 0
    while True:
        quiz1 = int(input("quiz 1 : "))
        quiz2 = int(input("quiz 2 : "))
        midterm = int(input("midterm : "))
        end_of_the_semester = int(input("end of the semester : "))
        if 0 <= quiz1 <= 10 and 0 <= quiz2 <= 10:
            sum_quiz = (quiz1 + quiz2) * 5
            collection_of_quiz = sum_quiz * 0.25
            print("Sum Quiz : ", collection_of_quiz)
        else:
            print("Enter your mark :)")
        if 0 <= midterm <= 20:
            sum_midterm = midterm * 5
            midterm_summation = sum_midterm * 0.25
            print("Sum Midterm : ", midterm_summation)
        else:
            print("Enter your mark :)")
        if 0 <= end_of_the_semester <= 20:
            sum_end_of_the_semester = end_of_the_semester * 5
            the_end_of_the_semester = sum_end_of_the_semester * 0.5
            print("Sum end of the semester : ", the_end_of_the_semester)
        else:
            print("Enter your mark :)")
        mark = collection_of_quiz + midterm_summation + the_end_of_the_semester
        print("Sum Mark : ", mark)
        if 90 <= mark <= 100:
            print("grade rank : A")
        elif 80 <= mark <= 89:
            print("grade rank : B")
        elif 70 <= mark <= 79:
            print("grade rank : C")
        elif 60 <= mark <= 69:
            print("grade rank : D")
        elif mark < 60:
            print("grade rank : E")
        else:
            print("Error")


number_mark()




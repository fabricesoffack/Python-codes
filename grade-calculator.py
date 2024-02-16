
grade_math = float(input("Enter your grade in math: "))
grade_english = float(input("Enter your grade in english: "))
grade_chemistry = float(input("Enter your grade in chemistry: "))
grade_science = float(input("Enter your grade in science: "))
grade_geography = float(input("Enter your grade in geography: "))

average_grade = (grade_math + grade_english + grade_chemistry + grade_science + grade_geography)/5

if average_grade >= 0 and average_grade <= 100:

    if average_grade >= 90:
        print( f"your average grade is {average_grade}, you passed with an A")

    elif average_grade >= 80:
        print( f"your average grade is {average_grade}, you passed with a B")

    elif average_grade >= 70:
        print( f"your average grade is {average_grade}, you passed with a C")

    elif average_grade >= 60:
        print( f"your average grade is {average_grade}, you passed with a D")    
   
    else:
        print(f"your average grade is {average_grade}, you failed")

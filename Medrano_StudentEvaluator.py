name = "" # GLOBAL VARIABLE

def display_header():
    print("==============================")
    print("STUDENT PERFORMANCE EVALUATOR")
    print("==============================")


def get_student_info():
    name = str(input("Enter student name: "))
    score1 = float(input("Enter Assessment 1: "))
    score2 = float(input("Enter Assessment 2: "))
    score3 = float(input("Enter Assessment 3: "))
    return name, score1, score2, score3

def evaluate_performance(score1, score2, score3):
    average = score1 + score2 + score3/3
    if average <= 74:
        performance_level = "Needs Improvement"
    elif average >= 75:
        performance_level = "Fairly Satisfactory"
    elif average >= 80:
        performance_level = "Satisfactory"
    elif average >= 85:
        performance_level = "Very Satisfactory"
    else:
        print("Outstanding")
    return performance_level

def display_report(score1, score2, score3, average, performance_level):
    print("=============================")
    print("STUDENT REPORT")
    print("=============================")
    print(f"Student Name: {name}")
    print(f"Assessment Scores: {score1}, {score2}, {score3}")
    print(f"Average Score: {average}.2f")
    print(f"Performance Level: {performance_level}")


display_header()
get_student_info()
evaluate_performance()
display_report()

# Chrizzia Jilllian M. Medrano
# 8-Adelfa

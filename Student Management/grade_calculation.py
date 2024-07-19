'''Module 2: Grade Calculation
Implement functions to calculate average grades, highest and lowest grades, 
and grade distribution (e.g., count of A's, B's, etc.)'''


def average_grades():
    total_grades =0

    for student in student_records: # Calculating average grades.
        total_grades += sum(student['grades'])
    average_grades

def highest_grade():
    highest = 0
    for student in student_records: # Finding highest grade
        for grades in student['grades']:
            if grades > highest:
                highest= grade

    return highest

def lowest_grade():
    lowest = 100
    for student in student_records: # Finding lowest grade
        for grades in student['grades']:
            if grades < lowest:
                lowest= grade

    return lowest



def grade_distribution():
    distribution = {'A':0, 'B':0, 'C':0, 'D':0, 'F':0}
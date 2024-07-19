

import csv
from Student Management.student import students

def save_to_file(filename="students.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Grades"])
        for student in students:
            writer.writerow([student["id"], student["name"], ",".join(map(str, student["grades"]))])

def load_from_file(filename="students.csv"):
    global students
    students.clear()
    with open(filename, mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            student_id = row[0]
            name = row[1]
            grades = list(map(int, row[2].split(",")))
            students.append({"id": student_id, "name": name, "grades": grades})

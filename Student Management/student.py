
#Grade Management System

'''Create functions to add, remove, update, and retrieve student information (name, ID, grades).
Use a dictionary or a list of dictionaries to store student records.'''

# Creating an empty list to store student records.

student_records =[]

def add_student(name, ID, grades):

    student={'name':name, 'ID':ID, 'grades':grades} # Dictionary containing user student info

    student_records.append(student) # Add the student to the list
    print(f"Student {name} was added")





def remove_student(ID):

    for student in student_records:  # finding student with matching ID
        if student[ID]==ID:

            student_records.remove(student) # Romoving student from list.
            print(f"Student with ID {ID} was removed" )
            return
    print(f"Student with ID {ID} not found" )    



def retrieve_student(ID):
     
     for student in student_records:  # finding student with matching ID
        if student[ID]==ID:

            return student   # returning the student's info
    return None










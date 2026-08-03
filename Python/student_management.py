import json
import sys

file = {}

def main():
    show_menu()

def show_menu():
    while True:
        print("1. add student")
        print("2. view students")
        print("3. search student")
        print("4. update student")
        print("5. delete student")
        print("6. calculate average")
        print("7. highest scorer")
        print("8. lowest scorer")
        print("9. save data")
        print("10. load data")
        print("11. exit")
        choice = int(input("Enter the choice"))
        if choice == 1:
            name = input("Enter the name of the student")
            id = input("Enter the student id")
            age =  int(input("Enter the age"))
            department = input("Enter the Department")
            sem = int(input("Enter the semester"))
            python = int(input("Enter the marks for Python"))
            sql = int(input("Enter the marks for SQL"))
            ml = int(input("Enter the marks for Machine Learning"))
            student={"Name":name, "ID": id, "Age": age, "Department": department, "Semester": sem, "Marks":{"Python": python, "SQL": sql, "Machine Learning":ml}} 
            add_student(student)
        if choice == 2:
            view_students(file)
        if choice == 3:
            ID = input("Enter the student ID")
            student = search_student(file, ID)
            print(student)
        if choice == 4:
            ID = input("Enter the  student ID")
            update_student(ID)
        if choice == 5:
            ID = input("Enter the student ID")
            delete_student(ID)
        if choice == 6:
            ID =input("Enter the student ID")
            print(calculate_average(ID))
        if choice == 7:
            highest_scorer()
        if choice == 8:
            lowest_scorer()
        if choice == 9:
            save_data()
        if choice == 10:
            load_data()
        if choice == 11:
            exit()

def add_student(student):
    if student["ID"] in file:
        print("Student already exists")
        return
    file[student["ID"]] = student
    
def view_students(file):
    for student in file.values():
        print(student)

def search_student(file, ID):
    student = file.get(ID)
    return student

def update_student(ID):
    student = file.get(ID)
    if student is None:
        print("Student not Found")
        return
    print("1. Name")
    print("2. Age")
    print("3. Department")
    print("4. Semester")
    print("5. Python Marks")
    print("6. SQL marks")
    print("7. Machine Learning marks")

    choice = int(input("Enter your choice "))

    if choice == 1:
        student["Name"] = input("Enter the name")

    elif choice == 2:
        student["Age"] = int(input("Enter the age"))
        
    elif choice == 3:
        student["Department"] = input("Enter the department")
    
    elif choice == 4:
        student["Semester"] = int(input("Enter the semester"))
    
    elif  choice == 5:
        student["Marks"]["Python"] = int(input("Enter the marks of Python"))
    
    elif choice == 6:
        student["Marks"]["SQL"] = int(input("Enter the marks of SQL"))
    
    elif choice == 7:
        student["Marks"]["Machine Learning"] = int(input("Enter the name of Machine Learning"))
    
    print("Student updated successfully")

def delete_student(ID):
    del file[ID]
    print("Successfullly deleted student")

def calculate_average(ID):
    python = file[ID]["Marks"]["Python"]
    sql = file[ID]["Marks"]["SQL"]
    ml = file[ID]["Marks"]["Machine Learning"]
    avg = (python + sql + ml)/3
    return avg

def highest_scorer():
    highest_student=None
    highest_score=-1
    for ID in file:
        avg = calculate_average(ID)
        if avg > highest_score:
            highest_score = avg
            highest_student = file[ID]
    return highest_student

def lowest_scorer():
    lowest_scorer = None
    lowest_score = float("inf")
    for ID in file:
        avg = calculate_average(ID)
        if avg < lowest_score:
            lowest_score = avg
            lowest_scorer = file[ID]
    return lowest_scorer

def save_data():
    with open("students.json", "w") as f:
        json.dump(file, f, indent=4)

    print("Data saved")

def load_data():
    global file
    with open("students.json", "r") as f:
        file = json.load(f)

def exit():
    sys.exit()

if __name__ == "__main__":
    main()
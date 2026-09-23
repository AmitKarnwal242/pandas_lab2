import pandas as pd

df = pd.read_excel(r'C:\Users\walia\OneDrive\Desktop\student_record_50_students.xlsx')

# ==============================
# ***GROUP ANALYSIS***
# ==============================

while True:
    print("\n== GROUP ANALYSIS ==")
    print("1. Find number of students in each department")
    print("2. Find average marks of each department")
    print("3. Find maximum marks in each department")
    print("4. Find minimum marks in each department")
    print("0. Exit from program")

    choice = input("Enter your query no : ")

    if choice == "1":
        count_students = df.groupby("Department")["Name"].count()

        print("\nNumber of students in each department:")
        print(count_students)

    elif choice == "2":
        average_marks = df.groupby("Department")["marks"].mean()

        print("\nAverage marks of each department:")
        print(average_marks)

    elif choice == "3":
        maximum_marks = df.groupby("Department")["marks"].max()

        print("\nMaximum marks of each department:")
        print(maximum_marks)

    elif choice == "4":
        minimum_marks = df.groupby("Department")["marks"].min()

        print("\nMinimum marks of each department:")
        print(minimum_marks)

    elif choice == "0":
        print("Exit from program")
        break

    else:
        print("Invalid input")
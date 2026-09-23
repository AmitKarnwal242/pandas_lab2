import pandas as pd

df = pd.read_excel(r'C:\Users\walia\OneDrive\Desktop\student_record_50_students.xlsx')

# ==============================
# ***DATA MANIPULATION***
# ==============================

while True:
    print("\n== DATA MANIPULATION ==")
    print("1. Add Bonus column")
    print("2. Create FinalMarks column")
    print("3. Create Result column")
    print("4. Create Grade column")
    print("0. Exit from program")

    choice = input("Enter your query no : ")

    if choice == "1":
        df["Bonus"] = 5
        print("\nBonus column added successfully.")
        print(df)

    elif choice == "2":
        df["Bonus"] = 5
        df["FinalMarks"] = df["marks"] + df["Bonus"]

        print("\nFinalMarks column created successfully.")
        print(df)

    elif choice == "3":
        df["Result"] = df["marks"].apply(
            lambda x: "Pass" if x >= 40 else "Fail"
        )

        print("\nResult column created successfully.")
        print(df)

    elif choice == "4":
        def grade(marks):
            if marks >= 90:
                return "A+"
            elif marks >= 80:
                return "A"
            elif marks >= 70:
                return "B"
            elif marks >= 60:
                return "C"
            else:
                return "D"

        df["Grade"] = df["marks"].apply(grade)

        print("\nGrade column created successfully.")
        print(df)

    elif choice == "0":
        print("Exit from program")
        break

    else:
        print("Invalid input")
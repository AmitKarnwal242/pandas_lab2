import pandas as pd

df = pd.read_excel(r'C:\Users\walia\OneDrive\Desktop\student_record_50_students.xlsx')

# ==============================
# ***RANKING***
# ==============================

while True:
    print("\n== RANKING ==")
    print("1. Sort students according to marks")
    print("2. Display top 3 students")
    print("3. Add Rank column")
    print("0. Exit from program")

    choice = input("Enter your query no : ")

    if choice == "1":
        sorted_students = df.sort_values(
            by="marks",
            ascending=False
        )

        print("\nStudents sorted from highest to lowest marks:")
        print(sorted_students)

    elif choice == "2":
        top_students = df.nlargest(3, "marks")

        print("\nTop 3 students:")
        print(top_students)

    elif choice == "3":
        df["Rank"] = df["marks"].rank(
            ascending=False
        )

        print("\nRank column added successfully:")
        print(df)

    elif choice == "0":
        print("Exit from program")
        break

    else:
        print("Invalid input")
import pandas as pd

df = pd.read_excel(
    r'C:\Users\walia\OneDrive\Desktop\student_record_50_students.xlsx'
)

# Rank
df["Rank"] = df["marks"].rank(
    ascending=False
).astype(int)

# Grade
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

# Result
df["Result"] = df["marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

merit_list = df.sort_values(
    by="marks",
    ascending=False
)

merit_list = merit_list[
    [
        "Rank",
        "Roll no",
        "Name",
        "Department",
        "marks",
        "Grade",
        "Result"
    ]
]
print("final merit list:")
print(merit_list)

# Export to Excel
merit_list.to_excel(
    "student_merit_list.xlsx",
    index=False
)

print("\nMerit list exported successfully.")
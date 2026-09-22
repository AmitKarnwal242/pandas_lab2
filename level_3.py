import pandas as pd
df = pd.read_excel(r'C:\Users\walia\Downloads\student_record_50_students.xlsx')
# ==============================
# ***DATA ANALYSIS***
# ==============================
while True:
    print("==DATA ANALYSIS==")
    print("1. calculate average marks")
    print("2. find maximum marks")
    print("3. find minimum marks")
    print("4. find the median of marks")
    print("5. find how many student scored above 75")
    print("6. calculate average marks of BCA students")
    print("7. calculate average marks of MCA students")
    print("8. find the highest scored student in university")
    print("0. exit from program")

    choice = input("enter your query no :")

    if(choice =="1"):
        average_marks = df['marks'].mean()
        print("average of students marks is :",average_marks)
    elif(choice == '2'):
        maxx =df['marks'].max()
        print("maximum marks is:",maxx)
    elif(choice == '3'):
        minn = df['marks'].min()
        print("minimum marks is:",minn)
    elif(choice == '4'):
        mediann = df["marks"].median()
        print("median of student is :",mediann)
    elif(choice == '5'):
        count = (df['marks']>75).sum()
        print("number of students who scored more than 75 is:",count)
    elif(choice == '6'):
        bca_students = df[df['Department'] == 'BCA']
        avg_marks = bca_students['marks'].mean()
        print("Average marks of BCA students:", avg_marks.round())
    elif(choice == '7'):
        mca_students = df[df['Department'] == 'MCA']
        avg_marks = mca_students['marks'].mean()
        print("Average marks of MCA students:", avg_marks.round())
    elif(choice == '8'):
        highest_marks = df.loc[df['marks'].idxmax()]
        print("highest scoring student is:",highest_marks)
    elif(choice== '0'):
        print("exit from program")
        break
    else:
        print("invalid input ")
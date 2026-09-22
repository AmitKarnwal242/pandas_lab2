import pandas as pd 
df = pd.read_excel(r'C:\Users\walia\Downloads\student_record_50_students.xlsx')
    # ==============================
    # ***FILTERING***
    # ==============================
while True:
    print("==DATA FILTERING==")
    print("1. student who scored more than 80 marks")
    print("2. student who scored less than 70 marks")
    print("3. student who scored between 70 to 90 marks")
    print("4. student who belongs to BCA department")
    print("5. student who belongs to MCA department and scored more than 80 marks")
    print("6. student who's age is greater than 21")
    print("0. exit from program")

    user_inp = input("enter your query no.")
    if(user_inp == "1"):
        print(df[df['marks']>80])
    elif(user_inp == "2"):
        print(df[df['marks']<70])
    elif(user_inp == "3"):
        print(df[(df['marks']>=70)&(df['marks']<=90)])
    elif(user_inp == "4"):
        print(df[df['Department']=='BCA'])
    elif(user_inp =='5'):
        print(df[(df['Department']=='MCA')&(df['marks']>80)])
    elif(user_inp == '6'):
        print(df[df['Age']>21])
    elif(user_inp == '0'):
        print("exit ")
        break
    else:
        print("invalid choice")


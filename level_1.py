import pandas as pd
df = pd.read_excel(r'C:\Users\walia\OneDrive\Desktop\student_record_50_students.xlsx')
# ==============================
# ***BASIC OPERATIONS***
# ==============================
while True:
   print("===BASIC OPERATION===")
   print("1. display the dataframe")
   print("2. display first three records")
   print("3. display last three records")
   print("4. find the no. of rows and column")
   print("5. display type name of all column")
   print("6. display data types of all column")
   print("7. display only the (name) column")
   print("8. display name and marks")
   print("0. exit from program")

   #--USER INPUT--
   choice = input("enter your choice/query:")

   #```CONDITIONS```

   if(choice=='1'):
      print(df)
   elif(choice=='2'):
      print(df.head(3))
   elif(choice=='3'):
      print(df.tail(3))
   elif(choice=='4'):
      print(df.shape)
   elif(choice=='5'):
      print(df.columns)
   elif(choice=='6'):
      print(type(df.columns))
   elif(choice=='7'):
      print(df['Name'])
   elif(choice=='8'):
      print(df[['Name','marks']])
   elif(choice=='0'):
      print("exit from program")
      break
   else:
      print("invalid choice")
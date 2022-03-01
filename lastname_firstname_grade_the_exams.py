
import pandas as pd
import numpy as np
#Task1
while True:
    #Task 1
    filename = input("Please enter a class file to grade (.txt):")
    stulist=[]
    
    try:
        with open (filename+".txt","r") as File1:
            data = File1.readlines()
            for line in data:
                stulist.append([line.replace("\n","")])
        stulist = pd.DataFrame(stulist,columns=["Record"])
        print("Successfully opened "+filename+".txt")
        break   

    #File not Found situation
    except FileNotFoundError:
        print("Sorry, I can't find this filename","If you want to open another files, type \"continue\"",sep = "\n")
        res = input()
        if res == "continue":
            pass
        else:
            print("Are you sure want to close the programme?","Type \"Y\" (Yes)",sep = "\n")
            prog_break = input()
            if prog_break == "Y":
                break
            else:
                pass
    
#task 2

#table create
stulist [["Student ID","Answer"]]= stulist["Record"].str.split(",",n=1,expand=True)
stulist["Answer"] = stulist["Answer"].apply(lambda x: x.split(","))
del stulist["Record"]

#data check
stulist["Student Validity"] = stulist["Student ID"].apply(lambda x:"True" if len(x) == 9 and x[0] == "N" and x[1:].isdigit() else "False")
stulist["Answer Validity"] = stulist["Answer"].apply(lambda x:"True" if len(x) == 25 else "False")

#data report
id_error=stulist[stulist["Student Validity"] == "False"]
an_error=stulist[stulist["Answer Validity"] == "False"]
del id_error["Answer Validity"], an_error["Student Validity"]
print("**** ANALYZING ****")
print("Invalid line of data: does not contain exactly 26 values",id_error,sep = "\n")
print("Invalid line of data: does not contain exactly 26 values",an_error,sep = "\n")

print("**** REPORT ****")
print("Total valid lines of data:",len(stulist[(stulist["Student Validity"] != "False")&(stulist["Answer Validity"] != "False")].index))
print("Total invalid lines of data:",len(stulist[(stulist["Student Validity"] == "False")|(stulist["Answer Validity"] == "False")].index))

#Task 3
#New table create
stulist = stulist[(stulist["Student Validity"] != "False")&(stulist["Answer Validity"] != "False")]
del stulist["Student Validity"], stulist["Answer Validity"]

#Create .txt
new_file = open(filename+"_grades.txt","w")

#Scoring
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer_key = answer_key.split(",")
gradelist = []
for index, row in stulist.iterrows():
    answer_position = 0
    student_grade = 0
    for student_answer in row ["Answer"]:
        if student_answer == answer_key[answer_position]:
            student_grade+=4
        elif student_answer =="":
            pass
        else:
            student_grade-=1
        answer_position+=1
    gradelist.append(student_grade)
    new_file.write(row["Student ID"]+","+str(student_grade)+"\n")
    #lồng task4
stulist["Grades"] = gradelist
new_file.close()
#REPORT
print("Mean (average) score:",stulist["Grades"].mean())
print("Highest score:",stulist["Grades"].max())
print("Highest score:",stulist["Grades"].min())
print("Range of scores:",stulist["Grades"].max()-stulist["Grades"].min())
print("Median score:",stulist["Grades"].median())
print("**REVIEW**")
print(stulist)

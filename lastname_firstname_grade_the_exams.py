import pandas as pd
import numpy as np
while True:
    print ("Please enter the name of opened file (.txt).","If it's not file .txt, enter.",sep="\n")
    a = input()
    try:
        with open ("test.txt","r") as File1:
            print(File1.read())  
        print("Task completed")
        break      
    except FileNotFoundError:
        print("File is not in the folder","If you want to open another files, type \"continue\"",sep="\n")
        res = input()
        if res == "continue":
            pass
        else:
            print("Task completed")
            break
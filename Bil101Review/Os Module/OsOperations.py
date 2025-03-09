
import os
print(os.getcwd())

os.chdir("D://temp")

print(os.getcwd())

os.chdir("D:\Academic\Dersler\Bil202\Bil202_End_2024_2025\Bil101Review")

l=os.listdir()

os.mkdir("D:/Temp/Temp2")
print(l)
os.rmdir("D:/Temp/Temp2")

#os.rename("D:/Temp/document2.pdx","D:/Temp/document.pdf")

os.remove("D:/Temp/document.pdf")
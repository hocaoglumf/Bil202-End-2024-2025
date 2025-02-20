
file=open("d:/temp/Dosya.txt","w")

file.write("fatih:hocaoglu:12345")
file.write("\n")
file.close()

file=open("d:/temp/Dosya.txt","r")

dt=file.read()
vr=dt.split(":")
print("İsim: ",vr[0], " Soyisim: ",vr[1]," no:",vr[2])
file.close()

dosya   =open("d:/temp/Dosya.txt","a")
dosya.write("ali:uzun:32")
dosya.write("\n")
dosya.close()

dosya   =open("d:/temp/Dosya.txt","r")
print(dosya.readline().split(":"))
print(dosya.readline().split(":"))

dosya.close()


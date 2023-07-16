m1=int(input("Enter the Mark Subject 1 :"))
m2=int(input("Enter the Mark Subject 2 :"))
m3=int(input("Enter the Mark Subject 3 :"))
m4=int(input("Enter the Mark Subject 4 :"))
m5=int(input("Enter the Mark Subject 5 :"))
total=m1+m2+m3+m4+m5
per=total/5
print("Total :",total)
print("Percentage :",per)
if(per>=60):
	print("First Division..")
elif(per>=50 and per<=59):
	print("Second Division..")
elif(per>=40 and per<=49):
	print("Third Division..")
else:
	print("Fail..")
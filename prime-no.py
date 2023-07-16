n=int(input("Enter the limit\n"))
print(type(n))
for num in range(2, n):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
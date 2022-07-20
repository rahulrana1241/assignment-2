choice = input("Enter operator to use:")
A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
if choice == '+':
   ans=A+B
elif choice == '-':
   ans=A+B
elif choice == '*':
   ans=A+B
elif choice == '/':
   ans=A+B
else:
   print("Invalid input")

print("the answer is",ans)

#patterns
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print(" ")

for i in range(5):
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")

x=0
for i in range(0,5):
    x+=1
    for j in range(0,i+1):
        print(x,end=" ")
    print(" ")

for i in range(6,0,-1):
    for j in range(0, i - 1):
        print("* ", end="")
    print(" ")

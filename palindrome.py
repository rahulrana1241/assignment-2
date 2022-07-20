n = 1441
temp = n
rev = 0


while(n>0):
    dig = n%10
    rev = (rev*10) + dig
    n = n//10
if(temp==rev):
    print("this is palindrome no.")
else:
    print("this is not a palindrome no.")

num = int(input("Enter a number:"))
sum = 0 
n1 = len(str(num))
temp = num 
while temp > 0:
    digit = temp % 10
    sum += digit ** n1
    temp //= 10 
if num == sum: 
    print(num, "is an armstrong number")
else: 
    print(num, "is not an armstrong number")
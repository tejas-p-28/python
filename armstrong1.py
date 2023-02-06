num = int(input("Enter a number:"))
sum = 0
n1 = len(str(num))
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** n1
    temp //= 10
if num == sum:
    print("Number is an armstrong number")
else: 
    print("Number is not an armstrong number")
number1=int('10')
print(type(number1) )
number2=int(input("enter the second number"))
# 10 -integer
#10.0 -decimal
# '2' -string,"q" ,'2334'
#input() out oput alwas string-'10','10.0',

#int()-type casting.

print("Enter which operation would like to perform?")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")

choice = input("Enter choice (1/2/3/4): ")


if choice == "1":
    print("Result:",add(number1,number2))

elif choice == '2':
    print("Result:", subtraction(number1,numbe2))

elif choice == '3':
    print("Result:",multiplication(number1,number2))

elif choice =='4':
    print("Result:", divsion(number1,number2))

else:
    print("Please enter a valid choice.")

          
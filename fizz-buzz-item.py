#This code uses if else statements to return info based on the input.

value = int(input("Enter an integer value: "))

#If the user inputs a multiple of 5 and 3 then the return will be fizzbuzz.

if value % 5 == 0 and value % 3 == 0:
    print("FizzBuzz")

#Input of a multiple of 3 will return a fizz.

elif value % 3 == 0:
    print("Fizz")
    
#Input of a multiple of 5 will return a buzz.
    
elif value % 5 == 0:
    print("Buzz")

#Anything else will just return back the value inputted.    

else:
    print(value)
    
#This code will be use loops to find divisible numbers from the user input.

upper_number = int(input("How many values should we process: "))

#The for loop will start with the number 1 and count up to the number that was input. 
#Note we can tell it is divisible by the returned output.

for number in range(1, upper_number + 1):
    
#Inside the loop we have an if else statement, if its divisible by 5 and 3 then fizzbuzz will be returned.

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
        
#If the number is divisible by 3 then fizz will be returned.
        
    elif number % 3 == 0:
        print("Fizz")
        
#If the number is divisible by 5 the buzz will be returned.
        
    elif number % 5 == 0:
        print("Buzz")
        
#Then if its any other number that isnt divisble then it will be returned normally.
        
    else:
        print(number)


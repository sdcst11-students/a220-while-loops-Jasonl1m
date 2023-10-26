#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""

input = float(input("Enter a number = "))
isEven = False
while input > 0:
    if input != int(input):
        break
    if input % 2 == 0:
        isEven = True
        break
    input = input / 10

if isEven:
    print("The number is an even integer.")
else:
    print("The number is not an even integer.")


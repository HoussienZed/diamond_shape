# prompting user to enter a number x

x = int(input("Enter a number: "))

# printing the upper part of the diamond
for i in range(x):

    # printing the beginning spaces
    for j in range(x - i - 1):
        print(" ", end="")

    # printing the astrices
    for k in range(2 * i + 1):
        print("*", end="")

    print("")

# printing the bottom part of the pyramid
for i in range(x - 1):

    # printing the beginning spaces
    for j in range(i + 1):
        print(" ", end="")

    # printing the astrices
    for k in range(2 * x - 2 * i - 3):
        print("*", end="")

    print("")

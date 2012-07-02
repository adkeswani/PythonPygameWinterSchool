MAX_NUMBERS = 10
numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
numNumbers = 0
finished = False

while numNumbers <= MAX_NUMBERS and not finished:
    print "Enter a number to add it to the store or \"Stop\" to stop entering numbers:"

    userInput = raw_input()

    if userInput == "Stop":
        finished = True
    else:
        numbers[numNumbers] = int(userInput)
        numNumbers = numNumbers + 1

currNumber = 0
while currNumber < numNumbers:
    print "Number", currNumber, "is", numbers[currNumber]

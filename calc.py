# Please write a function in Python which receives a natural decimal N-digit number (0<N<15) as an input 
# and returns the minimal next N-digit number with the same sum of digits or -1 if there isn't one. 
# Examples:
# Input:          Output:
# 123             132
# 0200            1001
# 09999999999999  18999999999999
# 90              -1
# 9999            -1


def nextNumber(input):
    input= str(input)
    # Error if input is not positive number
    if not input.isdigit() or int(input) < 0:
        print("Use positive numbers only")
        return '-1'

    # Add input to a list
    numberList = list(input)
    length = len(numberList)

    # Error if length is not within bounds
    if length <= 0 or length >=15:
        print("Number length must be between 1 and 14")
        return '-1'

    # get sum of input
    originalSum = 0
    for digit in numberList:
        originalSum = originalSum + int(digit)

    # create length exception for numbers starting with 0
    exception = 0
    if int(numberList[0]) == 0:
        exception = 1

    # forever loop (until function returns)
    while True:

        # Check length and return -1 if incorrect
        if exception == 1:
            exception = 1
        elif len(numberList) != length:
            print('-1')
            return '-1'
            break

        # Check Sum and return number if valid
        sum = 0
        for digit in numberList:
           sum = sum + int(digit)

        if sum == originalSum and int("".join(numberList)) != int(input):

            # add zeroes back to the exceptions so it maintains the same length
            if exception == 1 and len(numberList) != length:
                for i in range(length - len(numberList)):
                    numberList.insert(0, "0")

            # return number if valid
            print("".join(numberList))
            return("".join(numberList))
            break

        # Deal with huge differences in sums
        difference = 0
        difference = (originalSum - sum) / 9 
        addValue = "1"
        if difference >= 9:
            addValue=""
            for i in range(int(difference)):
                addValue = addValue +"9"
        else:
            # Deal with multiple trailing zeroes
            zeroes = 0
            for i in range((len(numberList)-1),-1, -1):
                if numberList[i] == "0":
                    zeroes = zeroes + 1
                else:
                    break    

            if zeroes > 0 and difference <= 0:
                addValue = "0"
                nonZeroIndex = (len(numberList) - zeroes) -1
                addValue = str(10 - int(numberList[nonZeroIndex]))
                for i in range(zeroes):    
                    addValue = str(int(addValue) * 10)       

        # if number is irrelevant, check next number
        numberList = (int("".join(numberList))) + int(addValue) 
        numberList = list(str(numberList))

nextNumber('0325')
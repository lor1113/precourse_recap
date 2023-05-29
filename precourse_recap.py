numbers = [1,2,3,4,5,6,7,8,9,10]

def statistics(input):
    mean = sum(input) /  len(input)
    print("The mean of the input is " + str(mean))
    print("The largest number in the input is " + str(max(input)))
    print("The smallest number in the input is " + str(min(input)))


statistics(numbers)
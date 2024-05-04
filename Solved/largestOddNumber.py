def largestOddNumber(num):
    odd_numbers = [1, 3, 5, 7, 9]
    num_str = str(num)

    numbers = [int(number) for number in num_str]

    for number in reversed(numbers):
        if number % 2 != 0:
            return ''.join(map(str, numbers))
        else:
            numbers.pop()
    else:
        return ""
            
        

print(largestOddNumber(24266))
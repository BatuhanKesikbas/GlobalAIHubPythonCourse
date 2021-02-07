# In my function there is a start and a end limits and in for loop i used end+1 to include my last value.
# To find a prime numbers it should be greater than 1 and cannot be divided by any numbers except itself and 1,
# so the range is between 2 and i(i does not counted).
def prime_numbers(start, end):
    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)


prime_numbers(0,100)
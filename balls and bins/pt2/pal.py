def palindrome(number):
    return str(number) == str(number)[::-1]

def largest(min, max):
    if min > max:
        raise ValueError("min cannot be greater than max")
    
    max_palindrome = None
    factor = []

    for i in range(min, (max + 1)):

        for j in range(i, (max + 1)):
            product = i * j

            if palindrome(product) and product > max_palindrome:
                max_palindrome = product
                factor = (i,j)
    
    return (max_palindrome, factor)
    
def smallest(min, max):
    if min > max:
        raise ValueError("min cannot be greater than max")
    
    min_palindrome = None
    factor = []

    for i in range(min, (max + 1)):

        for j in range(i, (max + 1)):
            product = i * j

            if palindrome(product):
                min_palindrome = product
                factor = (i,j)
                return (min_palindrome, factor)
            
    return (min_palindrome, factor)
                
min_factor=int(input("enter the lower limit of the range: "))
max_factor=int(input("enter the higher limit of the range: "))

largest_palindrome, factors_l = largest(min_factor, max_factor)
smallest_palindrome, factors_s = smallest(min_factor, max_factor)

print("largest: ", largest_palindrome, factors_l)
print("smallest: ", smallest_palindrome, factors_s)

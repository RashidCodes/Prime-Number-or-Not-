def is_prime(digit):
    if type(digit) != int:
        print('is_prime() accepts only values of datatype "int"')
        print('enter a valid number')
      
    if digit == 1 and type(digit) == int:
        return False 
    
    if digit == 2 or digit == 3 or digit == 5 or digit == 7 and type(digit) == int:
        return True
    
    if digit == 4 or digit == 6 and type(digit) == int:
        return False
    
    if digit > 7 and type(digit) == int:
        if digit % 3 == 0 or digit % 5 == 0 or digit % 7 == 0 or digit % 2 == 0:
            return False
        else:
            return True
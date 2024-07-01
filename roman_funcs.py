num_to_roman = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}

def to_roman(n):
    result = ''
    if n <= 3 :
        result = n * num_to_roman[1]
    elif n == 4:
        result = num_to_roman[1] + num_to_roman[5]  
    elif n < 9:
        result = num_to_roman[1] + num_to_roman[5]  
    elif n == 9:
        result = num_to_roman[1] + num_to_roman[5]  
    else: 
        result = num_to_roman[1] + num_to_roman[10]
    
    
    return result  

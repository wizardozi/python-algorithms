numbers = [4, 3, 2, 7, 8, 2, 3, 1]

def find_duplicates(numbers):
    duplicates = []    
    for num in numbers:  
        index = abs(num) -1              
        if numbers[index] < 1:                    
            duplicates.append(abs(num))       
        else:                        
            numbers[index] *= -1            
    return duplicates

print(find_duplicates(numbers))
        
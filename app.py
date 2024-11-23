def double_list():
    numbers = input("Enter numbers separated by spaces: ")  
    
    numbers = list(map(int, numbers.split())) 
    
    doubled_numbers = [num * 2 for num in numbers]
    
    print("Original list:", numbers)
    print("Doubled list:", doubled_numbers)

if __name__ == "__main__":
    double_list()

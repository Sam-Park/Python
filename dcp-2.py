nums = [1, 2, 21, 11, 5]
n = len(nums)
def product(nums, n):
    if n == 1: 
        print(0) 
        return
  
    i, temp = 1, 1
  
    # Allocate memory for the product array  
    prod = [1 for i in range(n)] 
  
    # Initialize the product array as 1  
  
    # In this loop, temp variable contains product of 
    # elements on left side excluding arr[i]  
    for i in range(n): 
        prod[i] = temp 
        temp *= nums[i] 
  
    # Initialize temp to 1 for product on right side  
    temp = 1
  
    # In this loop, temp variable contains product of 
    # elements on right side excluding arr[i]  
    for i in range(n - 1, -1, -1): 
        print(range(n - 2, -1 , -1))
        prod[i] *= temp 
        temp *= nums[i] 
  
    # Print the constructed prod array  
    for i in range(n): 
        print(prod[i], end = " ") 
  
    return

print(product(nums, n))
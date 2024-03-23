# searching
# sorting 

# !problem 1 
# ?input 
user_input = [1,2,3,4,5,6,7,8,9,10]

# ?Q: Check to see if a certain number exist in the user array 
n = 14

# linear search
result = False # !a variable to keep track of your answer
for i in user_input:
    if i  == n:
        
        result = True
if result == True:
    print('found')
else:
      print('not found')

# if else, for loops, print, calculation (+, -) 

# Time: o(n)
input = [1,2,3,4,5,6,7,8,9,10]
for i in input:
    print('hi')
    if i == 1:   # o(1)
        break  
    
input = [1,2,3,4,5]
for i in input:
    print('hey')
    if i == 1:   # o(1)
        continue

input = [1]
for i in input:
    for k in input:
        print('---')
        
input = [1,2]
for i in input:
    for k in input:
        for m in input:
            print('---')
            
input = [1,2,1,1,1]
# O(N)
for i in input:    # n^3 + n^2 # n^3
    print('hi') 
    for k in input:     # n
        print('hello')  
    for m in input:     # n^2
            print('hello')
            for l in input: # n
                print('hello')
            

    
            
        

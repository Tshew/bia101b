import random


input_str = "((())())()(((((()()(()())())(()((((((((()))()(())(()())((()))())(((()())))()))(((()))()())()((()(())))((())())())()))))(((())()))()(()((()))(())()())))()()())(()(())))()))((())())()(((()()()()(()(()(((())((((()))))))(())((()(()())())()(())))()()(((((()))))(()))()))(())())))((()))((())))()))()))()(()(()))(()()())(()((((()())((()((()(()))))(()))())((())(((()()()))((((((()()()(()(())(()()()))()()()((((((())()))())()())()))()(())()())(()())()((()))()))))((((())))))())(())((((())))())((())()))(()))())))((())))()))))))((())(())))((())))(())))(())()(()()))(((())()((()()(((()))((()(()))()))))))()))))(()()(((()()((((((())()))()(((((((())())))()()((()))())())(((()(())()((((((())))))))()))))(())((((()((()()(()(())))()((((((())(()))(()))))((()(((()))()))))))(((((())()))(((((((()(()()((()))(())((()())((((()(((()))((()(()))))())())))())())(()))))(())(((())))())))((()(()(((((())))()())()()(((()()))()(()(((((())(())(())))(()())()(()))()((()())))()))())())(()(())()))())(())))(((((()())))()(()))(()()(()(()"

floor_index = 0 #? variable to keep track of the ans
for i in input_str: #! go through each character 
    if i == "(": #? if ( add one to the answer
        floor_index = floor_index + 1
    if i == ")": #? if ) sub one to the answer
        floor_index = floor_index - 1
# print the final answer
print('the final floor is', floor_index)

# ! problem 1
# ? given an input string with just oprn and close brackets
# ? calculate the final floor that the alien will reach at


input_str = "((("

# ! Example 1
# (((())))
# output: 0

# ! (((
# output: 3

for i in range (100):
    input_string =""
    random_bracket = random.randint(0,1)
    if random_bracket == 0:
        input_str = input_str + "("
        
floor_index = 0 #? variable to keep track of the answer      
for i in input_str: #! go through each character
    if i == "(":  # add onr to the answer
        floor_index = floor_index + 1
    if i == ")": # subtract one to the answer
         floor_index = floor_index - 1
    # print the final answer
    print('the final floor ', floor_index)
        
       
       # for pushing github
        # git add
        # git commit -m "floor"
        # git push 
        
        
# ! problem 2
#? scenerio: the alien only understands you
#? if the input is valid
# give a set of open and close brackets
# chech to see if the input is valid

# ! example 1
#? ((()))
# output : True
#? (()
# output: False

input_str = "(((((((()))))))))"
for i in input_str:
   a = "("
for i in input_str:
    b = ")"
if a == b:
    print('true')
else:
    print('flase')




# parenthesis
input_str = "(((())))"

stack = []

for char in input_str:
    if char == "(":
        stack.append(char)
    if char == ")":
        stack.pop()      
    print('true')
else:
    print('false')

print('length of stack:',stack)

input_str = ")))"
stack = []
for char in input_str:
    if char == "(":
        stack.append(char)
    if char == ")":
        stack.pop()
length = len(stack)
if length == 0:
    print('True')
else:
    print("False")
# ! check if user can vote

# ?Get user age from input
# ?convert userinput(str) to int() to number
# ?check if user can vote
    # ?if else statement
    # ?if above 18, print "You can vote"
    # ?if below 18, print "You canot vote"
    
user = input("enter your age: ")
userAge = int(user)
if userAge >= 18:
    print('You can vote')
else:
    print('You cannot vote')

# 3. Check if user can vote
if userAge > 18:
    print('You can vote')
elif userAge < 18:
    print('You cannot vote')
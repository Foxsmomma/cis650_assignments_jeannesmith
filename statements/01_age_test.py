
#Modify this code so that it rejects non-positive inputs for age
# and prompts the user to enter again, and proceed with processing 
# after the user has entered a positive integer
name = input('What is your name?')
age  = int(input('What is your age?'))
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
else:
    print('You are not over the hill')
# git push the changes with message '01_age_test'
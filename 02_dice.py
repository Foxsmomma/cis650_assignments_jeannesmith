#When we role two dice, the score is the sum of the two dice. 
# The score is a random number between 2 and 12.
# Write a program that simulates 100 rolls of two dice 
# and counts the frequencies of each score value.  
# Print is so that score is left aligned in a 10 character column
# and the frequency is right aligned in a 5 character column

# After completing this script, git commit with 'after_02_dice' as the message 
# and git push the repo 
import random
def total_rolls (num_rolls):
    resultcounts = {}
    for i in range(num_rolls):
        roll = random.randint(2,12)
        if roll ==1:
            resultcounts.append(roll)

    return resultcounts
       
def frequencies (frequencycount):
   print(f"{'Score':<10}{'Frequency':>5}")  
   for score,frequency in frequencycount.items():
    print(f"Sum of {score:<10}{frequency:>5}")

frequencycount= total_rolls (100)
frequencies(frequencycount)
















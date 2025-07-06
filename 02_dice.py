#When we role two dice, the score is the sum of the two dice. 
# The score is a random number between 2 and 12.
# Write a program that simulates 100 rolls of two dice 
# and counts the frequencies of each score value.  
# Print is so that score is left aligned in a 10 character column
# and the frequency is right aligned in a 5 character column

# After completing this script, git commit with 'after_02_dice' as the message 
# and git push the repo 










# %%
# %%
import random

def total_rolls (num_rolls):
    resultcounts = {}
    i:0 for i in range(2,13)
    roll = random.randint(2,13)
    resultcounts [roll]+=1
      
    return resultcounts
       
def frequencies (frequencycount):
   

   

   print(f"{'Score':<10}{'Frequency':>5}")
   for score,count in frequencycount.items():
    print(f"{score:<10}{count:>5}")


frequencies(frequencycount)
# %%

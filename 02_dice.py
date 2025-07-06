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
# %%
import random

def total_rolls (num_rolls):
   results = []
   for i in range(num_rolls):
      roll = random.randint(2,12)
      results.append(roll)
   return results

def frequencies (rolls):
   frequencyResults = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
   for j in range(numRolls):
      frequencyResults[rolls[j]] += 1
   return frequencyResults
   

def printResults(rollResults):
   print(f"{'Score':<10}{'Frequency': >5}")
   for i in range(2,13):
      print(f"{i:<10}{rollResults[i]: >5}")

numRolls = 100

rollResults = total_rolls(numRolls)

rollFrequencies = frequencies(rollResults)

printResults(rollFrequencies)
# %%

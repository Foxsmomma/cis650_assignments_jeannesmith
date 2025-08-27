import string 
ascii_letters = string.ascii_letters
print(ascii_letters)

#Assume the user inputs a word.  For each letter in the word, the 
#program will create a coded message by shifting the letter by 3 places
#For example, if the user enters "hello", the program will print "khoor"

# After completing this script, git commit with 'after_07_coded_messages' as the message 
# and git push the repo  

def CodeShift(word, move=3):
 result = ""
 for char in word:
    if char.isalpha():
        begin = ord('a') if char.islower()
        else
        moved = chr((ord(char)))
        result += moved
    else:
      result += char
      return result

userword =input ("Enter Word to code: ")
Finalword=CodeShift(word)
print(f"Input: {userword}")
print(f"Result: {Finalword}")

#this one appears to be stuck!
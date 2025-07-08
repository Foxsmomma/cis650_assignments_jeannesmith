# Using the alignment feature of the f formatter, 
# create script that will print just ONE OF THE SYMMETRIC alphabets in a 10x10 grid
# The symmetric alphabets are A, H, I, M, O, T, U, V, W, X, Y
# For example, if the character you choose is X, the output should be:
"""
X         X
  X      X
    X  X
      X
    X  X
  X      X
 X         X  
"""
# Your code must use at least one loop and the overloaded * operator

# use the overloaded * operator to repeat spaces
# for example " " * 3 will give you "   "
# use the f formatter to align the characters to the left or right

# After completing this script, git commit with 'after_04_symmetric' as the message 
# and git push the repo 

letter = "X"
box=1
for i in range (box):
    if i > box:
      print(f"{letter:>1}" + " "*8+f"{letter:<1}")
    print(f"{letter:>2}",' ' * 4,f"{letter:<2}")
    print(f"{letter:>4}",' ' * 1,f"{letter:<4}")
    print(f"{letter:>6}")
for j in range (box):
  print(f"{letter:>4}",' ' * 1,f"{letter:<4}")
  print(f"{letter:>2}",' ' * 4,f"{letter:<2}")
  print(f"{letter:>1}" + ' ' * 8+f"{letter:<1}")
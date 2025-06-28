# Consider the tax bracket guide at https://thecollegeinvestor.com/wp-content/uploads/2023/11/TCI_-_2024_Federal_Tax_Brackets_1600x974.png
# It shows the tax bracket based on the income and filing status.  For example, a 'Single' with and 
# income $50000 will be in the 22% tax bracket
# Write a script that will prompt the user for an income, and filing status and then print the appropriate tax bracket 
# The user should be allowed to try this code upto 5 times.
# your code should use only if and while statements.  Do not use any
# data structures including lists, dictionaries, tuples, etc,
# Do not use advanced topics including class, or lambda or comprehension 
# or generators to complete this

#git commit -m 'updated 04_tax_brackets' and then
#git push

remainingAttempts = 5

while remainingAttempts > 0:
    income = int(input("Please enter income:"))
    filingStatus = input("Please enter filing status:")
    if filingStatus == 'Single':
        if income <= 11600:
            print("income " + income + " will be in the 10% tax bracket")
        elif income >=11601 and income <= 47150:
            print("income " + income + " will be in the 12% tax bracket")
        elif income >= 47151 and income <= 100525:
            print("income " + income + " will be in the 22% tax bracket")
        elif income >= 100526 and income <= 191950:
            print("income " + income + " will be in the 24% tax bracket")
        elif income >= 191951 and income <= 243725:
            print("income " + income + " will be in the 32% tax bracket")
        elif income >= 243726 and income <= 609350:
            print("income " + income + " will be in the 35% tax bracket")
        elif income >= 609351:
            print("income " + income + " will be in the 37% tax bracket")
    elif filingStatus == 'Married Filing Jointly':
        if income <23200:
            print("income " + income + " will be in the 10% tax bracket")
        elif income >= 23201 and income <= 94300:
            print("income " + income + " will be in the 12% tax bracket")
        elif income >= 94301 and income <= 201050:
            print("income " + income + " will be in the 22% tax bracket")
        elif income >= 201051 and income <= 383900:
            print("income " + income + " will be in the 24% tax bracket")
        elif income >= 383901 and income <= 487450:
            print("income " + income + " will be in the 32% tax bracket")
        elif income >= 487451 and income <= 731200:
            print("income " + income + " will be in the 35% tax bracket")
        elif income >= 731201:
            print("income " + income + " will be in the 37% tax bracket")
    elif filingStatus == 'Head of Household':
        if income < 16550:
            print("income " + income + " will be in the 10% tax bracket")
        elif income >= 16551 and income <= 63100:
            print("income " + income + " will be in the 12% tax bracket")
        elif income >= 63101 and income <= 100500:
            print("income " + income + " will be in the 22% tax bracket")
        elif income >= 100501 and income <= 191950:
            print("income " + income + " will be in the 24% tax bracket")
        elif income >= 191951 and income <= 243700:
            print("income " + income + " will be in the 32% tax bracket")
        elif income >= 243701 and income <609350:
            print("income " + income + " will be in the 35% tax bracket")
        elif income >609351:
            print("income " + income + " will be in the 37% tax bracket")

    remainingAttempts -= 1
print ("No attempts remaining")

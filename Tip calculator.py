#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")

bill = float(input("What was the total bill? $"))

tip = int(input("What percentage would you like?"))

people = int(input("How many people to split the bill?"))

bill_with_tip =  tip / 100 * bill + bill

split_bill = bill_with_tip / people

split_bill = float(round(split_bill,2))
print(f"Each person needs to pay {split_bill}")



#input("What percentage would you like to give?")

#input("How many peopl to split the bill")


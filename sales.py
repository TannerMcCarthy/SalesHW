# Sales Program
# Written by Tanner McCarthy
# 9/20/21
# Prof Fried

packagePrice = 99
discount = 0

#used a while loop so that it will keep running until I am satisfied with the input given to me 
#by the user

#use True so that it will always run
while True:
  #used try and except so that if an error comes up that would crash the program occurs, this keeps
  #the program running and ask the user again for a valid input 
  try:
    numPack = int(input("How many packages did you purchase?\nPackages Purchased: "))
    print("")
  #except ValueError is to catch any error thrown so the program doesnt stop
  except ValueError:
    print("\nINVALID, Please try again\n")
    #continue will continue the program and reask the user for a valid input
    continue

  #this if statement is to make sure that the user does not enter 0 or any negative numebrs 
  #since it would not make sense to have purchased 0 or a negative amount of packages
  if numPack < 0 or numPack == 0: 
    print("\nINVALID, Please try again\n")
    #continue will continue the program and reask the user for a valid input
    continue
  
  #this else is so that when we have a valid input we can break out of this forever running while loop
  else:
    #break will simply break us out of the while loop and continue the rest of the program
    break

#made it its own if statement bc it will read "...purchased 1 package..." and not 
#"...purchased 1 packages...". All of this so that it has correct grammar
if numPack == 1:
  print("Since you purchased", numPack, "package, you are NOT entitled to any discount.")

#elif statements for the rest to check what discount they fall into

elif numPack <= 9:
  print("Since you purchased", numPack, "packages, you are NOT entitled to any discount.")

elif numPack >= 10 and numPack <= 19:
  print("Since you purchased", numPack, "packages, you are entitled to a 10% discount.")
  discount  = .10

elif numPack >= 20 and numPack <= 49:
  print("Since you purchased", numPack, "packages, you are entitled to a 20% discount.")
  discount  = .20

elif numPack >= 50 and numPack <= 99:
  print("Since you purchased", numPack, "packages, you are entitled to a 30% discount.")
  discount  = .30

#else statement and not a elif bc it is the last to run and I do not need to check anything since 
#everything I needed to check has already been checked
else:
  print("Since you purchased", numPack, "packages, you are entitled to a 40% discount.")
  discount  = .40

#math formula to apply the discount to get the total price
totalAmt = packagePrice * numPack*(1 - discount)

#commented this print line out bc the print(f) can format a nonconstant variable
#print("The total cost after applying your discount is", totalAmt )

print(f'The total cost after applying your discount is ${totalAmt:,.2f}.\n' )

#end of the first part of the program




#Start of the second part of the program
#The Fast Freight Shipping Company program

#use True so that it will always run
while True:
  #used try and except so that if an error comes up that would crash the program occurs, this keeps
  #the program running and ask the user again for a valid input 
  try:
    weight = float(input("Please enter the weight of the package.\nPackage weight: "))
    print("")
  #except ValueError is to catch any error thrown so the program doesnt stop
  except ValueError:
    print("\nINVALID, Please try again.\n")
    #continue will continue the program and reask the user for a valid input
    continue

  #this if statement is to make sure that the user does not enter 0 or any negative numebrs 
  #since it would not make sense to have a weight of 0 or a negative weight
  if weight < 0 or weight == 0: 
    print("\nINVALID, Please try again.\n")
    #continue will continue the program and reask the user for a valid input
    continue
  
  #this else is so that when we have a valid input we can break out of this forever running while loop
  else:
    #break will simply break us out of the while loop and continue the rest of the program
    break

#created the variable finalCost
finalCost = float(0)

#test to see if weight is less than 2lbs it applies the correct rpp
if weight <= 2.00:
  finalCost = float(weight * 1.50)
  print(f'The total cost after applying our rate per pound, $1.50, the shipping cost is ${finalCost:,.2f}')
  
#test to see if weight is inbetween 2lbs and 6lbs and applies the correct rpp
elif weight > 2.00 and weight <= 6.00:
  finalCost = float(weight * 3.00)
  print(f'The total cost after applying our rate per pound, $3.00, the shipping cost is ${finalCost:,.2f}')

#test to see if weight is inbetween 2lbs and 6lbs and applies the correct rpp
elif weight > 6.00 and weight <= 10.00:
  finalCost = float(weight * 4.00)
  print(f'The total cost after applying our rate per pound, $4.00, the shipping cost is ${finalCost:,.2f}')

#else statement and not a elif bc it is the last to run and I do not need to check anything since 
#everything I needed to check has already been checked
else:
  finalCost = float(weight * 4.75)
  print(f'The total cost after applying our rate per pound, $4.75, the shipping cost is ${finalCost:,.2f}')


#end of the second part of the program

#end of the entire program 
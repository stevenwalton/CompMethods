# A cash register program to take drinks. Let's pretend we are running a bar so that we can get our spirits and other drinks.

# First we will create an extremely simple class.  This will alow us to use the attributes later in the script.
# For this simple version we need the drink and the price of the drink
class DrinkOrder:
    " A customer's drink order"     # This is the document.  If you output DrinkOrder.__doc__ then we will get this as an output
    drinkCount = 0                  # We plan on counting the number of drinks, and we want to initialize it.  Notice how we are able to
                                    # increment this value though it is at the top

    # We will make our init definition.  Notice the use of self. This is good practice.  You don't have to call it self, you could call it 
    # somerandomvariablethatwillconfuseanyonewhoreadsyourcode but that isn't really user friendly and you'll have to type it many times
    def __init__(self, drink, price):
        self.drink = drink          # We give the attribute of drink to self
        self.price = price
        DrinkOrder.drinkCount += 1  # Every time we define a drink order we increment drinkCount

# Here we are defining our globals.  Good style from more advanced languages, but this is good practice.
order = {}
i = 0
totalCost = 0
space = ' '

# Now we will start taking orders.  Most of this should be familiar to you and the reasons I do things this way.
# If you are confused then go back to previous lectures and examples
while True:
    drink = raw_input("What would you like to drink?: ").lower()
    price = input("How much is that?: ")
    order[i] = DrinkOrder(drink, price) # Like in our lecture, we are using a dictionary to store all our orders

    # Let's ask the user if they want another drink.  This is something that you are suppose to make better
    again = raw_input("Would you like another drink?(y/n): ").lower()
    i += 1
    if again == 'n':
        break

print "\nThank you, your order is:\n"
# Now we want to print all the drinks, price of each drink, and the total.  Since these are generally on a receipt. 
# You can also define the following in a class itself.  Please take this challenge.  We talked about inheritance.  Have your new class inherit the
# attributes from the DrinkOrder class and print out our receipt.  Remember, we can do anything inside classes.  Even loops and conditional statements.
for x in range(0,i):
    spaces = space * (15-len(str(order[x].drink)))  # This is my cleaver method to line things up.  There are many methods to do this, but this is mine.
    print order[x].drink, spaces, ":\t$", order[x].price
    totalCost += order[x].price

totalCost = totalCost * 1.08
print "-" * 27                      # I just counted to get this 
print "Your total is: ", 6*space, "%.2f" % totalCost    # Ditto.  But I did limit the float to only two decimal places.  Notice how I did this.
print "\nThe tax is 8%"
print "Total number of drinks: %d" % DrinkOrder.drinkCount

print "\nThank you, have a nice day"

# If you go back up to take a new order, like you would do in real life, you will want to clear the attributes and clear the dictionary that we used.
# We don't want to waste memory after all.  So clear the memory when we don't need it.

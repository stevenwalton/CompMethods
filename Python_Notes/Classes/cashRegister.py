# A cash register program to take drinks. Let's pretend we are running a bar so that we can get our spirits and other drinks.

class DrinkOrder:
    " A customer's drink order"
    drinkCount = 0

    def __init__(self, drink, price):
        self.drink = drink
        self.price = price
        DrinkOrder.drinkCount += 1

    def displayOrder(self):
        print self.drink, "\t:\t$", self.price

    def displayDrink(self):
        print self.drink

    def displayPrice(self):
        print self.price

order = {}
i = 0
totalCost = 0
space = ' '
while True:
    drink = raw_input("What would you like to drink?: ").lower()
    price = input("How much is that?: ")
    order[i] = DrinkOrder(drink, price)

    again = raw_input("Would you like another drink?(y/n): ").lower()
    i += 1
    if again == 'n':
        break
print "\nThank you, your order is:"
for x in range(0,i):
    spaces = space * (15-len(str(order[x].drink)))
    #order[x].displayOrder()
    print order[x].drink, spaces, ":\t$", order[x].price
    totalCost += order[x].price

totalCost = totalCost * 1.08
print "-" * 27 
print "Your total is: ", 6*space, "%.2f" % totalCost
print "\nThe tax is 8%"
print "Total number of drinks: %d" % DrinkOrder.drinkCount

print "\nThank you, have a nice day"

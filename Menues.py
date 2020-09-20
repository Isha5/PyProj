#create Menu object
class Menu:
  #constructor  
  def __init__(self,name,items,start_time,       end_time):
    self.name=name
    self.items=items
    self.start_time=start_time
    self.end_time=end_time
  
  #prints string rep of an object
  def __repr__(self):
    print('{} menu available from {}am to {}pm'. format(self.name, self.start_time, (self.end_time - 12)))

  def calculate_bill(self, purchased_items):
    sum = 0
    for i in purchased_items:
      if(i in self.items):
        sum += self.items[i]
    return sum

# new object brunch created from Menu class
brunch = Menu('brunch', {'pancakes': 7.50,
     'waffles': 9.00, 
     'burger': 11.00, 
     'home fries': 4.50,
     'coffee': 1.50,
     'espresso': 3.00, 
     'tea': 1.00, 
     'mimosa': 10.50,
     'orange juice': 3.5
  }, 11, 16)
# new object early_bird created from Menu class  
early_bird= Menu('early_bird', {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 15, 18)

# new object dinner created from Menu class
dinner = Menu('dinner', {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17, 23 )

# new object kids created from Menu class
kids = Menu('kids', {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11, 21)

print(brunch)  
# ouput
#   brunch menu available from 11am to 4pm

total_bill = brunch.calculate_bill(['tea', 'espresso'])
print(total_bill)
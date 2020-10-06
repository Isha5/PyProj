class Student():
  def __init__(self,name,year):     #constructor also called dunder method
    self.name=name
    self.year=year
    self.grades=[]
  def add_grade(self, grade):
    if(type(grade) == Grade):
      self.grades.append(grade)
  def get_average(self):
    sum = 0
    for gr in self.grades:
      sum += gr.score
    print('Average is {avg}'.format(avg= sum/len(self.grades)))
    
roger=Student('Roger van der Weyden', 10)
sandro=Student('Sandro Botticelli', 12)
pieter=Student('Pieter Bruegel the Elder', 8)

class Grade():
  minimum_passing = 65
  def __init__(self,score):
    self.score=score
  def is_passing(self,grade):
    if(self.score > self.minimum_passing):
      print('Passed')
    else:
      print('NP')
pieter.add_grade(Grade(100))
pieter.add_grade(Grade(20))
pieter.get_average()
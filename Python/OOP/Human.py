import random
class Human(object):
  def __init__(self, clan=None):
    print 'New Human!!!'
    self.clan = clan


    self.health = 100
    self.strength = 3
    self.intelligence = 3
    self.stealth = 3
  def taunt(self):
    print "You want a piece of me?"
  def attack(self):
    self.taunt()
    luck = round(random.random() * 100)
    if(luck > 50):
      if((luck * self.stealth) > 150):
        print 'attacking!'
        return True
      else:
        print 'attack failed'
        return False
    else:
      self.health -= self.strength
      print "attack failed"
      return False


michael = Human('codingDojo')
jimmy = Human('NINJAS')

# print michael
# print jimmy
#
# michael.taunt()       # when we invoke the function, notice how we didn't pass a parameter

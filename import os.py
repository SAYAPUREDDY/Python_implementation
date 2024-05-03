import os
os.sys.path.append(os.getcwd())  # needed? - yes!!
import person  # as interactive

me = person.Person(70, 176)  # module.Class
me.eat(0.5)  # breakfast
me.eat(1)  # lunch
print('My weight after eat: ', me.getWeight())
me.run(5)
print('My weight after run: ',me.getWeight())
you = person.Person(80, 190)

# Accessing class variable
print('We have now:', person.Person.nPerson, 'persons')
